from PyQt5.QtWidgets import QWidget,QLabel,QMainWindow,QGridLayout,QLineEdit,QDialog

class CheckUnder18(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Componetnts()
        
    def Componetnts(self):
        self.pName = QLabel("Perants Name: ")
        self.pNameIn = QLineEdit()
        self.pContacts = QLabel("Contact Number")
        self.pContactsIn = QLineEdit()