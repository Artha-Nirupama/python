from PyQt5.QtWidgets import QMainWindow,QWidget,QLabel,QGridLayout,QGraphicsDropShadowEffect,QLineEdit,QRadioButton,QButtonGroup,QCheckBox,QComboBox,QGroupBox,QVBoxLayout,QPushButton,QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class MainWindowSec(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration")
        self.resize(500,300)
        self.components()
        self.LayOutCus()
        self.shadowTopic()
        self.blockShadow(self.Block1)
        self.blockShadow(self.Block2)
        self.blockShadow(self.Block3)
        self.blockShadow(self.Block4)
        self.blockShadow(self.Block5)
        self.css()
        
        
    
    def components(self):
        
        self.Topic = QLabel("Registration")
        self.Topic.setObjectName("RegistrationC")
        self.Topic.setAlignment(Qt.AlignCenter)
        
        self.Block1 = QGroupBox("Personal Information")
        
        self.membership = QLabel("Membership type: ")
        self.rBtnMem1 = QRadioButton("Student")
        self.rBtnMem2 = QRadioButton("Lecture")
        self.rBtnMem3 = QRadioButton("Worker")
        
        self.title = QLabel("Title: ")
        self.titleCombo = QComboBox()
        self.titleCombo.addItems(["Mr.","Miss.","Ms.","Mrs.","Dr.","Prof.","Mx."])
        
        self.name = QLabel("Full name: ")
        self.nameIn = QLineEdit()
        
        self.id = QLabel("NIC or Passport ID number: ")
        self.idIn = QLineEdit()
        
        self.bOD = QLabel("Birth of day: ")
        self.bODIn = QLineEdit()
        
        self.gender = QLabel("Gender: ")
        self.genderIn = QLineEdit()
        
        self.statues = QLabel("Civil Statues: ")
        self.statuesCombo = QComboBox()
        self.statuesCombo.addItems(["Single","Married","Divorced","Other"])
        
        self.Block2 = QGroupBox("If under 18")
        
        self.rBtnUnCheck1 = QRadioButton("Yes")
        self.rBtnUnCheck2 = QRadioButton("No")
        
        self.Block3 = QGroupBox("Course Details")
        
        self.courses = QLabel("Course or Courses:")
        self.cBox1 = QCheckBox("IT(Level3)")
        self.cBox2 = QCheckBox("English(Level3)")
        self.cBox3 = QCheckBox("Software Enginerring")
        self.cBox4 = QCheckBox("CyberSecurity")
        self.cBox5 = QCheckBox("Networking")
        self.cBox6 = QCheckBox("Management")
        
        self.Block4 = QGroupBox("Contact Details")
        
        self.address = QLabel("Address: ")
        self.addressIn = QLineEdit()
        self.email = QLabel("Email: ")
        self.emailIn = QLineEdit()
        self.cNumber = QLabel("Contact Numbers: ")
        self.cNumberHome = QLabel("Home: ")
        self.cNumberHomeIn = QLineEdit()
        self.cNumberMobile = QLabel("Mobile: ")
        self.cNumberMobileIn = QLineEdit()
        
        self.Block5 = QGroupBox("Login Informations")
        self.userName = QLabel("User Name: ")
        self.userNameIn = QLineEdit()
        self.password = QLabel("Password")
        self.passwordIn = QLineEdit()
        self.comPassword = QLabel("Comfirem Password")
        self.comPasswordIn = QLineEdit()
        
        self.btnDelete = QPushButton("Delete")
        self.btnDelete.setObjectName("DeleteC")
        self.btnClear = QPushButton("Clear")
        self.btnClear.setObjectName("ClearC")
        self.btnSelect = QPushButton("Select")
        self.btnSelect.setObjectName("SelectC")
        self.btnUpdate = QPushButton("Update")
        self.btnUpdate.setObjectName("UpdateC")
        self.btnInsert = QPushButton("Insert")
        self.btnInsert.setObjectName("InsertC")
                
    def LayOutCus(self):
            MainBlock = QWidget()
            self.setCentralWidget(MainBlock)
            
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            
            containerWidget = QWidget()
            self.vBox = QVBoxLayout(containerWidget)
            
            topicGrid = QGridLayout()
            topicGrid.addWidget(self.Topic,0,0)
            topicWiget = QWidget()
            topicWiget.setLayout(topicGrid)
            
            personalInfoGrid = QGridLayout()
            personalInfoGrid.addWidget(self.membership,0,0)
            personalInfoGrid.addWidget(self.rBtnMem1,0,1)
            personalInfoGrid.addWidget(self.rBtnMem2,0,2)
            personalInfoGrid.addWidget(self.rBtnMem3,0,3)
            personalInfoGrid.addWidget(self.title,1,0)
            personalInfoGrid.addWidget(self.titleCombo,1,1,1,3)
            personalInfoGrid.addWidget(self.name,2,0)
            personalInfoGrid.addWidget(self.nameIn,2,1,1,3)
            personalInfoGrid.addWidget(self.id,3,0)
            personalInfoGrid.addWidget(self.idIn,3,1,1,3)
            personalInfoGrid.addWidget(self.bOD,4,0)
            personalInfoGrid.addWidget(self.bODIn,4,1,1,3)
            personalInfoGrid.addWidget(self.gender,5,0)
            personalInfoGrid.addWidget(self.genderIn,5,1,1,3)
            personalInfoGrid.addWidget(self.statues,6,0)
            personalInfoGrid.addWidget(self.statuesCombo,6,1,1,3)
            
            self.Block1.setLayout(personalInfoGrid)
            
            self.vBox.addWidget(topicWiget)
            self.vBox.addWidget(self.Block1)
            
            # Block2: Under 18
            under18Layout = QGridLayout()
            under18Layout.addWidget(self.rBtnUnCheck1, 0, 0)
            under18Layout.addWidget(self.rBtnUnCheck2, 0, 1)
            self.Block2.setLayout(under18Layout)
            self.vBox.addWidget(self.Block2)

            # Block3: Courses
            courseLayout = QGridLayout()
            courseLayout.addWidget(self.courses, 0, 0)
            courseLayout.addWidget(self.cBox1, 1, 0)
            courseLayout.addWidget(self.cBox2, 1, 1)
            courseLayout.addWidget(self.cBox3, 2, 0)
            courseLayout.addWidget(self.cBox4, 2, 1)
            courseLayout.addWidget(self.cBox5, 3, 0)
            courseLayout.addWidget(self.cBox6, 3, 1)
            self.Block3.setLayout(courseLayout)
            self.vBox.addWidget(self.Block3)

            # Block4: Contact Details
            contactLayout = QGridLayout()
            contactLayout.addWidget(self.address, 0, 0)
            contactLayout.addWidget(self.addressIn, 0, 1)
            contactLayout.addWidget(self.email, 1, 0)
            contactLayout.addWidget(self.emailIn, 1, 1)
            contactLayout.addWidget(self.cNumber, 2, 0)
            contactLayout.addWidget(self.cNumberHome, 3, 0)
            contactLayout.addWidget(self.cNumberHomeIn, 3, 1)
            contactLayout.addWidget(self.cNumberMobile, 4, 0)
            contactLayout.addWidget(self.cNumberMobileIn, 4, 1)
            self.Block4.setLayout(contactLayout)
            self.vBox.addWidget(self.Block4)
            
            loginLayout = QGridLayout()
            loginLayout.addWidget(self.userName,0,0)
            loginLayout.addWidget(self.userNameIn,0,1)
            loginLayout.addWidget(self.password,1,0)
            loginLayout.addWidget(self.passwordIn,1,1)
            loginLayout.addWidget(self.comPassword,2,0)
            loginLayout.addWidget(self.comPasswordIn,2,1)
            self.Block5.setLayout(loginLayout)
            self.vBox.addWidget(self.Block5)

            btnBlock = QGridLayout()
            btnBlock.addWidget(self.btnDelete,0,0)
            btnBlock.addWidget(self.btnClear,0,1)
            btnBlock.addWidget(self.btnSelect,0,2)
            btnBlock.addWidget(self.btnUpdate,0,3)
            btnBlock.addWidget(self.btnInsert,0,4)
            self.vBox.addLayout(btnBlock)
            
            scroll.setWidget(containerWidget)
            
            mainlayout = QVBoxLayout()
            mainlayout.addWidget(scroll)
            MainBlock.setLayout(mainlayout)
    
    def shadowTopic(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setOffset(2,3)
        shadow.setBlurRadius(5)
        shadow.setColor(QColor("#F0261F"))
        self.Topic.setGraphicsEffect(shadow)
        
    def blockShadow(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(6)
        shadow.setOffset(1, 1)
        shadow.setColor(QColor(0, 0, 0, 40))
        widget.setGraphicsEffect(shadow)
             
    def css(self):
        self.setStyleSheet("""
                           QLabel{
                               font-size:20px;
                               font-family:'Times New Roman';
                               
                           }
                           QLabel#RegistrationC{
                               color:blue;
                               border:3px solid green;
                               border-radius:8px;
                               font-size:30px;
                               font-family:'Ink Free';
                           }
                           QGroupBox{
                               font-size:28px;
                               font-family:'Times New Roman';
                           }
                           QPushButton{
                               color:white;
                               padding:5px;
                               border-radius:8px;
                               cuser:select;
                           }
                           QPushButton#DeleteC{
                               background-color:#ED452B;
                           }
                           QPushButton#ClearC{
                               background-color:#ED792B;
                           }
                           QPushButton#SelectC{
                               background-color:#27E8AB;
                           }
                           QPushButton#UpdateC{
                               background-color:#27ABE8;
                           }
                           QPushButton#InsertC{
                               background-color:#1EDB0D;
                           }
                           """)