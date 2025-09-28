from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt Example")

layout = QVBoxLayout()

label = QLabel("Hello PyQt!")
button = QPushButton("Click")
button.clicked.connect(lambda: label.setText("Clicked!"))

layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
