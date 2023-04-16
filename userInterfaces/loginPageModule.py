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
    QSizePolicy, QStackedWidget, QWidget)
import img_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 768)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1021, 771))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 961, 731))
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
        self.Signin_Label = QLabel(self.widget)
        self.Signin_Label.setObjectName(u"Signin_Label")
        self.Signin_Label.setGeometry(QRect(670, 130, 131, 51))
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.Signin_Label.setFont(font)
        self.Signin_Label.setStyleSheet(u"color:rgba(0,0,0,150);\n"
"")
        self.lineEditUserLogin = QLineEdit(self.widget)
        self.lineEditUserLogin.setObjectName(u"lineEditUserLogin")
        self.lineEditUserLogin.setGeometry(QRect(600, 250, 311, 51))
        font1 = QFont()
        font1.setPointSize(18)
        self.lineEditUserLogin.setFont(font1)
        self.lineEditUserLogin.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,100);\n"
"padding-bottom:7px;")
        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(600, 440, 311, 71))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.loginButton.setFont(font2)
        self.loginButton.setStyleSheet(u"QPushButton#loginButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,160), stop:1 rgba(85,98,112,160));\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#loginButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,200), stop:1 rgba(85,98,112,200));\n"
"}\n"
"\n"
"QPushButton#loginButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,120), stop:1 rgba(85,98,112,120));\n"
"}\n"
"")
        self.GoRegisterButton = QPushButton(self.widget)
        self.GoRegisterButton.setObjectName(u"GoRegisterButton")
        self.GoRegisterButton.setGeometry(QRect(600, 530, 311, 71))
        self.GoRegisterButton.setFont(font2)
        self.GoRegisterButton.setStyleSheet(u"QPushButton#GoRegisterButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,120), stop:1 rgba(85,98,112,120));\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#GoRegisterButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,160), stop:1 rgba(85,98,112,160));\n"
"}\n"
"\n"
"QPushButton#GoRegisterButton:pressed {\n"
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
        self.lineEditPassLogin = QLineEdit(self.widget)
        self.lineEditPassLogin.setObjectName(u"lineEditPassLogin")
        self.lineEditPassLogin.setGeometry(QRect(600, 350, 311, 51))
        self.lineEditPassLogin.setFont(font1)
        self.lineEditPassLogin.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,100);\n"
"padding-bottom:7px;")
        self.lineEditPassLogin.setEchoMode(QLineEdit.Password)
        self.closeButton = QPushButton(self.widget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(910, 90, 31, 32))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setBaseSize(QSize(0, 0))
        self.closeButton.setStyleSheet(u"QPushButton#closeButton {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/pics/images/x-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.widget_2 = QWidget(self.page_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(30, 30, 961, 731))
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 80, 541, 561))
        self.label_6.setStyleSheet(u"background-image: url(:/pics/images/Summary.png);\n"
"border-top-left-radius: 50px;")
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(540, 80, 411, 561))
        self.label_7.setStyleSheet(u"background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius: 50px;")
        self.Reigstration_Label = QLabel(self.widget_2)
        self.Reigstration_Label.setObjectName(u"Reigstration_Label")
        self.Reigstration_Label.setGeometry(QRect(630, 130, 241, 51))
        self.Reigstration_Label.setFont(font)
        self.Reigstration_Label.setStyleSheet(u"color:rgba(0,0,0,150);\n"
"")
        self.lineEditUserRegister = QLineEdit(self.widget_2)
        self.lineEditUserRegister.setObjectName(u"lineEditUserRegister")
        self.lineEditUserRegister.setGeometry(QRect(600, 210, 311, 51))
        self.lineEditUserRegister.setFont(font1)
        self.lineEditUserRegister.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,100);\n"
"padding-bottom:7px;")
        self.RegisterButton = QPushButton(self.widget_2)
        self.RegisterButton.setObjectName(u"RegisterButton")
        self.RegisterButton.setGeometry(QRect(600, 450, 311, 71))
        self.RegisterButton.setFont(font2)
        self.RegisterButton.setStyleSheet(u"QPushButton#RegisterButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,160), stop:1 rgba(85,98,112,160));\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#RegisterButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,200), stop:1 rgba(85,98,112,200));\n"
"}\n"
"\n"
"QPushButton#RegisterButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,120), stop:1 rgba(85,98,112,120));\n"
"}\n"
"")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 120, 521, 81))
        self.label_9.setStyleSheet(u"background-color: rgba(0,0,0,75);")
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 130, 241, 61))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: white;\n"
"")
        self.lineEditUserPassword = QLineEdit(self.widget_2)
        self.lineEditUserPassword.setObjectName(u"lineEditUserPassword")
        self.lineEditUserPassword.setGeometry(QRect(600, 300, 311, 51))
        self.lineEditUserPassword.setFont(font1)
        self.lineEditUserPassword.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,100);\n"
"padding-bottom:7px;")
        self.lineEditUserPassword.setEchoMode(QLineEdit.Password)
        self.closeButton_2 = QPushButton(self.widget_2)
        self.closeButton_2.setObjectName(u"closeButton_2")
        self.closeButton_2.setGeometry(QRect(910, 90, 31, 32))
        sizePolicy.setHeightForWidth(self.closeButton_2.sizePolicy().hasHeightForWidth())
        self.closeButton_2.setSizePolicy(sizePolicy)
        self.closeButton_2.setBaseSize(QSize(0, 0))
        self.closeButton_2.setStyleSheet(u"QPushButton#closeButton_2 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton_2:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        self.closeButton_2.setIcon(icon)
        self.lineEditUserPassword_2 = QLineEdit(self.widget_2)
        self.lineEditUserPassword_2.setObjectName(u"lineEditUserPassword_2")
        self.lineEditUserPassword_2.setGeometry(QRect(600, 370, 311, 51))
        self.lineEditUserPassword_2.setFont(font1)
        self.lineEditUserPassword_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,100);\n"
"padding-bottom:7px;")
        self.lineEditUserPassword_2.setEchoMode(QLineEdit.Password)
        self.goSigninButton = QPushButton(self.widget_2)
        self.goSigninButton.setObjectName(u"goSigninButton")
        self.goSigninButton.setGeometry(QRect(600, 540, 311, 71))
        self.goSigninButton.setFont(font2)
        self.goSigninButton.setStyleSheet(u"QPushButton#goSigninButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,120), stop:1 rgba(85,98,112,120));\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#goSigninButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,160), stop:1 rgba(85,98,112,160));\n"
"}\n"
"\n"
"QPushButton#goSigninButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,80), stop:1 rgba(85,98,112,80));\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_4)

        self.retranslateUi(Form)
        self.closeButton.clicked.connect(Form.close)
        self.closeButton_2.clicked.connect(Form.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.Signin_Label.setText(QCoreApplication.translate("Form", u"Sign In", None))
        self.lineEditUserLogin.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.loginButton.setText(QCoreApplication.translate("Form", u"S i g n  I n", None))
        self.GoRegisterButton.setText(QCoreApplication.translate("Form", u"G o  R e g i s t er", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.lineEditPassLogin.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.closeButton.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.Reigstration_Label.setText(QCoreApplication.translate("Form", u"Registration", None))
        self.lineEditUserRegister.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.RegisterButton.setText(QCoreApplication.translate("Form", u"R e g i s t er", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.lineEditUserPassword.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.closeButton_2.setText("")
        self.lineEditUserPassword_2.setPlaceholderText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.goSigninButton.setText(QCoreApplication.translate("Form", u"B a c k  to  S i g n I n", None))
    # retranslateUi

