from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(500, 500)
        self.winGUI()

    def winGUI(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.title = QLabel("Login")
        self.title.setAlignment(Qt.AlignCenter)

        self.labelUser = QLabel("User Name")
        self.labelPassword = QLabel("Password")

        self.textUser = QLineEdit()
        self.textUser.setPlaceholderText("Enter User Name")

        self.textPassword = QLineEdit()
        self.textPassword.setPlaceholderText("Enter Password")

        self.login = QPushButton("Login")

        grid = QGridLayout()

        # Title spans two columns
        grid.addWidget(self.title, 0, 0, 1, 2)

        # Username row
        grid.addWidget(self.labelUser, 1, 0)
        grid.addWidget(self.textUser, 1, 1)

        # Password row
        grid.addWidget(self.labelPassword, 2, 0)
        grid.addWidget(self.textPassword, 2, 1)

        # Login button spans two columns
        grid.addWidget(self.login, 3, 0, 1, 2)

        centralWidget.setLayout(grid)

        self.title.setObjectName("title")

        self.setStyleSheet("""
            QLabel {
                font-size: 20px;
                color: blue;
            }
            QLabel#title {
                font-size: 40px;
            }
            QPushButton {
                border-radius: 5px;
                background-color: green;
                padding: 5px;
            }
            QLineEdit {
                text-align: left;
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
