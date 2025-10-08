"""
login_app.py
Simple PyQt5 login + register example using MySQL and secure password hashing.
Fill in DB_CONFIG with your MySQL credentials before running.
"""

import sys
import os
import hashlib
import mysql.connector
from mysql.connector import errorcode

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# -----------------------
#  CONFIG - update these
# -----------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'artha2025',
    'database': 'login'   # create this DB or allow the script to create it
}
# -----------------------

# -----------------------
# Password hashing helpers
# -----------------------
def hash_password(password: str) -> str:
    """
    Return a string containing salt and hash separated by '$'.
    Uses PBKDF2-HMAC-SHA256 (stdlib) with 100,000 iterations.
    """
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)
    return salt.hex() + '$' + dk.hex()

def verify_password(password: str, stored: str) -> bool:
    """
    Verify a password against the stored "salt$hash" value.
    """
    try:
        salt_hex, hash_hex = stored.split('$')
    except ValueError:
        return False
    salt = bytes.fromhex(salt_hex)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)
    return dk.hex() == hash_hex

# -----------------------
# Database helper
# -----------------------
class DBHelper:
    def __init__(self, config):
        self.config = dict(config)
        self.conn = None

    def connect(self):
        if self.conn and getattr(self.conn, 'is_connected', lambda: False)():
            return
        self.conn = mysql.connector.connect(**self.config)

    def close(self):
        if self.conn and getattr(self.conn, 'is_connected', lambda: False)():
            self.conn.close()
            self.conn = None

    def init_db(self):
        """
        Ensure database exists and create 'users' table.
        If the configured database doesn't exist, attempt to create it.
        """
        try:
            self.connect()
        except mysql.connector.Error as err:
            # if DB doesn't exist, create it then reconnect
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                tmp_conf = dict(self.config)
                tmp_conf.pop('database', None)
                conn = mysql.connector.connect(**tmp_conf)
                cur = conn.cursor()
                cur.execute(
                    "CREATE DATABASE IF NOT EXISTS `{}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
                    .format(self.config['database'])
                )
                conn.commit()
                cur.close()
                conn.close()
                # now connect again with database
                self.connect()
            else:
                raise

        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100) UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """)
        self.conn.commit()
        cur.close()

    def add_user(self, username: str, password_hash: str):
        self.connect()
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)",
                        (username, password_hash))
            self.conn.commit()
        finally:
            cur.close()

    def get_password_hash(self, username: str):
        self.connect()
        cur = self.conn.cursor()
        cur.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
        row = cur.fetchone()
        cur.close()
        return row[0] if row else None

# -----------------------
# PyQt5 main window
# -----------------------
class mainWindow(QMainWindow):
    def __init__(self, db_helper: DBHelper):
        super().__init__()
        self.db = db_helper
        self.setWindowTitle("Login")
        self.resize(380, 220)

        # central widget and layout
        central = QWidget()
        self.setCentralWidget(central)

        title = QLabel("Login Form")
        title.setFont(QFont('Sans', 14))
        title.setAlignment(Qt.AlignCenter)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")
        self.register_btn = QPushButton("Register")

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(title)
        vbox.addWidget(self.username_input)
        vbox.addWidget(self.password_input)
        vbox.addWidget(self.login_btn)
        vbox.addWidget(self.register_btn)
        vbox.addWidget(self.status_label)
        central.setLayout(vbox)

        # signals
        self.login_btn.clicked.connect(self.handle_login)
        self.register_btn.clicked.connect(self.handle_register)

    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Input required", "Please enter username and password.")
            return

        try:
            stored = self.db.get_password_hash(username)
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database error", f"DB error: {e}")
            return

        if not stored:
            QMessageBox.warning(self, "Login failed", "Invalid username or password.")
            return

        if verify_password(password, stored):
            QMessageBox.information(self, "Welcome", f"Login successful. Welcome, {username}!")
            self.status_label.setText("Login successful")
            # you can proceed to open the next window here
        else:
            QMessageBox.warning(self, "Login failed", "Invalid username or password.")
            self.status_label.setText("Login failed")

    def handle_register(self):
        username = self.username_input.text().strip()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Input required", "Please enter username and password to register.")
            return

        # check existing
        try:
            if self.db.get_password_hash(username) is not None:
                QMessageBox.warning(self, "Already exists", "Username already taken. Choose another.")
                return
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database error", f"DB error: {e}")
            return

        pw_hash = hash_password(password)
        try:
            self.db.add_user(username, pw_hash)
            QMessageBox.information(self, "Registered", "User registered successfully. You can now login.")
            self.status_label.setText("Registered")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database error", f"DB error: {e}")

# -----------------------
# Application entry point
# -----------------------
def main():
    app = QApplication(sys.argv)

    # setup DB
    db = DBHelper(DB_CONFIG)
    try:
        db.init_db()
    except mysql.connector.Error as e:
        QMessageBox.critical(None, "Database error", f"Cannot initialize DB: {e}")
        return

    window = mainWindow(db)
    window.show()
    exit_code = app.exec_()
    db.close()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
