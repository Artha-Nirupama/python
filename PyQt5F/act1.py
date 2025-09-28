import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

app=QApplication([])
window=QWidget()

window.setWindowTitle("The First One")
window.resize(200,200)

text1 = QLabel("Hello World!")
text2 = QLabel("Apple")
text3 = QLabel("Banana")
text4 = QLabel("Mango")

master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()

row1.addWidget(text1,alignment=Qt.AlignCenter)
row2.addWidget(text2,alignment=Qt.AlignCenter)
row2.addWidget(text3,alignment=Qt.AlignCenter)
row2.addWidget(text4,alignment=Qt.AlignCenter)

master_layout.addLayout(row1)
master_layout.addLayout(row2)

window.setLayout(master_layout)

window.show()
app.exec_()