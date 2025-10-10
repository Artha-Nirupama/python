from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QLabel,QLineEdit,QPushButton,QGridLayout,QVBoxLayout,QMessageBox,QGraphicsDropShadowEffect,QScrollArea
from PyQt5.QtCore import Qt
import sys

from file2 import MainWindowSec

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
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()