import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(0, 0, 1366, 768)

        # Create label
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width(), self.height())

        # Load image
        self.pixmap = QPixmap(r"C:\Users\Artha\Documents\python\python\PyQt5F\img1.jpg")
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)

    def resizeEvent(self, event):
        # Make label always match window size
        self.label.setGeometry(self.width()//4, 0, self.width()//2, self.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
