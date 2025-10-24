from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QLabel,QLineEdit,QPushButton,QGridLayout,QVBoxLayout,QMessageBox,QGraphicsDropShadowEffect,QScrollArea
from PyQt5.QtCore import Qt
import sys

from file2 import MainWindowSec
from Inside import MainWindowInside
import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='artha2025',
            database='login',
        )
        self.cursors = self.connection.cursor()
        
    def commits(self):
        self.connection.commit()
        
    def close(self):
        self.cursors.close()
        self.connection.close()
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.components()
        self.css()
        self.layouts()
        self.LayFuntionsCon()
    
    def components(self):
        
        self.topic = QLabel("Login")
        self.topic.setAlignment(Qt.AlignCenter)
        self.topic.setObjectName("topicC")
        shadow = QGraphicsDropShadowEffect()
        shadow.setOffset(2,2)
        shadow.setBlurRadius(5)
        shadow.setColor(Qt.red)
        self.topic.setGraphicsEffect(shadow)
        
        self.uname = QLabel("User name")
        self.unameIn = QLineEdit()
        
        self.password = QLabel("Password")
        self.passwordIn = QLineEdit()         
        
        self.loginBtn = QPushButton("Login")
        
        self.regBtn = QPushButton("Register")
        
    
    def layouts(self):
        mainBlock = QWidget()
        self.setCentralWidget(mainBlock)
        
        mainLayout = QVBoxLayout()
        mainBlock.setLayout(mainLayout)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        
        mainLayout.addWidget(scroll)
        
        mainContainer = QWidget()
        scroll.setWidget(mainContainer)
        
        vBox = QVBoxLayout()
        mainContainer.setLayout(vBox)
        
        grid = QGridLayout()
        
        grid.addWidget(self.topic,0,0,1,2)
        grid.addWidget(self.uname,1,0)
        grid.addWidget(self.unameIn,1,1)
        grid.addWidget(self.password,2,0)
        grid.addWidget(self.passwordIn,2,1)
        grid.addWidget(self.regBtn,3,0)
        grid.addWidget(self.loginBtn,3,1)
        
        vBox.addLayout(grid)
    
    def LayFuntions(self):
        QMessageBox.information(self,"Done","Your Ready to go😁")
        self.hide()
        self.file2 = MainWindowSec()
        self.file2.show()
    
    def LayFuntionsCon(self):
        self.regBtn.clicked.connect(self.LayFuntions)
        self.loginBtn.clicked.connect(self.loginFuntion)
        
    def css(self):
        self.setStyleSheet("""
                           QLabel{
                               font-family:'Times New Roman';
                               font-size:18px;
                           }
                           QLabel#topicC{
                               font-family:'Ink Free';
                               font-size:30px;
                               color:green;
                               border:5px solid black;
                               border-radius:8px;
                           }
                           QPushButton{
                               font-family:'Ink Free';
                               font-size:20px;
                               color:white;
                               background-color:green;
                               border:2px solid black;
                               border-radius:8px;
                               padding:5px;
                               width:100px;
                           }
                           """)
    def loginFuntion(self):
            username = self.unameIn.text()
            password = self.passwordIn.text()
            
            db = Database()
            curser = db.cursors
            
            query = "SELECT * FROM Login WHERE userName = %s AND password = %s " 
            valuses = (username,password)
            
            curser.execute(query,valuses)
            result = curser.fetchone()
            
            if result:
                QMessageBox.information(self,"Login","Login successful!")
                self.hide()
                self.insides = MainWindowInside()
                self.insides.show()
            else:
                QMessageBox.warning(self,"Error!","Login Fails!")      
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()