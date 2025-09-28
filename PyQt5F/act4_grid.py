import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout 
from PyQt5.QtGui import QFont

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Girds")
        self.setGeometry(470,self.height()//4,500,600)
        self.initUI()
    
    def initUI(self):    
        container = QWidget()
        self.setCentralWidget(container)
        
        self.text1 = QLabel("Box1")
        self.text2 = QLabel("Box2")
        self.text3 = QLabel("Box3")
        self.text4 = QLabel("Box4")
        self.text5 = QLabel("Box5")
        self.text6 = QLabel("Box6")
        
        self.text1.setStyleSheet("background-color:red;font-size:20px;color:white;padding:5px")
        self.text2.setStyleSheet("background-color:blue;font-size:20px;color:white;padding:5px")
        self.text3.setStyleSheet("background-color:green;font-size:20px;color:white;padding:5px")
        self.text4.setStyleSheet("background-color:yellow;font-size:20px;color:black;padding:5px")
        self.text5.setStyleSheet("background-color:purple;font-size:20px;color:white;padding:5px")
        self.text6.setStyleSheet("background-color:indigo;font-size:20px;color:white;padding:5px")
        
        grid = QGridLayout()
        
        grid.addWidget(self.text1,0,0)
        grid.addWidget(self.text2,0,1)
        grid.addWidget(self.text3,1,0)
        grid.addWidget(self.text4,1,1)
        grid.addWidget(self.text5,2,0)
        grid.addWidget(self.text6,2,1)
        
        container.setLayout(grid)
        
        
def main():
    app = QApplication(sys.argv)
    Window = mainWindow()
    Window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()