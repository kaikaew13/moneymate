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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)
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
        self.label_5.setGeometry(QRect(30, 130, 501, 61))
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
        self.label_10.setGeometry(QRect(30, 130, 501, 61))
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
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_3 = QLabel(self.page_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-30, -30, 1071, 101))
        self.label_3.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 30, 121, 21))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: white;\n"
"")
        self.tabsButton = QPushButton(self.page_5)
        self.tabsButton.setObjectName(u"tabsButton")
        self.tabsButton.setGeometry(QRect(20, 20, 41, 41))
        self.tabsButton.setStyleSheet(u"QPushButton#tabsButton {\n"
"    border: none;\n"
"    background-color: rgb(81,74,248);\n"
"   qproperty-iconSize: 40px;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#tabsButton:hover {\n"
"    background-color: rgb(81,74,170);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/pics/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabsButton.setIcon(icon1)
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 70, 1021, 701))
        self.label_11.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_12 = QLabel(self.page_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 80, 241, 691))
        self.label_12.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.label_13 = QLabel(self.page_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(260, 146, 221, 61))
        self.label_13.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.label_14 = QLabel(self.page_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(510, 146, 221, 61))
        self.label_14.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.label_15 = QLabel(self.page_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(760, 146, 221, 61))
        self.label_15.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.label_16 = QLabel(self.page_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(260, 190, 221, 21))
        self.label_16.setStyleSheet(u"background-color: rgb(178,241,149);\n"
"")
        self.label_17 = QLabel(self.page_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(510, 190, 221, 21))
        self.label_17.setStyleSheet(u"background-color: rgb(164,202,247);\n"
"")
        self.label_18 = QLabel(self.page_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(760, 190, 221, 21))
        self.label_18.setStyleSheet(u"background-color: rgb(213,131,131);\n"
"")
        self.label_19 = QLabel(self.page_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(270, 150, 111, 16))
        font3 = QFont()
        font3.setBold(True)
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_20 = QLabel(self.page_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(520, 150, 121, 16))
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_21 = QLabel(self.page_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(770, 150, 111, 16))
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_22 = QLabel(self.page_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(270, 170, 16, 31))
        font4 = QFont()
        font4.setPointSize(20)
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_23 = QLabel(self.page_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(520, 170, 16, 31))
        self.label_23.setFont(font4)
        self.label_23.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_24 = QLabel(self.page_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(770, 170, 16, 31))
        self.label_24.setFont(font4)
        self.label_24.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_25 = QLabel(self.page_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(290, 175, 171, 21))
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_26 = QLabel(self.page_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(540, 175, 171, 21))
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_27 = QLabel(self.page_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(790, 175, 171, 21))
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_28 = QLabel(self.page_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(260, 240, 201, 21))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        self.label_28.setFont(font5)
        self.label_28.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_29 = QLabel(self.page_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(260, 270, 751, 501))
        self.label_29.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.line = QFrame(self.page_5)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(260, 310, 751, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_30 = QLabel(self.page_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(270, 90, 241, 21))
        font6 = QFont()
        font6.setPointSize(22)
        self.label_30.setFont(font6)
        self.label_30.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_31 = QLabel(self.page_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(50, 90, 101, 21))
        font7 = QFont()
        font7.setPointSize(20)
        font7.setBold(False)
        self.label_31.setFont(font7)
        self.label_31.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_32 = QLabel(self.page_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(50, 140, 101, 21))
        self.label_32.setFont(font4)
        self.label_32.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_33 = QLabel(self.page_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(50, 190, 131, 21))
        self.label_33.setFont(font4)
        self.label_33.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_34 = QLabel(self.page_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(50, 240, 61, 21))
        self.label_34.setFont(font4)
        self.label_34.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_35 = QLabel(self.page_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 80, 31, 31))
        self.label_35.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.closeButton_3 = QPushButton(self.page_5)
        self.closeButton_3.setObjectName(u"closeButton_3")
        self.closeButton_3.setGeometry(QRect(980, 10, 31, 32))
        sizePolicy.setHeightForWidth(self.closeButton_3.sizePolicy().hasHeightForWidth())
        self.closeButton_3.setSizePolicy(sizePolicy)
        self.closeButton_3.setBaseSize(QSize(0, 0))
        self.closeButton_3.setStyleSheet(u"QPushButton#closeButton_3 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton_3:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        self.closeButton_3.setIcon(icon)
        self.stackedWidget.addWidget(self.page_5)
        self.label_12.raise_()
        self.label_11.raise_()
        self.label_3.raise_()
        self.label_8.raise_()
        self.label_16.raise_()
        self.label_13.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.line.raise_()
        self.label_30.raise_()
        self.label_35.raise_()
        self.closeButton_3.raise_()
        self.label_32.raise_()
        self.label_31.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        self.tabsButton.raise_()

        self.retranslateUi(Form)
        self.closeButton.clicked.connect(Form.close)
        self.closeButton_2.clicked.connect(Form.close)
        self.closeButton_3.clicked.connect(Form.close)

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
        self.label_3.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.tabsButton.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("Form", u"Current Balance", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Available Balance", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Spent This Week", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Account Transaction:", None))
        self.label_29.setText("")
        self.label_30.setText(QCoreApplication.translate("Form", u"\u2190 User Account", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Accounts", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.label_35.setText("")
        self.closeButton_3.setText("")
    # retranslateUi

