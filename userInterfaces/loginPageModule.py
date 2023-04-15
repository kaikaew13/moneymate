# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginPage.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import img_rc
import sys
import os

####
script_dir = os.path.dirname(os.path.abspath(__file__))
moneymate_dir = os.path.abspath(os.path.join(script_dir, ".."))
sys.path.insert(0, moneymate_dir)
from User import User
# import คนละ folder ยากชิบหาย



class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 768)
        Form.setWindowFlags(Qt.FramelessWindowHint) # Remove the window frame
        Form.setAttribute(Qt.WA_TranslucentBackground) # Set the background to transparent
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 961, 731))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 541, 561))
        self.label.setStyleSheet(u"background-image: url(:/pics/images/Summary.png);\n"
"border-top-left-radius: 50px;")
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(540, 80, 411, 561))
        self.label_2.setStyleSheet(u"background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(670, 130, 131, 51))
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgba(0,0,0,150);\n"
"")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(600, 250, 311, 51))
        font1 = QFont()
        font1.setPointSize(18)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,100);\n"
"padding-bottom:7px;")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 440, 311, 71))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,160), stop:1 rgba(85,98,112,160));\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,200), stop:1 rgba(85,98,112,200));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,120), stop:1 rgba(85,98,112,120));\n"
"}\n"
"")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(600, 530, 311, 71))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"QPushButton#pushButton_2 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,120), stop:1 rgba(85,98,112,120));\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,160), stop:1 rgba(85,98,112,160));\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,80), stop:1 rgba(85,98,112,80));\n"
"}\n"
"")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 120, 521, 81))
        self.label_4.setStyleSheet(u"background-color: rgba(0,0,0,75);")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 130, 241, 61))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: white;\n"
"")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(600, 350, 311, 51))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,100);\n"
"padding-bottom:7px;")
        self.closeButton = QPushButton(self.widget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(910, 90, 31, 32))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setBaseSize(QSize(0, 0))
        self.closeButton.setStyleSheet(u"QPushButton#closeButton\n"
" {\n"
"    border: none;\n"
"}")
        def on_signin_clicked():
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()
            if username == "" or password == "":
                self.label_5.setText("Please fill all the fields")
            else:
                user = User(username, password) # actually this have be done in the register page
                try:
                    pass # check if user exists in database then login
                except Exception as e:
                    print(e)

        icon = QIcon()
        icon.addFile(u":/pics/images/x-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon)

        self.retranslateUi(Form)
        self.closeButton.clicked.connect(Form.close)
        self.pushButton.clicked.connect(on_signin_clicked)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Sign In", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"S i g n  I n", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"R e g i s t er", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.closeButton.setText("")
    # retranslateUi


        

