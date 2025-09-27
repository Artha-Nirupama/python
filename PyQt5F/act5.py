from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

app = QApplication([])

window = QWidget()
window.setWindowTitle("Login")
window.setStyleSheet("background-color: rgba(255,255,255,0.1);")

layout = QVBoxLayout()

label = QLabel("Login")
label.setFont(QFont("Arial", 20))
label.setAlignment(Qt.AlignCenter)

username = QLineEdit()
username.setPlaceholderText("Username")

password = QLineEdit()
password.setEchoMode(QLineEdit.Password)
password.setPlaceholderText("Password")

login_btn = QPushButton("Login")
login_btn.setStyleSheet("""
    QPushButton {background-color: #3498db; color: white; border-radius: 5px;}
    QPushButton:hover {background-color: #2980b9;}
""")

layout.addWidget(label)
layout.addWidget(username)
layout.addWidget(password)
layout.addWidget(login_btn)

window.setLayout(layout)
window.resize(300, 200)
window.show()
app.exec_()
