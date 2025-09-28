import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QDesktopWidget

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Centered + Responsive Grid")
        self.resize(400, 300)   # Set default size
        self.center()           # Center the window
        self.initUI()           # Build UI
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):    
        container = QWidget()
        self.setCentralWidget(container)
        
        boxes = []
        colors = ["red", "blue", "green", "yellow", "purple", "indigo"]
        for i, color in enumerate(colors, start=1):
            lbl = QLabel(f"Box{i}")
            lbl.setStyleSheet(f"background-color:{color}; color:white; font-size:16px;")
            lbl.setMinimumSize(100, 60)  # Makes resizing smoother
            boxes.append(lbl)

        grid = QGridLayout()
        positions = [(i, j) for i in range(3) for j in range(2)]
        
        for pos, box in zip(positions, boxes):
            grid.addWidget(box, *pos)

        container.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    Window = mainWindow()
    Window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
