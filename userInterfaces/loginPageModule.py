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
        self.widget_3 = QWidget(self.page_5)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 1021, 771))
        self.label_29 = QLabel(self.widget_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(320, 205, 171, 21))
        font3 = QFont()
        font3.setPointSize(20)
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_13 = QFrame(self.widget_3)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(290, 630, 751, 16))
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)
        self.CatLabel5 = QLabel(self.widget_3)
        self.CatLabel5.setObjectName(u"CatLabel5")
        self.CatLabel5.setGeometry(QRect(630, 530, 81, 16))
        self.CatLabel5.setStyleSheet(u"color: rgb(0,0,0);")
        self.AmountLabel1 = QLabel(self.widget_3)
        self.AmountLabel1.setObjectName(u"AmountLabel1")
        self.AmountLabel1.setGeometry(QRect(450, 370, 91, 16))
        self.AmountLabel1.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_39 = QLabel(self.widget_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(570, 205, 171, 21))
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"color: rgb(0,0,0);")
        self.goGoalButton = QPushButton(self.widget_3)
        self.goGoalButton.setObjectName(u"goGoalButton")
        self.goGoalButton.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton.setFont(font3)
        self.goGoalButton.setStyleSheet(u"QPushButton#goGoalButton {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goGoalButton:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}")
        self.label_40 = QLabel(self.widget_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(300, 200, 16, 31))
        self.label_40.setFont(font3)
        self.label_40.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_41 = QLabel(self.widget_3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(540, 176, 221, 61))
        self.label_41.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.goDashboardButton = QPushButton(self.widget_3)
        self.goDashboardButton.setObjectName(u"goDashboardButton")
        self.goDashboardButton.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton.setFont(font3)
        self.goDashboardButton.setStyleSheet(u"QPushButton#goDashboardButton {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goDashboardButton:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"")
        self.DesLabel9 = QLabel(self.widget_3)
        self.DesLabel9.setObjectName(u"DesLabel9")
        self.DesLabel9.setGeometry(QRect(860, 690, 81, 16))
        self.DesLabel9.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_42 = QLabel(self.widget_3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(320, 330, 60, 16))
        font4 = QFont()
        font4.setPointSize(14)
        self.label_42.setFont(font4)
        self.label_42.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_43 = QLabel(self.widget_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(630, 330, 60, 16))
        self.label_43.setFont(font4)
        self.label_43.setStyleSheet(u"color: rgb(148,148,148);")
        self.DesLabel8 = QLabel(self.widget_3)
        self.DesLabel8.setObjectName(u"DesLabel8")
        self.DesLabel8.setGeometry(QRect(860, 650, 81, 16))
        self.DesLabel8.setStyleSheet(u"color: rgb(0,0,0);")
        self.DateLabel5 = QLabel(self.widget_3)
        self.DateLabel5.setObjectName(u"DateLabel5")
        self.DateLabel5.setGeometry(QRect(310, 530, 81, 16))
        self.DateLabel5.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_44 = QLabel(self.widget_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(300, 180, 111, 16))
        font5 = QFont()
        font5.setBold(True)
        self.label_44.setFont(font5)
        self.label_44.setStyleSheet(u"color: rgb(148,148,148);")
        self.DateLabel2 = QLabel(self.widget_3)
        self.DateLabel2.setObjectName(u"DateLabel2")
        self.DateLabel2.setGeometry(QRect(310, 410, 81, 16))
        self.DateLabel2.setStyleSheet(u"color: rgb(0,0,0);")
        self.CatLabel7 = QLabel(self.widget_3)
        self.CatLabel7.setObjectName(u"CatLabel7")
        self.CatLabel7.setGeometry(QRect(630, 610, 81, 16))
        self.CatLabel7.setStyleSheet(u"color: rgb(0,0,0);")
        self.AmountLabel6 = QLabel(self.widget_3)
        self.AmountLabel6.setObjectName(u"AmountLabel6")
        self.AmountLabel6.setGeometry(QRect(450, 570, 91, 16))
        self.AmountLabel6.setStyleSheet(u"color: rgb(0,0,0);")
        self.AmountLabel9 = QLabel(self.widget_3)
        self.AmountLabel9.setObjectName(u"AmountLabel9")
        self.AmountLabel9.setGeometry(QRect(450, 690, 91, 16))
        self.AmountLabel9.setStyleSheet(u"color: rgb(0,0,0);")
        self.DesLabel4 = QLabel(self.widget_3)
        self.DesLabel4.setObjectName(u"DesLabel4")
        self.DesLabel4.setGeometry(QRect(860, 490, 81, 16))
        self.DesLabel4.setStyleSheet(u"color: rgb(0,0,0);")
        self.DateLabel6 = QLabel(self.widget_3)
        self.DateLabel6.setObjectName(u"DateLabel6")
        self.DateLabel6.setGeometry(QRect(310, 570, 81, 16))
        self.DateLabel6.setStyleSheet(u"color: rgb(0,0,0);")
        self.DateLabel1 = QLabel(self.widget_3)
        self.DateLabel1.setObjectName(u"DateLabel1")
        self.DateLabel1.setGeometry(QRect(310, 370, 81, 16))
        self.DateLabel1.setStyleSheet(u"color: rgb(0,0,0);")
        self.CatLabel3 = QLabel(self.widget_3)
        self.CatLabel3.setObjectName(u"CatLabel3")
        self.CatLabel3.setGeometry(QRect(630, 450, 81, 16))
        self.CatLabel3.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_45 = QLabel(self.widget_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(290, 220, 221, 21))
        self.label_45.setStyleSheet(u"background-color: rgb(178,241,149);\n"
"")
        self.label_46 = QLabel(self.widget_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(460, 330, 60, 16))
        self.label_46.setFont(font4)
        self.label_46.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_47 = QLabel(self.widget_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(20, 170, 31, 31))
        self.label_47.setStyleSheet(u"")
        self.label_47.setPixmap(QPixmap(u":/pics/images/user.png"))
        self.label_47.setScaledContents(True)
        self.DateLabel3 = QLabel(self.widget_3)
        self.DateLabel3.setObjectName(u"DateLabel3")
        self.DateLabel3.setGeometry(QRect(310, 450, 81, 16))
        self.DateLabel3.setStyleSheet(u"color: rgb(0,0,0);")
        self.CatLabel8 = QLabel(self.widget_3)
        self.CatLabel8.setObjectName(u"CatLabel8")
        self.CatLabel8.setGeometry(QRect(630, 650, 81, 16))
        self.CatLabel8.setStyleSheet(u"color: rgb(0,0,0);")
        self.CatLabel9 = QLabel(self.widget_3)
        self.CatLabel9.setObjectName(u"CatLabel9")
        self.CatLabel9.setGeometry(QRect(630, 690, 81, 16))
        self.CatLabel9.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_14 = QFrame(self.widget_3)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(290, 750, 751, 16))
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)
        self.label_48 = QLabel(self.widget_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(100, 60, 121, 21))
        self.label_48.setFont(font2)
        self.label_48.setStyleSheet(u"color: white;\n"
"")
        self.AmountLabel2 = QLabel(self.widget_3)
        self.AmountLabel2.setObjectName(u"AmountLabel2")
        self.AmountLabel2.setGeometry(QRect(450, 410, 91, 16))
        self.AmountLabel2.setStyleSheet(u"color: rgb(0,0,0);")
        self.DesLabel6 = QLabel(self.widget_3)
        self.DesLabel6.setObjectName(u"DesLabel6")
        self.DesLabel6.setGeometry(QRect(860, 570, 81, 16))
        self.DesLabel6.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_49 = QLabel(self.widget_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(790, 176, 221, 61))
        self.label_49.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.label_50 = QLabel(self.widget_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(550, 180, 121, 16))
        self.label_50.setFont(font5)
        self.label_50.setStyleSheet(u"color: rgb(148,148,148);")
        self.CatLabel4 = QLabel(self.widget_3)
        self.CatLabel4.setObjectName(u"CatLabel4")
        self.CatLabel4.setGeometry(QRect(630, 490, 81, 16))
        self.CatLabel4.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_15 = QFrame(self.widget_3)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(290, 670, 751, 16))
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)
        self.line_16 = QFrame(self.widget_3)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(290, 590, 751, 16))
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)
        self.label_51 = QLabel(self.widget_3)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(850, 330, 81, 16))
        self.label_51.setFont(font4)
        self.label_51.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_52 = QLabel(self.widget_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(800, 200, 16, 31))
        self.label_52.setFont(font3)
        self.label_52.setStyleSheet(u"color: rgb(0,0,0);")
        self.AmountLabel5 = QLabel(self.widget_3)
        self.AmountLabel5.setObjectName(u"AmountLabel5")
        self.AmountLabel5.setGeometry(QRect(450, 530, 91, 16))
        self.AmountLabel5.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_17 = QFrame(self.widget_3)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setGeometry(QRect(290, 510, 751, 16))
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)
        self.DateLabel4 = QLabel(self.widget_3)
        self.DateLabel4.setObjectName(u"DateLabel4")
        self.DateLabel4.setGeometry(QRect(310, 490, 81, 16))
        self.DateLabel4.setStyleSheet(u"color: rgb(0,0,0);")
        self.DesLabel1 = QLabel(self.widget_3)
        self.DesLabel1.setObjectName(u"DesLabel1")
        self.DesLabel1.setGeometry(QRect(860, 370, 81, 16))
        self.DesLabel1.setStyleSheet(u"color: rgb(0,0,0);")
        self.DateLabel10 = QLabel(self.widget_3)
        self.DateLabel10.setObjectName(u"DateLabel10")
        self.DateLabel10.setGeometry(QRect(310, 730, 81, 16))
        self.DateLabel10.setStyleSheet(u"color: rgb(0,0,0);")
        self.closeButton_3 = QPushButton(self.widget_3)
        self.closeButton_3.setObjectName(u"closeButton_3")
        self.closeButton_3.setGeometry(QRect(970, 30, 31, 31))
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
        self.label_53 = QLabel(self.widget_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(540, 220, 221, 21))
        self.label_53.setStyleSheet(u"background-color: rgb(164,202,247);\n"
"")
        self.line_18 = QFrame(self.widget_3)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setGeometry(QRect(290, 430, 751, 16))
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)
        self.label_54 = QLabel(self.widget_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(800, 180, 111, 16))
        self.label_54.setFont(font5)
        self.label_54.setStyleSheet(u"color: rgb(148,148,148);")
        self.CatLabel6 = QLabel(self.widget_3)
        self.CatLabel6.setObjectName(u"CatLabel6")
        self.CatLabel6.setGeometry(QRect(630, 570, 81, 16))
        self.CatLabel6.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_55 = QLabel(self.widget_3)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(0, 0, 1071, 101))
        self.label_55.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.AmountLabel7 = QLabel(self.widget_3)
        self.AmountLabel7.setObjectName(u"AmountLabel7")
        self.AmountLabel7.setGeometry(QRect(450, 610, 91, 16))
        self.AmountLabel7.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_56 = QLabel(self.widget_3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(300, 120, 241, 21))
        font6 = QFont()
        font6.setPointSize(22)
        self.label_56.setFont(font6)
        self.label_56.setStyleSheet(u"color: rgb(0,0,0);")
        self.DesLabel2 = QLabel(self.widget_3)
        self.DesLabel2.setObjectName(u"DesLabel2")
        self.DesLabel2.setGeometry(QRect(860, 410, 81, 16))
        self.DesLabel2.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_57 = QLabel(self.widget_3)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(790, 220, 221, 21))
        self.label_57.setStyleSheet(u"background-color: rgb(213,131,131);\n"
"")
        self.DateLabel8 = QLabel(self.widget_3)
        self.DateLabel8.setObjectName(u"DateLabel8")
        self.DateLabel8.setGeometry(QRect(310, 650, 81, 16))
        self.DateLabel8.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_58 = QLabel(self.widget_3)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(820, 205, 171, 21))
        self.label_58.setFont(font3)
        self.label_58.setStyleSheet(u"color: rgb(0,0,0);")
        self.CatLabel10 = QLabel(self.widget_3)
        self.CatLabel10.setObjectName(u"CatLabel10")
        self.CatLabel10.setGeometry(QRect(630, 730, 81, 16))
        self.CatLabel10.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_59 = QLabel(self.widget_3)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(550, 200, 16, 31))
        self.label_59.setFont(font3)
        self.label_59.setStyleSheet(u"color: rgb(0,0,0);")
        self.AmountLabel3 = QLabel(self.widget_3)
        self.AmountLabel3.setObjectName(u"AmountLabel3")
        self.AmountLabel3.setGeometry(QRect(450, 450, 91, 16))
        self.AmountLabel3.setStyleSheet(u"color: rgb(0,0,0);")
        self.CatLabel1 = QLabel(self.widget_3)
        self.CatLabel1.setObjectName(u"CatLabel1")
        self.CatLabel1.setGeometry(QRect(630, 370, 81, 16))
        self.CatLabel1.setStyleSheet(u"color: rgb(0,0,0);")
        self.CatLabel2 = QLabel(self.widget_3)
        self.CatLabel2.setObjectName(u"CatLabel2")
        self.CatLabel2.setGeometry(QRect(630, 410, 81, 16))
        self.CatLabel2.setStyleSheet(u"color: rgb(0,0,0);")
        self.goAccountButton = QPushButton(self.widget_3)
        self.goAccountButton.setObjectName(u"goAccountButton")
        self.goAccountButton.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton.setFont(font3)
        self.goAccountButton.setStyleSheet(u"QPushButton#goAccountButton {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goAccountButton:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}")
        self.line_19 = QFrame(self.widget_3)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setGeometry(QRect(290, 350, 751, 16))
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)
        self.DateLabel9 = QLabel(self.widget_3)
        self.DateLabel9.setObjectName(u"DateLabel9")
        self.DateLabel9.setGeometry(QRect(310, 690, 81, 16))
        self.DateLabel9.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_60 = QLabel(self.widget_3)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(0, 100, 1021, 701))
        self.label_60.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_61 = QLabel(self.widget_3)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(20, 290, 31, 31))
        self.label_61.setStyleSheet(u"")
        self.label_61.setPixmap(QPixmap(u":/pics/images/goal.png"))
        self.label_61.setScaledContents(True)
        self.label_62 = QLabel(self.widget_3)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(20, 230, 31, 31))
        self.label_62.setStyleSheet(u"")
        self.label_62.setPixmap(QPixmap(u":/pics/images/trans.png"))
        self.label_62.setScaledContents(True)
        self.tabsButton = QPushButton(self.widget_3)
        self.tabsButton.setObjectName(u"tabsButton")
        self.tabsButton.setGeometry(QRect(50, 50, 41, 41))
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
        self.line_20 = QFrame(self.widget_3)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setGeometry(QRect(290, 550, 751, 16))
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)
        self.AmountLabel10 = QLabel(self.widget_3)
        self.AmountLabel10.setObjectName(u"AmountLabel10")
        self.AmountLabel10.setGeometry(QRect(450, 730, 101, 16))
        self.AmountLabel10.setStyleSheet(u"color: rgb(0,0,0);")
        self.AmountLabel8 = QLabel(self.widget_3)
        self.AmountLabel8.setObjectName(u"AmountLabel8")
        self.AmountLabel8.setGeometry(QRect(450, 650, 91, 16))
        self.AmountLabel8.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_63 = QLabel(self.widget_3)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(0, 100, 251, 701))
        self.label_63.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.DesLabel3 = QLabel(self.widget_3)
        self.DesLabel3.setObjectName(u"DesLabel3")
        self.DesLabel3.setGeometry(QRect(860, 450, 81, 16))
        self.DesLabel3.setStyleSheet(u"color: rgb(0,0,0);")
        self.DesLabel10 = QLabel(self.widget_3)
        self.DesLabel10.setObjectName(u"DesLabel10")
        self.DesLabel10.setGeometry(QRect(860, 730, 81, 16))
        self.DesLabel10.setStyleSheet(u"color: rgb(0,0,0);")
        self.DesLabel7 = QLabel(self.widget_3)
        self.DesLabel7.setObjectName(u"DesLabel7")
        self.DesLabel7.setGeometry(QRect(860, 610, 81, 16))
        self.DesLabel7.setStyleSheet(u"color: rgb(0,0,0);")
        self.DateLabel7 = QLabel(self.widget_3)
        self.DateLabel7.setObjectName(u"DateLabel7")
        self.DateLabel7.setGeometry(QRect(310, 610, 81, 16))
        self.DateLabel7.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_21 = QFrame(self.widget_3)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setGeometry(QRect(290, 470, 751, 16))
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)
        self.goTransButton = QPushButton(self.widget_3)
        self.goTransButton.setObjectName(u"goTransButton")
        self.goTransButton.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton.setFont(font3)
        self.goTransButton.setStyleSheet(u"QPushButton#goTransButton {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goTransButton:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}")
        self.label_64 = QLabel(self.widget_3)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(290, 176, 221, 61))
        self.label_64.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.AmountLabel4 = QLabel(self.widget_3)
        self.AmountLabel4.setObjectName(u"AmountLabel4")
        self.AmountLabel4.setGeometry(QRect(450, 490, 91, 16))
        self.AmountLabel4.setStyleSheet(u"color: rgb(0,0,0);")
        self.DesLabel5 = QLabel(self.widget_3)
        self.DesLabel5.setObjectName(u"DesLabel5")
        self.DesLabel5.setGeometry(QRect(860, 530, 81, 16))
        self.DesLabel5.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_65 = QLabel(self.widget_3)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(290, 270, 201, 21))
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(True)
        self.label_65.setFont(font7)
        self.label_65.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_22 = QFrame(self.widget_3)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setGeometry(QRect(290, 390, 751, 16))
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)
        self.label_66 = QLabel(self.widget_3)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(20, 110, 31, 31))
        self.label_66.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.line_23 = QFrame(self.widget_3)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setGeometry(QRect(290, 710, 751, 16))
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)
        self.bg = QLabel(self.widget_3)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(290, 310, 731, 451))
        self.bg.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.addButton = QPushButton(self.widget_3)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(70, 600, 91, 81))
        self.addButton.setStyleSheet(u"color: rgb(0,0,0);\n"
"border: 5px solid black;")
        self.label_60.raise_()
        self.label_63.raise_()
        self.goDashboardButton.raise_()
        self.bg.raise_()
        self.label_45.raise_()
        self.label_64.raise_()
        self.label_57.raise_()
        self.label_53.raise_()
        self.label_41.raise_()
        self.label_29.raise_()
        self.line_13.raise_()
        self.CatLabel5.raise_()
        self.AmountLabel1.raise_()
        self.label_39.raise_()
        self.label_40.raise_()
        self.DesLabel9.raise_()
        self.label_42.raise_()
        self.label_43.raise_()
        self.DesLabel8.raise_()
        self.DateLabel5.raise_()
        self.label_44.raise_()
        self.DateLabel2.raise_()
        self.CatLabel7.raise_()
        self.AmountLabel6.raise_()
        self.AmountLabel9.raise_()
        self.DesLabel4.raise_()
        self.DateLabel6.raise_()
        self.DateLabel1.raise_()
        self.CatLabel3.raise_()
        self.label_46.raise_()
        self.DateLabel3.raise_()
        self.CatLabel8.raise_()
        self.CatLabel9.raise_()
        self.line_14.raise_()
        self.AmountLabel2.raise_()
        self.DesLabel6.raise_()
        self.label_49.raise_()
        self.label_50.raise_()
        self.CatLabel4.raise_()
        self.line_15.raise_()
        self.line_16.raise_()
        self.label_51.raise_()
        self.label_52.raise_()
        self.AmountLabel5.raise_()
        self.line_17.raise_()
        self.DateLabel4.raise_()
        self.DesLabel1.raise_()
        self.DateLabel10.raise_()
        self.line_18.raise_()
        self.label_54.raise_()
        self.CatLabel6.raise_()
        self.label_55.raise_()
        self.AmountLabel7.raise_()
        self.label_56.raise_()
        self.DesLabel2.raise_()
        self.DateLabel8.raise_()
        self.label_58.raise_()
        self.CatLabel10.raise_()
        self.label_59.raise_()
        self.AmountLabel3.raise_()
        self.CatLabel1.raise_()
        self.CatLabel2.raise_()
        self.line_19.raise_()
        self.DateLabel9.raise_()
        self.tabsButton.raise_()
        self.line_20.raise_()
        self.AmountLabel10.raise_()
        self.AmountLabel8.raise_()
        self.DesLabel3.raise_()
        self.DesLabel10.raise_()
        self.DesLabel7.raise_()
        self.DateLabel7.raise_()
        self.line_21.raise_()
        self.goTransButton.raise_()
        self.AmountLabel4.raise_()
        self.DesLabel5.raise_()
        self.label_65.raise_()
        self.line_22.raise_()
        self.label_66.raise_()
        self.line_23.raise_()
        self.goAccountButton.raise_()
        self.goGoalButton.raise_()
        self.closeButton_3.raise_()
        self.label_47.raise_()
        self.label_62.raise_()
        self.label_61.raise_()
        self.label_48.raise_()
        self.addButton.raise_()
        self.stackedWidget.addWidget(self.page_5)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_2 = QPushButton(self.widget_4)
        self.goGoalButton_2.setObjectName(u"goGoalButton_2")
        self.goGoalButton_2.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_2.setFont(font3)
        self.goGoalButton_2.setStyleSheet(u"QPushButton#goGoalButton_2 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goGoalButton_2:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}")
        self.goDashboardButton_2 = QPushButton(self.widget_4)
        self.goDashboardButton_2.setObjectName(u"goDashboardButton_2")
        self.goDashboardButton_2.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_2.setFont(font3)
        self.goDashboardButton_2.setStyleSheet(u"QPushButton#goDashboardButton_2 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goDashboardButton_2:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"")
        self.label_75 = QLabel(self.widget_4)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(20, 170, 31, 31))
        self.label_75.setStyleSheet(u"")
        self.label_75.setPixmap(QPixmap(u":/pics/images/user.png"))
        self.label_75.setScaledContents(True)
        self.label_76 = QLabel(self.widget_4)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(100, 60, 121, 21))
        self.label_76.setFont(font2)
        self.label_76.setStyleSheet(u"color: white;\n"
"")
        self.closeButton_4 = QPushButton(self.widget_4)
        self.closeButton_4.setObjectName(u"closeButton_4")
        self.closeButton_4.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy.setHeightForWidth(self.closeButton_4.sizePolicy().hasHeightForWidth())
        self.closeButton_4.setSizePolicy(sizePolicy)
        self.closeButton_4.setBaseSize(QSize(0, 0))
        self.closeButton_4.setStyleSheet(u"QPushButton#closeButton_4 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton_4:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        self.closeButton_4.setIcon(icon)
        self.label_83 = QLabel(self.widget_4)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(0, 0, 1071, 101))
        self.label_83.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.goAccountButton_2 = QPushButton(self.widget_4)
        self.goAccountButton_2.setObjectName(u"goAccountButton_2")
        self.goAccountButton_2.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_2.setFont(font3)
        self.goAccountButton_2.setStyleSheet(u"QPushButton#goAccountButton_2 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goAccountButton_2:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}")
        self.label_88 = QLabel(self.widget_4)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(0, 100, 1021, 701))
        self.label_88.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_89 = QLabel(self.widget_4)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(20, 290, 31, 31))
        self.label_89.setStyleSheet(u"")
        self.label_89.setPixmap(QPixmap(u":/pics/images/goal.png"))
        self.label_89.setScaledContents(True)
        self.label_90 = QLabel(self.widget_4)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(20, 230, 31, 31))
        self.label_90.setStyleSheet(u"")
        self.label_90.setPixmap(QPixmap(u":/pics/images/trans.png"))
        self.label_90.setScaledContents(True)
        self.tabsButton_2 = QPushButton(self.widget_4)
        self.tabsButton_2.setObjectName(u"tabsButton_2")
        self.tabsButton_2.setGeometry(QRect(50, 50, 41, 41))
        self.tabsButton_2.setStyleSheet(u"QPushButton#tabsButton_2 {\n"
"    border: none;\n"
"    background-color: rgb(81,74,248);\n"
"   qproperty-iconSize: 40px;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#tabsButton_2:hover {\n"
"    background-color: rgb(81,74,170);\n"
"}\n"
"")
        self.tabsButton_2.setIcon(icon1)
        self.label_91 = QLabel(self.widget_4)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(0, 100, 251, 701))
        self.label_91.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.goTransButton_2 = QPushButton(self.widget_4)
        self.goTransButton_2.setObjectName(u"goTransButton_2")
        self.goTransButton_2.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_2.setFont(font3)
        self.goTransButton_2.setStyleSheet(u"QPushButton#goTransButton_2 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goTransButton_2:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}")
        self.label_94 = QLabel(self.widget_4)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(20, 110, 31, 31))
        self.label_94.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 120, 101, 31))
        self.label_83.raise_()
        self.label_88.raise_()
        self.tabsButton_2.raise_()
        self.label_91.raise_()
        self.goTransButton_2.raise_()
        self.goGoalButton_2.raise_()
        self.goDashboardButton_2.raise_()
        self.goAccountButton_2.raise_()
        self.closeButton_4.raise_()
        self.label_94.raise_()
        self.label_90.raise_()
        self.label_89.raise_()
        self.label_75.raise_()
        self.label_76.raise_()
        self.label_3.raise_()
        self.stackedWidget.addWidget(self.page)

        self.retranslateUi(Form)
        self.closeButton.clicked.connect(Form.close)
        self.closeButton_2.clicked.connect(Form.close)
        self.closeButton_3.clicked.connect(Form.close)
        self.closeButton_4.clicked.connect(Form.close)

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
        self.label_29.setText(QCoreApplication.translate("Form", u"0", None))
        self.CatLabel5.setText(QCoreApplication.translate("Form", u"CatLabel5", None))
        self.AmountLabel1.setText(QCoreApplication.translate("Form", u"AmountLabel1", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"0", None))
        self.goGoalButton.setText(QCoreApplication.translate("Form", u"Goal", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.label_41.setText("")
        self.goDashboardButton.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.DesLabel9.setText(QCoreApplication.translate("Form", u"DesLabel9", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"Date", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"Category", None))
        self.DesLabel8.setText(QCoreApplication.translate("Form", u"DesLabel8", None))
        self.DateLabel5.setText(QCoreApplication.translate("Form", u"DateLabel5", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"Current Balance", None))
        self.DateLabel2.setText(QCoreApplication.translate("Form", u"DateLabel2", None))
        self.CatLabel7.setText(QCoreApplication.translate("Form", u"CatLabel7", None))
        self.AmountLabel6.setText(QCoreApplication.translate("Form", u"AmountLabel6", None))
        self.AmountLabel9.setText(QCoreApplication.translate("Form", u"AmountLabel9", None))
        self.DesLabel4.setText(QCoreApplication.translate("Form", u"DesLabel4", None))
        self.DateLabel6.setText(QCoreApplication.translate("Form", u"DateLabel6", None))
        self.DateLabel1.setText(QCoreApplication.translate("Form", u"DateLabel1", None))
        self.CatLabel3.setText(QCoreApplication.translate("Form", u"CatLabel3", None))
        self.label_45.setText("")
        self.label_46.setText(QCoreApplication.translate("Form", u"Amount", None))
        self.label_47.setText("")
        self.DateLabel3.setText(QCoreApplication.translate("Form", u"DateLabel3", None))
        self.CatLabel8.setText(QCoreApplication.translate("Form", u"CatLabel8", None))
        self.CatLabel9.setText(QCoreApplication.translate("Form", u"CatLabel9", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.AmountLabel2.setText(QCoreApplication.translate("Form", u"AmountLabel2", None))
        self.DesLabel6.setText(QCoreApplication.translate("Form", u"DesLabel6", None))
        self.label_49.setText("")
        self.label_50.setText(QCoreApplication.translate("Form", u"Available Balance", None))
        self.CatLabel4.setText(QCoreApplication.translate("Form", u"CatLabel4", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"Description", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.AmountLabel5.setText(QCoreApplication.translate("Form", u"AmountLabel5", None))
        self.DateLabel4.setText(QCoreApplication.translate("Form", u"DateLabel4", None))
        self.DesLabel1.setText(QCoreApplication.translate("Form", u"DesLabel1", None))
        self.DateLabel10.setText(QCoreApplication.translate("Form", u"DateLabel10", None))
        self.closeButton_3.setText("")
        self.label_53.setText("")
        self.label_54.setText(QCoreApplication.translate("Form", u"Spent This Week", None))
        self.CatLabel6.setText(QCoreApplication.translate("Form", u"CatLabel6", None))
        self.label_55.setText("")
        self.AmountLabel7.setText(QCoreApplication.translate("Form", u"AmountLabel7", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"\u2190 User Account", None))
        self.DesLabel2.setText(QCoreApplication.translate("Form", u"DesLabel2", None))
        self.label_57.setText("")
        self.DateLabel8.setText(QCoreApplication.translate("Form", u"DateLabel8", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"0", None))
        self.CatLabel10.setText(QCoreApplication.translate("Form", u"CatLabel10", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.AmountLabel3.setText(QCoreApplication.translate("Form", u"AmountLabel3", None))
        self.CatLabel1.setText(QCoreApplication.translate("Form", u"CatLabel1", None))
        self.CatLabel2.setText(QCoreApplication.translate("Form", u"CatLabel2", None))
        self.goAccountButton.setText(QCoreApplication.translate("Form", u"Account", None))
        self.DateLabel9.setText(QCoreApplication.translate("Form", u"DateLabel9", None))
        self.label_60.setText("")
        self.label_61.setText("")
        self.label_62.setText("")
        self.tabsButton.setText("")
        self.AmountLabel10.setText(QCoreApplication.translate("Form", u"AmountLabel10", None))
        self.AmountLabel8.setText(QCoreApplication.translate("Form", u"AmountLabel8", None))
        self.label_63.setText("")
        self.DesLabel3.setText(QCoreApplication.translate("Form", u"DesLabel3", None))
        self.DesLabel10.setText(QCoreApplication.translate("Form", u"DesLabel10", None))
        self.DesLabel7.setText(QCoreApplication.translate("Form", u"DesLabel7", None))
        self.DateLabel7.setText(QCoreApplication.translate("Form", u"DateLabel7", None))
        self.goTransButton.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_64.setText("")
        self.AmountLabel4.setText(QCoreApplication.translate("Form", u"AmountLabel4", None))
        self.DesLabel5.setText(QCoreApplication.translate("Form", u"DesLabel5", None))
        self.label_65.setText(QCoreApplication.translate("Form", u"Account Transaction:", None))
        self.label_66.setText("")
        self.bg.setText("")
        self.addButton.setText(QCoreApplication.translate("Form", u"add +", None))
        self.goGoalButton_2.setText(QCoreApplication.translate("Form", u"Goal", None))
        self.goDashboardButton_2.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_75.setText("")
        self.label_76.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.closeButton_4.setText("")
        self.label_83.setText("")
        self.goAccountButton_2.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_88.setText("")
        self.label_89.setText("")
        self.label_90.setText("")
        self.tabsButton_2.setText("")
        self.label_91.setText("")
        self.goTransButton_2.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_94.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"New Transaction", None))
    # retranslateUi

