from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtGui import QFont

from random import choice

app = QApplication([])
Window = QWidget()

Window.resize(300,300)
Window.setWindowTitle("Roll the dice")

mainCol1 = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()

text1 = QLabel("?")
text1.setFont(QFont("Ink Free",30))
text2 = QLabel("?")
text2.setFont(QFont("Ink Free",30))
text3 = QLabel("?")
text3.setFont(QFont("Ink Free",30))

btn1 = QPushButton("Click")

row1.addWidget(text1,alignment=Qt.AlignCenter)
row1.addWidget(text2,alignment=Qt.AlignCenter)
row1.addWidget(text3,alignment=Qt.AlignCenter)

row2.addWidget(btn1,alignment=Qt.AlignCenter)

num1 = ["1","2","3","4","5","6"]
num2 = ["2","3","4","1","6","5"]
num3 = ["4","1","6","3","5","2"]

def fnum():
    x = choice(num1)
    text1.setText(x)
    
    y = choice(num2)
    text2.setText(y)

    z = choice(num3)
    text3.setText(z)

btn1.clicked.connect(fnum)

mainCol1.addLayout(row1)
mainCol1.addLayout(row2)

Window.setLayout(mainCol1)

Window.show()
app.exec_()