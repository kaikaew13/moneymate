# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDateTimeEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import img_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1021, 771))
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.widget = QWidget(self.loginPage)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy1)
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
        self.stackedWidget.addWidget(self.loginPage)
        self.registerPage = QWidget()
        self.registerPage.setObjectName(u"registerPage")
        self.widget_2 = QWidget(self.registerPage)
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
        sizePolicy1.setHeightForWidth(self.closeButton_2.sizePolicy().hasHeightForWidth())
        self.closeButton_2.setSizePolicy(sizePolicy1)
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
        self.stackedWidget.addWidget(self.registerPage)
        self.dashboardPage = QWidget()
        self.dashboardPage.setObjectName(u"dashboardPage")
        self.widget_3 = QWidget(self.dashboardPage)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 1021, 771))
        self.currentBalanceLabel = QLabel(self.widget_3)
        self.currentBalanceLabel.setObjectName(u"currentBalanceLabel")
        self.currentBalanceLabel.setGeometry(QRect(320, 205, 171, 21))
        font3 = QFont()
        font3.setPointSize(20)
        self.currentBalanceLabel.setFont(font3)
        self.currentBalanceLabel.setStyleSheet(u"color: rgb(0,0,0);")
        self.budgetLabel = QLabel(self.widget_3)
        self.budgetLabel.setObjectName(u"budgetLabel")
        self.budgetLabel.setGeometry(QRect(570, 205, 171, 21))
        self.budgetLabel.setFont(font3)
        self.budgetLabel.setStyleSheet(u"color: rgb(0,0,0);")
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
"}\n"
"QPushButton#goGoalButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
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
"\n"
"QPushButton#goDashboardButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_44 = QLabel(self.widget_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(300, 180, 111, 16))
        font4 = QFont()
        font4.setBold(True)
        self.label_44.setFont(font4)
        self.label_44.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_45 = QLabel(self.widget_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(290, 220, 221, 21))
        self.label_45.setStyleSheet(u"background-color: rgb(178,241,149);\n"
"")
        self.label_47 = QLabel(self.widget_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(20, 170, 31, 31))
        self.label_47.setStyleSheet(u"")
        self.label_47.setPixmap(QPixmap(u":/pics/images/user.png"))
        self.label_47.setScaledContents(True)
        self.label_48 = QLabel(self.widget_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(100, 60, 121, 21))
        self.label_48.setFont(font2)
        self.label_48.setStyleSheet(u"color: white;\n"
"")
        self.label_49 = QLabel(self.widget_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(790, 176, 221, 61))
        self.label_49.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.label_50 = QLabel(self.widget_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(550, 180, 121, 16))
        self.label_50.setFont(font4)
        self.label_50.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_52 = QLabel(self.widget_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(800, 200, 16, 31))
        self.label_52.setFont(font3)
        self.label_52.setStyleSheet(u"color: rgb(0,0,0);")
        self.closeButton_3 = QPushButton(self.widget_3)
        self.closeButton_3.setObjectName(u"closeButton_3")
        self.closeButton_3.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(self.closeButton_3.sizePolicy().hasHeightForWidth())
        self.closeButton_3.setSizePolicy(sizePolicy1)
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
        self.label_54 = QLabel(self.widget_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(800, 180, 111, 16))
        self.label_54.setFont(font4)
        self.label_54.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_55 = QLabel(self.widget_3)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(0, 0, 1071, 101))
        self.label_55.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.label_56 = QLabel(self.widget_3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(290, 120, 241, 21))
        font5 = QFont()
        font5.setPointSize(22)
        self.label_56.setFont(font5)
        self.label_56.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_57 = QLabel(self.widget_3)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(790, 220, 221, 21))
        self.label_57.setStyleSheet(u"background-color: rgb(213,131,131);\n"
"")
        self.spentLabel = QLabel(self.widget_3)
        self.spentLabel.setObjectName(u"spentLabel")
        self.spentLabel.setGeometry(QRect(820, 205, 171, 21))
        self.spentLabel.setFont(font3)
        self.spentLabel.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_59 = QLabel(self.widget_3)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(550, 200, 16, 31))
        self.label_59.setFont(font3)
        self.label_59.setStyleSheet(u"color: rgb(0,0,0);")
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
"}\n"
"QPushButton#goAccountButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
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
        self.label_63 = QLabel(self.widget_3)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(0, 100, 251, 701))
        self.label_63.setStyleSheet(u"background-color: rgb(255,255,255);")
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
"}\n"
"QPushButton#goTransButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_64 = QLabel(self.widget_3)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(290, 176, 221, 61))
        self.label_64.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.label_65 = QLabel(self.widget_3)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(290, 260, 201, 21))
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(True)
        self.label_65.setFont(font6)
        self.label_65.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_66 = QLabel(self.widget_3)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(20, 110, 31, 31))
        self.label_66.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.addButton = QPushButton(self.widget_3)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(10, 680, 231, 61))
        font7 = QFont()
        font7.setPointSize(18)
        font7.setBold(True)
        self.addButton.setFont(font7)
        self.addButton.setStyleSheet(u"QPushButton#addButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#addButton:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#addButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.widget_13 = QWidget(self.widget_3)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(290, 290, 721, 41))
        self.widget_13.setStyleSheet(u"background-color: white;")
        self.label_24 = QLabel(self.widget_13)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 10, 111, 16))
        self.label_25 = QLabel(self.widget_13)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(480, 10, 111, 16))
        self.label_26 = QLabel(self.widget_13)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(230, 10, 131, 16))
        self.line_7 = QFrame(self.widget_13)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(-10, 30, 721, 21))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.widget_13)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(-10, 40, 741, 20))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.scrollArea_2 = QScrollArea(self.widget_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(290, 330, 721, 181))
        self.scrollArea_2.setStyleSheet(u"background-color: rgb(240,240,240)")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 719, 179))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.label_69 = QLabel(self.widget_3)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(290, 530, 201, 21))
        self.label_69.setFont(font6)
        self.label_69.setStyleSheet(u"color: rgb(0,0,0);")
        self.horizontalLayoutWidget = QWidget(self.widget_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(290, 560, 721, 181))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_108 = QLabel(self.widget_3)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(0, 70, 1021, 701))
        self.label_108.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.goBillsButton = QPushButton(self.widget_3)
        self.goBillsButton.setObjectName(u"goBillsButton")
        self.goBillsButton.setGeometry(QRect(-10, 340, 261, 61))
        self.goBillsButton.setFont(font3)
        self.goBillsButton.setStyleSheet(u"QPushButton#goBillsButton {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goBillsButton:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.notiButton = QPushButton(self.widget_3)
        self.notiButton.setObjectName(u"notiButton")
        self.notiButton.setGeometry(QRect(-10, 400, 261, 61))
        self.notiButton.setFont(font3)
        self.notiButton.setStyleSheet(u"QPushButton#notiButton {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_29 = QLabel(self.widget_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 350, 41, 41))
        self.label_29.setPixmap(QPixmap(u":/pics/images/Vzt78rEMgwJJdAAAAABJRU5ErkJggg==.png"))
        self.bellicon = QLabel(self.widget_3)
        self.bellicon.setObjectName(u"bellicon")
        self.bellicon.setGeometry(QRect(20, 410, 41, 41))
        self.bellicon.setPixmap(QPixmap(u":/pics/images/k1DgxNmG74K3Ehe5GBarWemJDbD6cZYezwDPqoDrKR6n9dLZP+TlCbMGG3akiX8bAAAAAElFTkSuQmCC.png"))
        self.label_108.raise_()
        self.label_63.raise_()
        self.goDashboardButton.raise_()
        self.label_45.raise_()
        self.label_64.raise_()
        self.label_57.raise_()
        self.label_53.raise_()
        self.label_41.raise_()
        self.currentBalanceLabel.raise_()
        self.budgetLabel.raise_()
        self.label_40.raise_()
        self.label_44.raise_()
        self.label_49.raise_()
        self.label_50.raise_()
        self.label_52.raise_()
        self.label_54.raise_()
        self.label_55.raise_()
        self.label_56.raise_()
        self.spentLabel.raise_()
        self.label_59.raise_()
        self.goTransButton.raise_()
        self.label_65.raise_()
        self.label_66.raise_()
        self.goAccountButton.raise_()
        self.goGoalButton.raise_()
        self.closeButton_3.raise_()
        self.label_47.raise_()
        self.label_62.raise_()
        self.label_61.raise_()
        self.label_48.raise_()
        self.addButton.raise_()
        self.widget_13.raise_()
        self.scrollArea_2.raise_()
        self.label_69.raise_()
        self.horizontalLayoutWidget.raise_()
        self.goBillsButton.raise_()
        self.notiButton.raise_()
        self.label_29.raise_()
        self.bellicon.raise_()
        self.stackedWidget.addWidget(self.dashboardPage)
        self.addPage = QWidget()
        self.addPage.setObjectName(u"addPage")
        self.widget_4 = QWidget(self.addPage)
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
"}\n"
"QPushButton#goGoalButton_2:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
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
" \n"
"   background-color: rgb(81,74,200);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_2:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
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
        sizePolicy1.setHeightForWidth(self.closeButton_4.sizePolicy().hasHeightForWidth())
        self.closeButton_4.setSizePolicy(sizePolicy1)
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
"}\n"
"QPushButton#goAccountButton_2:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
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
"}\n"
"QPushButton#goTransButton_2:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_94 = QLabel(self.widget_4)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(20, 110, 31, 31))
        self.label_94.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 120, 151, 31))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(0,0,0);")
        self.line = QFrame(self.widget_4)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(270, 150, 731, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.transnameLineEdit = QLineEdit(self.widget_4)
        self.transnameLineEdit.setObjectName(u"transnameLineEdit")
        self.transnameLineEdit.setGeometry(QRect(270, 200, 241, 31))
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(270, 170, 151, 31))
        font8 = QFont()
        font8.setPointSize(16)
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet(u"color: rgb(0,0,0);")
        self.catLineEdit = QLineEdit(self.widget_4)
        self.catLineEdit.setObjectName(u"catLineEdit")
        self.catLineEdit.setGeometry(QRect(270, 270, 241, 31))
        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(270, 240, 151, 31))
        self.label_11.setFont(font8)
        self.label_11.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(560, 170, 151, 31))
        self.label_12.setFont(font8)
        self.label_12.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_13 = QLabel(self.widget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(270, 460, 151, 31))
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_2 = QFrame(self.widget_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(260, 490, 731, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.goalnameLineEdit = QLineEdit(self.widget_4)
        self.goalnameLineEdit.setObjectName(u"goalnameLineEdit")
        self.goalnameLineEdit.setGeometry(QRect(270, 540, 241, 31))
        self.goalamountLineEdit = QLineEdit(self.widget_4)
        self.goalamountLineEdit.setObjectName(u"goalamountLineEdit")
        self.goalamountLineEdit.setGeometry(QRect(270, 620, 241, 31))
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(270, 510, 151, 31))
        self.label_14.setFont(font8)
        self.label_14.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(270, 590, 151, 31))
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(560, 500, 151, 31))
        self.label_16.setFont(font8)
        self.label_16.setStyleSheet(u"color: rgb(0,0,0);")
        self.income_radio = QRadioButton(self.widget_4)
        self.income_radio.setObjectName(u"income_radio")
        self.income_radio.setGeometry(QRect(290, 380, 100, 20))
        self.income_radio.setStyleSheet(u"color: rgb(0,0,0);")
        self.expense_radio = QRadioButton(self.widget_4)
        self.expense_radio.setObjectName(u"expense_radio")
        self.expense_radio.setGeometry(QRect(410, 380, 100, 20))
        self.expense_radio.setStyleSheet(u"color: rgb(0,0,0);")
        self.saveTransButton = QPushButton(self.widget_4)
        self.saveTransButton.setObjectName(u"saveTransButton")
        self.saveTransButton.setGeometry(QRect(270, 420, 113, 32))
        self.saveGoalButton = QPushButton(self.widget_4)
        self.saveGoalButton.setObjectName(u"saveGoalButton")
        self.saveGoalButton.setGeometry(QRect(270, 680, 113, 32))
        self.transamountLineEdit = QLineEdit(self.widget_4)
        self.transamountLineEdit.setObjectName(u"transamountLineEdit")
        self.transamountLineEdit.setGeometry(QRect(270, 340, 241, 31))
        self.label_17 = QLabel(self.widget_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(270, 310, 151, 31))
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet(u"color: rgb(0,0,0);")
        self.transDesc = QTextEdit(self.widget_4)
        self.transDesc.setObjectName(u"transDesc")
        self.transDesc.setGeometry(QRect(560, 200, 431, 31))
        self.GoalDesc = QTextEdit(self.widget_4)
        self.GoalDesc.setObjectName(u"GoalDesc")
        self.GoalDesc.setGeometry(QRect(560, 540, 431, 211))
        self.goBillsButton_2 = QPushButton(self.widget_4)
        self.goBillsButton_2.setObjectName(u"goBillsButton_2")
        self.goBillsButton_2.setGeometry(QRect(-10, 340, 261, 61))
        self.goBillsButton_2.setFont(font3)
        self.goBillsButton_2.setStyleSheet(u"QPushButton#goBillsButton_2 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goBillsButton_2:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_2:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.notiButton_2 = QPushButton(self.widget_4)
        self.notiButton_2.setObjectName(u"notiButton_2")
        self.notiButton_2.setGeometry(QRect(-10, 400, 261, 61))
        self.notiButton_2.setFont(font3)
        self.notiButton_2.setStyleSheet(u"QPushButton#notiButton_2 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_2:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_2:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_30 = QLabel(self.widget_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(20, 350, 41, 41))
        self.label_30.setPixmap(QPixmap(u":/pics/images/Vzt78rEMgwJJdAAAAABJRU5ErkJggg==.png"))
        self.bellicon_2 = QLabel(self.widget_4)
        self.bellicon_2.setObjectName(u"bellicon_2")
        self.bellicon_2.setGeometry(QRect(20, 410, 41, 41))
        self.bellicon_2.setPixmap(QPixmap(u":/pics/images/k1DgxNmG74K3Ehe5GBarWemJDbD6cZYezwDPqoDrKR6n9dLZP+TlCbMGG3akiX8bAAAAAElFTkSuQmCC.png"))
        self.dateTimeEdit = QDateTimeEdit(self.widget_4)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(560, 270, 451, 41))
        self.label_142 = QLabel(self.widget_4)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setGeometry(QRect(560, 240, 111, 16))
        self.label_83.raise_()
        self.label_88.raise_()
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
        self.line.raise_()
        self.transnameLineEdit.raise_()
        self.label_8.raise_()
        self.catLineEdit.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.line_2.raise_()
        self.goalnameLineEdit.raise_()
        self.goalamountLineEdit.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.income_radio.raise_()
        self.expense_radio.raise_()
        self.saveTransButton.raise_()
        self.saveGoalButton.raise_()
        self.transamountLineEdit.raise_()
        self.label_17.raise_()
        self.transDesc.raise_()
        self.GoalDesc.raise_()
        self.goBillsButton_2.raise_()
        self.notiButton_2.raise_()
        self.label_30.raise_()
        self.bellicon_2.raise_()
        self.dateTimeEdit.raise_()
        self.label_142.raise_()
        self.stackedWidget.addWidget(self.addPage)
        self.BillsPage = QWidget()
        self.BillsPage.setObjectName(u"BillsPage")
        self.widget_6 = QWidget(self.BillsPage)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_12 = QPushButton(self.widget_6)
        self.goGoalButton_12.setObjectName(u"goGoalButton_12")
        self.goGoalButton_12.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_12.setFont(font3)
        self.goGoalButton_12.setStyleSheet(u"QPushButton#goGoalButton_12 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goGoalButton_12:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goGoalButton_12:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.goDashboardButton_12 = QPushButton(self.widget_6)
        self.goDashboardButton_12.setObjectName(u"goDashboardButton_12")
        self.goDashboardButton_12.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_12.setFont(font3)
        self.goDashboardButton_12.setStyleSheet(u"QPushButton#goDashboardButton_12 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goDashboardButton_12:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_12:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_184 = QLabel(self.widget_6)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setGeometry(QRect(20, 170, 31, 31))
        self.label_184.setStyleSheet(u"")
        self.label_184.setPixmap(QPixmap(u":/pics/images/user.png"))
        self.label_184.setScaledContents(True)
        self.label_185 = QLabel(self.widget_6)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setGeometry(QRect(100, 60, 121, 21))
        self.label_185.setFont(font2)
        self.label_185.setStyleSheet(u"color: white;\n"
"")
        self.closeButton_14 = QPushButton(self.widget_6)
        self.closeButton_14.setObjectName(u"closeButton_14")
        self.closeButton_14.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(self.closeButton_14.sizePolicy().hasHeightForWidth())
        self.closeButton_14.setSizePolicy(sizePolicy1)
        self.closeButton_14.setBaseSize(QSize(0, 0))
        self.closeButton_14.setStyleSheet(u"QPushButton#closeButton_14 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton_14:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        self.closeButton_14.setIcon(icon)
        self.label_186 = QLabel(self.widget_6)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setGeometry(QRect(0, 0, 1071, 101))
        self.label_186.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.goAccountButton_12 = QPushButton(self.widget_6)
        self.goAccountButton_12.setObjectName(u"goAccountButton_12")
        self.goAccountButton_12.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_12.setFont(font3)
        self.goAccountButton_12.setStyleSheet(u"QPushButton#goAccountButton_12 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goAccountButton_12:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goAccountButton_12:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_187 = QLabel(self.widget_6)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setGeometry(QRect(0, 100, 1021, 701))
        self.label_187.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_188 = QLabel(self.widget_6)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setGeometry(QRect(20, 290, 31, 31))
        self.label_188.setStyleSheet(u"")
        self.label_188.setPixmap(QPixmap(u":/pics/images/goal.png"))
        self.label_188.setScaledContents(True)
        self.label_189 = QLabel(self.widget_6)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setGeometry(QRect(20, 230, 31, 31))
        self.label_189.setStyleSheet(u"")
        self.label_189.setPixmap(QPixmap(u":/pics/images/trans.png"))
        self.label_189.setScaledContents(True)
        self.label_190 = QLabel(self.widget_6)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setGeometry(QRect(0, 100, 251, 701))
        self.label_190.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.goTransButton_12 = QPushButton(self.widget_6)
        self.goTransButton_12.setObjectName(u"goTransButton_12")
        self.goTransButton_12.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_12.setFont(font3)
        self.goTransButton_12.setStyleSheet(u"QPushButton#goTransButton_12 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goTransButton_12:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goTransButton_12:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_191 = QLabel(self.widget_6)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setGeometry(QRect(20, 110, 31, 31))
        self.label_191.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.label_192 = QLabel(self.widget_6)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setGeometry(QRect(270, 120, 151, 31))
        self.label_192.setFont(font3)
        self.label_192.setStyleSheet(u"color: rgb(0,0,0);")
        self.scrollArea_8 = QScrollArea(self.widget_6)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setGeometry(QRect(290, 220, 701, 511))
        self.scrollArea_8.setStyleSheet(u"background-color: rgb(240,240,240)")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 699, 509))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_9)
        self.widget_22 = QWidget(self.widget_6)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setGeometry(QRect(290, 180, 701, 41))
        self.widget_22.setStyleSheet(u"background-color: white;")
        self.label_193 = QLabel(self.widget_22)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(20, 10, 111, 16))
        self.label_194 = QLabel(self.widget_22)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(460, 10, 111, 16))
        self.label_195 = QLabel(self.widget_22)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(230, 10, 131, 16))
        self.line_26 = QFrame(self.widget_22)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setGeometry(QRect(-10, 30, 721, 21))
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)
        self.line_27 = QFrame(self.widget_22)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setGeometry(QRect(-10, 40, 741, 20))
        self.line_27.setFrameShape(QFrame.HLine)
        self.line_27.setFrameShadow(QFrame.Sunken)
        self.label_196 = QLabel(self.widget_6)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setGeometry(QRect(290, 180, 701, 41))
        self.label_196.setStyleSheet(u"background-color: rgb(240,240,240)")
        self.addButton_11 = QPushButton(self.widget_6)
        self.addButton_11.setObjectName(u"addButton_11")
        self.addButton_11.setGeometry(QRect(10, 680, 231, 61))
        self.addButton_11.setFont(font7)
        self.addButton_11.setStyleSheet(u"QPushButton#addButton_11{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#addButton_11:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#addButton_11:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.goBillsButton_12 = QPushButton(self.widget_6)
        self.goBillsButton_12.setObjectName(u"goBillsButton_12")
        self.goBillsButton_12.setGeometry(QRect(-10, 340, 261, 61))
        self.goBillsButton_12.setFont(font3)
        self.goBillsButton_12.setStyleSheet(u"QPushButton#goBillsButton_12 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goBillsButton_12:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_12:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.line_28 = QFrame(self.widget_6)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setGeometry(QRect(270, 150, 731, 16))
        self.line_28.setFrameShape(QFrame.HLine)
        self.line_28.setFrameShadow(QFrame.Sunken)
        self.addBillsButton = QPushButton(self.widget_6)
        self.addBillsButton.setObjectName(u"addBillsButton")
        self.addBillsButton.setGeometry(QRect(10, 610, 231, 61))
        self.addBillsButton.setFont(font7)
        self.addBillsButton.setStyleSheet(u"QPushButton#addBillsButton{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#addBillsButton:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#addBillsButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.notiButton_3 = QPushButton(self.widget_6)
        self.notiButton_3.setObjectName(u"notiButton_3")
        self.notiButton_3.setGeometry(QRect(-10, 400, 261, 61))
        self.notiButton_3.setFont(font3)
        self.notiButton_3.setStyleSheet(u"QPushButton#notiButton_3 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);	color: rgb(255,255,255);\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_3:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_3:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_31 = QLabel(self.widget_6)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 350, 41, 41))
        self.label_31.setPixmap(QPixmap(u":/pics/images/Vzt78rEMgwJJdAAAAABJRU5ErkJggg==.png"))
        self.bellicon_3 = QLabel(self.widget_6)
        self.bellicon_3.setObjectName(u"bellicon_3")
        self.bellicon_3.setGeometry(QRect(20, 410, 41, 41))
        self.bellicon_3.setPixmap(QPixmap(u":/pics/images/k1DgxNmG74K3Ehe5GBarWemJDbD6cZYezwDPqoDrKR6n9dLZP+TlCbMGG3akiX8bAAAAAElFTkSuQmCC.png"))
        self.label_186.raise_()
        self.label_187.raise_()
        self.label_192.raise_()
        self.scrollArea_8.raise_()
        self.line_28.raise_()
        self.label_185.raise_()
        self.label_196.raise_()
        self.widget_22.raise_()
        self.label_190.raise_()
        self.addBillsButton.raise_()
        self.addButton_11.raise_()
        self.closeButton_14.raise_()
        self.goAccountButton_12.raise_()
        self.goBillsButton_12.raise_()
        self.goDashboardButton_12.raise_()
        self.goGoalButton_12.raise_()
        self.goTransButton_12.raise_()
        self.label_184.raise_()
        self.label_188.raise_()
        self.label_189.raise_()
        self.label_191.raise_()
        self.notiButton_3.raise_()
        self.label_31.raise_()
        self.bellicon_3.raise_()
        self.stackedWidget.addWidget(self.BillsPage)
        self.TransactionPage = QWidget()
        self.TransactionPage.setObjectName(u"TransactionPage")
        self.widget_5 = QWidget(self.TransactionPage)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_3 = QPushButton(self.widget_5)
        self.goGoalButton_3.setObjectName(u"goGoalButton_3")
        self.goGoalButton_3.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_3.setFont(font3)
        self.goGoalButton_3.setStyleSheet(u"QPushButton#goGoalButton_3 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goGoalButton_3:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goGoalButton_3:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.goDashboardButton_3 = QPushButton(self.widget_5)
        self.goDashboardButton_3.setObjectName(u"goDashboardButton_3")
        self.goDashboardButton_3.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_3.setFont(font3)
        self.goDashboardButton_3.setStyleSheet(u"QPushButton#goDashboardButton_3 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goDashboardButton_3:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_3:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_77 = QLabel(self.widget_5)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(20, 170, 31, 31))
        self.label_77.setStyleSheet(u"")
        self.label_77.setPixmap(QPixmap(u":/pics/images/user.png"))
        self.label_77.setScaledContents(True)
        self.label_78 = QLabel(self.widget_5)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(100, 60, 121, 21))
        self.label_78.setFont(font2)
        self.label_78.setStyleSheet(u"color: white;\n"
"")
        self.closeButton_5 = QPushButton(self.widget_5)
        self.closeButton_5.setObjectName(u"closeButton_5")
        self.closeButton_5.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(self.closeButton_5.sizePolicy().hasHeightForWidth())
        self.closeButton_5.setSizePolicy(sizePolicy1)
        self.closeButton_5.setBaseSize(QSize(0, 0))
        self.closeButton_5.setStyleSheet(u"QPushButton#closeButton_5 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton_5:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        self.closeButton_5.setIcon(icon)
        self.label_84 = QLabel(self.widget_5)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(0, 0, 1071, 101))
        self.label_84.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.goAccountButton_3 = QPushButton(self.widget_5)
        self.goAccountButton_3.setObjectName(u"goAccountButton_3")
        self.goAccountButton_3.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_3.setFont(font3)
        self.goAccountButton_3.setStyleSheet(u"QPushButton#goAccountButton_3 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goAccountButton_3:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goAccountButton_3:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_92 = QLabel(self.widget_5)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(0, 100, 1021, 701))
        self.label_92.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_93 = QLabel(self.widget_5)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(20, 290, 31, 31))
        self.label_93.setStyleSheet(u"")
        self.label_93.setPixmap(QPixmap(u":/pics/images/goal.png"))
        self.label_93.setScaledContents(True)
        self.label_95 = QLabel(self.widget_5)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(20, 230, 31, 31))
        self.label_95.setStyleSheet(u"")
        self.label_95.setPixmap(QPixmap(u":/pics/images/trans.png"))
        self.label_95.setScaledContents(True)
        self.label_96 = QLabel(self.widget_5)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(0, 100, 251, 701))
        self.label_96.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.goTransButton_3 = QPushButton(self.widget_5)
        self.goTransButton_3.setObjectName(u"goTransButton_3")
        self.goTransButton_3.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_3.setFont(font3)
        self.goTransButton_3.setStyleSheet(u"QPushButton#goTransButton_3 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goTransButton_3:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goTransButton_3:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_97 = QLabel(self.widget_5)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(20, 110, 31, 31))
        self.label_97.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.label_18 = QLabel(self.widget_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(270, 120, 151, 31))
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"color: rgb(0,0,0);")
        self.scrollArea = QScrollArea(self.widget_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(290, 220, 701, 511))
        self.scrollArea.setStyleSheet(u"background-color: rgb(240,240,240)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 699, 509))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(290, 180, 701, 41))
        self.widget_7.setStyleSheet(u"background-color: white;")
        self.label_19 = QLabel(self.widget_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 10, 111, 16))
        self.label_20 = QLabel(self.widget_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(460, 10, 111, 16))
        self.label_21 = QLabel(self.widget_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(230, 10, 131, 16))
        self.line_6 = QFrame(self.widget_7)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(-10, 30, 721, 21))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.widget_7)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(-10, 40, 741, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_22 = QLabel(self.widget_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(290, 180, 701, 41))
        self.label_22.setStyleSheet(u"background-color: rgb(240,240,240)")
        self.addButton_2 = QPushButton(self.widget_5)
        self.addButton_2.setObjectName(u"addButton_2")
        self.addButton_2.setGeometry(QRect(10, 680, 231, 61))
        self.addButton_2.setFont(font7)
        self.addButton_2.setStyleSheet(u"QPushButton#addButton_2{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#addButton_2:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#addButton_2:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.goBillsButton_3 = QPushButton(self.widget_5)
        self.goBillsButton_3.setObjectName(u"goBillsButton_3")
        self.goBillsButton_3.setGeometry(QRect(-10, 340, 261, 61))
        self.goBillsButton_3.setFont(font3)
        self.goBillsButton_3.setStyleSheet(u"QPushButton#goBillsButton_3 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goBillsButton_3:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_3:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.line_9 = QFrame(self.widget_5)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(270, 150, 731, 16))
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.notiButton_4 = QPushButton(self.widget_5)
        self.notiButton_4.setObjectName(u"notiButton_4")
        self.notiButton_4.setGeometry(QRect(-10, 400, 261, 61))
        self.notiButton_4.setFont(font3)
        self.notiButton_4.setStyleSheet(u"QPushButton#notiButton_4 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);	color: rgb(255,255,255);\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_4:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_4:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_32 = QLabel(self.widget_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(20, 350, 41, 41))
        self.label_32.setPixmap(QPixmap(u":/pics/images/Vzt78rEMgwJJdAAAAABJRU5ErkJggg==.png"))
        self.bellicon_4 = QLabel(self.widget_5)
        self.bellicon_4.setObjectName(u"bellicon_4")
        self.bellicon_4.setGeometry(QRect(20, 410, 41, 41))
        self.bellicon_4.setPixmap(QPixmap(u":/pics/images/k1DgxNmG74K3Ehe5GBarWemJDbD6cZYezwDPqoDrKR6n9dLZP+TlCbMGG3akiX8bAAAAAElFTkSuQmCC.png"))
        self.label_92.raise_()
        self.label_22.raise_()
        self.label_96.raise_()
        self.label_84.raise_()
        self.goTransButton_3.raise_()
        self.label_18.raise_()
        self.closeButton_5.raise_()
        self.goAccountButton_3.raise_()
        self.goDashboardButton_3.raise_()
        self.goGoalButton_3.raise_()
        self.label_77.raise_()
        self.label_78.raise_()
        self.label_93.raise_()
        self.label_95.raise_()
        self.label_97.raise_()
        self.scrollArea.raise_()
        self.widget_7.raise_()
        self.addButton_2.raise_()
        self.goBillsButton_3.raise_()
        self.line_9.raise_()
        self.notiButton_4.raise_()
        self.label_32.raise_()
        self.bellicon_4.raise_()
        self.stackedWidget.addWidget(self.TransactionPage)
        self.goalPage = QWidget()
        self.goalPage.setObjectName(u"goalPage")
        self.widget_8 = QWidget(self.goalPage)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_4 = QPushButton(self.widget_8)
        self.goGoalButton_4.setObjectName(u"goGoalButton_4")
        self.goGoalButton_4.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_4.setFont(font3)
        self.goGoalButton_4.setStyleSheet(u"QPushButton#goGoalButton_4 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goGoalButton_4:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goGoalButton_4:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.goDashboardButton_4 = QPushButton(self.widget_8)
        self.goDashboardButton_4.setObjectName(u"goDashboardButton_4")
        self.goDashboardButton_4.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_4.setFont(font3)
        self.goDashboardButton_4.setStyleSheet(u"QPushButton#goDashboardButton_4 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goDashboardButton_4:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_4:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_79 = QLabel(self.widget_8)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(20, 170, 31, 31))
        self.label_79.setStyleSheet(u"")
        self.label_79.setPixmap(QPixmap(u":/pics/images/user.png"))
        self.label_79.setScaledContents(True)
        self.label_80 = QLabel(self.widget_8)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(100, 60, 121, 21))
        self.label_80.setFont(font2)
        self.label_80.setStyleSheet(u"color: white;\n"
"")
        self.closeButton_6 = QPushButton(self.widget_8)
        self.closeButton_6.setObjectName(u"closeButton_6")
        self.closeButton_6.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(self.closeButton_6.sizePolicy().hasHeightForWidth())
        self.closeButton_6.setSizePolicy(sizePolicy1)
        self.closeButton_6.setBaseSize(QSize(0, 0))
        self.closeButton_6.setStyleSheet(u"QPushButton#closeButton_6 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton_6:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        self.closeButton_6.setIcon(icon)
        self.label_85 = QLabel(self.widget_8)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(0, 0, 1071, 101))
        self.label_85.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.goAccountButton_4 = QPushButton(self.widget_8)
        self.goAccountButton_4.setObjectName(u"goAccountButton_4")
        self.goAccountButton_4.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_4.setFont(font3)
        self.goAccountButton_4.setStyleSheet(u"QPushButton#goAccountButton_4 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goAccountButton_4:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goAccountButton_4:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_98 = QLabel(self.widget_8)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(0, 100, 1021, 701))
        self.label_98.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_99 = QLabel(self.widget_8)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(20, 290, 31, 31))
        self.label_99.setStyleSheet(u"")
        self.label_99.setPixmap(QPixmap(u":/pics/images/goal.png"))
        self.label_99.setScaledContents(True)
        self.label_100 = QLabel(self.widget_8)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(20, 230, 31, 31))
        self.label_100.setStyleSheet(u"")
        self.label_100.setPixmap(QPixmap(u":/pics/images/trans.png"))
        self.label_100.setScaledContents(True)
        self.label_101 = QLabel(self.widget_8)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(0, 100, 251, 701))
        self.label_101.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.goTransButton_4 = QPushButton(self.widget_8)
        self.goTransButton_4.setObjectName(u"goTransButton_4")
        self.goTransButton_4.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_4.setFont(font3)
        self.goTransButton_4.setStyleSheet(u"QPushButton#goTransButton_4 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goTransButton_4:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goTransButton_4:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_102 = QLabel(self.widget_8)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(20, 110, 31, 31))
        self.label_102.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.label_23 = QLabel(self.widget_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(270, 120, 151, 31))
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_4 = QFrame(self.widget_8)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(270, 150, 731, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(70, 410, 151, 31))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy2)
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(290, 180, 701, 41))
        self.widget_10.setStyleSheet(u"background-color: white;")
        self.label_33 = QLabel(self.widget_10)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(20, 10, 111, 16))
        self.label_34 = QLabel(self.widget_10)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(460, 10, 111, 16))
        self.label_35 = QLabel(self.widget_10)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(230, 10, 131, 16))
        self.line_11 = QFrame(self.widget_10)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(-20, 30, 721, 21))
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.line_12 = QFrame(self.widget_10)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(-10, 40, 741, 20))
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)
        self.scrollArea_3 = QScrollArea(self.widget_8)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(290, 220, 701, 511))
        self.scrollArea_3.setStyleSheet(u"background-color: rgb(240,240,240)")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 699, 509))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)
        self.addButton_3 = QPushButton(self.widget_8)
        self.addButton_3.setObjectName(u"addButton_3")
        self.addButton_3.setGeometry(QRect(10, 680, 231, 61))
        self.addButton_3.setFont(font7)
        self.addButton_3.setStyleSheet(u"QPushButton#addButton_3{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#addButton_3:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#addButton_3:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.goBillsButton_4 = QPushButton(self.widget_8)
        self.goBillsButton_4.setObjectName(u"goBillsButton_4")
        self.goBillsButton_4.setGeometry(QRect(-10, 340, 261, 61))
        self.goBillsButton_4.setFont(font3)
        self.goBillsButton_4.setStyleSheet(u"QPushButton#goBillsButton_4 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goBillsButton_4:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_4:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.notiButton_5 = QPushButton(self.widget_8)
        self.notiButton_5.setObjectName(u"notiButton_5")
        self.notiButton_5.setGeometry(QRect(-10, 400, 261, 61))
        self.notiButton_5.setFont(font3)
        self.notiButton_5.setStyleSheet(u"QPushButton#notiButton_5 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);	color: rgb(255,255,255);\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_5:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_5:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_136 = QLabel(self.widget_8)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(20, 350, 41, 41))
        self.label_136.setPixmap(QPixmap(u":/pics/images/Vzt78rEMgwJJdAAAAABJRU5ErkJggg==.png"))
        self.bellicon_5 = QLabel(self.widget_8)
        self.bellicon_5.setObjectName(u"bellicon_5")
        self.bellicon_5.setGeometry(QRect(20, 410, 41, 41))
        self.bellicon_5.setPixmap(QPixmap(u":/pics/images/k1DgxNmG74K3Ehe5GBarWemJDbD6cZYezwDPqoDrKR6n9dLZP+TlCbMGG3akiX8bAAAAAElFTkSuQmCC.png"))
        self.label_85.raise_()
        self.label_98.raise_()
        self.label_23.raise_()
        self.line_4.raise_()
        self.label_80.raise_()
        self.widget_9.raise_()
        self.closeButton_6.raise_()
        self.label_101.raise_()
        self.goAccountButton_4.raise_()
        self.goDashboardButton_4.raise_()
        self.goGoalButton_4.raise_()
        self.goTransButton_4.raise_()
        self.label_100.raise_()
        self.label_102.raise_()
        self.label_79.raise_()
        self.label_99.raise_()
        self.widget_10.raise_()
        self.scrollArea_3.raise_()
        self.addButton_3.raise_()
        self.goBillsButton_4.raise_()
        self.notiButton_5.raise_()
        self.label_136.raise_()
        self.bellicon_5.raise_()
        self.stackedWidget.addWidget(self.goalPage)
        self.accountPage = QWidget()
        self.accountPage.setObjectName(u"accountPage")
        self.widget_11 = QWidget(self.accountPage)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_5 = QPushButton(self.widget_11)
        self.goGoalButton_5.setObjectName(u"goGoalButton_5")
        self.goGoalButton_5.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_5.setFont(font3)
        self.goGoalButton_5.setStyleSheet(u"QPushButton#goGoalButton_5 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goGoalButton_5:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goGoalButton_5:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.goDashboardButton_5 = QPushButton(self.widget_11)
        self.goDashboardButton_5.setObjectName(u"goDashboardButton_5")
        self.goDashboardButton_5.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_5.setFont(font3)
        self.goDashboardButton_5.setStyleSheet(u"QPushButton#goDashboardButton_5 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_5:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_5:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_81 = QLabel(self.widget_11)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(20, 170, 31, 31))
        self.label_81.setStyleSheet(u"")
        self.label_81.setPixmap(QPixmap(u":/pics/images/user.png"))
        self.label_81.setScaledContents(True)
        self.label_82 = QLabel(self.widget_11)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(100, 60, 121, 21))
        self.label_82.setFont(font2)
        self.label_82.setStyleSheet(u"color: white;\n"
"")
        self.closeButton_7 = QPushButton(self.widget_11)
        self.closeButton_7.setObjectName(u"closeButton_7")
        self.closeButton_7.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(self.closeButton_7.sizePolicy().hasHeightForWidth())
        self.closeButton_7.setSizePolicy(sizePolicy1)
        self.closeButton_7.setBaseSize(QSize(0, 0))
        self.closeButton_7.setStyleSheet(u"QPushButton#closeButton_7 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton_7:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        self.closeButton_7.setIcon(icon)
        self.label_86 = QLabel(self.widget_11)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(0, 0, 1071, 101))
        self.label_86.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.goAccountButton_5 = QPushButton(self.widget_11)
        self.goAccountButton_5.setObjectName(u"goAccountButton_5")
        self.goAccountButton_5.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_5.setFont(font3)
        self.goAccountButton_5.setStyleSheet(u"QPushButton#goAccountButton_5 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goAccountButton_5:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goAccountButton_5:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_103 = QLabel(self.widget_11)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(0, 100, 1021, 701))
        self.label_103.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_104 = QLabel(self.widget_11)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(20, 290, 31, 31))
        self.label_104.setStyleSheet(u"")
        self.label_104.setPixmap(QPixmap(u":/pics/images/goal.png"))
        self.label_104.setScaledContents(True)
        self.label_105 = QLabel(self.widget_11)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setGeometry(QRect(20, 230, 31, 31))
        self.label_105.setStyleSheet(u"")
        self.label_105.setPixmap(QPixmap(u":/pics/images/trans.png"))
        self.label_105.setScaledContents(True)
        self.label_106 = QLabel(self.widget_11)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setGeometry(QRect(0, 100, 251, 701))
        self.label_106.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.goTransButton_5 = QPushButton(self.widget_11)
        self.goTransButton_5.setObjectName(u"goTransButton_5")
        self.goTransButton_5.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_5.setFont(font3)
        self.goTransButton_5.setStyleSheet(u"QPushButton#goTransButton_5 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goTransButton_5:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goTransButton_5:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_107 = QLabel(self.widget_11)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setGeometry(QRect(20, 110, 31, 31))
        self.label_107.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.label_28 = QLabel(self.widget_11)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(270, 120, 151, 31))
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_5 = QFrame(self.widget_11)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(270, 150, 731, 16))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(70, 410, 151, 31))
        sizePolicy2.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy2)
        self.logoutButton = QPushButton(self.widget_11)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(370, 340, 131, 21))
        self.logoutButton.setStyleSheet(u"QPushButton#logoutButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#logoutButton:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#logoutButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.username_account_field = QLineEdit(self.widget_11)
        self.username_account_field.setObjectName(u"username_account_field")
        self.username_account_field.setEnabled(True)
        self.username_account_field.setGeometry(QRect(370, 190, 161, 21))
        self.username_account_field.setReadOnly(True)
        self.label_36 = QLabel(self.widget_11)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(270, 190, 91, 16))
        self.addButton_4 = QPushButton(self.widget_11)
        self.addButton_4.setObjectName(u"addButton_4")
        self.addButton_4.setGeometry(QRect(10, 680, 231, 61))
        self.addButton_4.setFont(font7)
        self.addButton_4.setStyleSheet(u"QPushButton#addButton_4{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#addButton_4:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#addButton_4:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.bugetField = QLineEdit(self.widget_11)
        self.bugetField.setObjectName(u"bugetField")
        self.bugetField.setEnabled(True)
        self.bugetField.setGeometry(QRect(370, 220, 161, 21))
        self.bugetField.setReadOnly(True)
        self.label_42 = QLabel(self.widget_11)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(270, 220, 91, 16))
        self.editBudgetButton = QPushButton(self.widget_11)
        self.editBudgetButton.setObjectName(u"editBudgetButton")
        self.editBudgetButton.setGeometry(QRect(550, 220, 111, 21))
        self.editBudgetButton.setStyleSheet(u"QPushButton#editBudgetButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#editBudgetButton:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#editBudgetButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_134 = QLabel(self.widget_11)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setGeometry(QRect(270, 250, 91, 16))
        self.ttincome = QLineEdit(self.widget_11)
        self.ttincome.setObjectName(u"ttincome")
        self.ttincome.setEnabled(True)
        self.ttincome.setGeometry(QRect(370, 250, 161, 21))
        self.ttincome.setReadOnly(True)
        self.label_135 = QLabel(self.widget_11)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setGeometry(QRect(270, 280, 91, 16))
        self.ttexpense = QLineEdit(self.widget_11)
        self.ttexpense.setObjectName(u"ttexpense")
        self.ttexpense.setEnabled(True)
        self.ttexpense.setGeometry(QRect(370, 280, 161, 21))
        self.ttexpense.setReadOnly(True)
        self.goBillsButton_5 = QPushButton(self.widget_11)
        self.goBillsButton_5.setObjectName(u"goBillsButton_5")
        self.goBillsButton_5.setEnabled(True)
        self.goBillsButton_5.setGeometry(QRect(-10, 340, 261, 61))
        self.goBillsButton_5.setFont(font3)
        self.goBillsButton_5.setStyleSheet(u"QPushButton#goBillsButton_5 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goBillsButton_5:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_5:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.ttBalance = QLineEdit(self.widget_11)
        self.ttBalance.setObjectName(u"ttBalance")
        self.ttBalance.setEnabled(True)
        self.ttBalance.setGeometry(QRect(370, 310, 161, 21))
        self.ttBalance.setReadOnly(True)
        self.label_255 = QLabel(self.widget_11)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setGeometry(QRect(270, 310, 91, 16))
        self.notiButton_6 = QPushButton(self.widget_11)
        self.notiButton_6.setObjectName(u"notiButton_6")
        self.notiButton_6.setGeometry(QRect(-10, 400, 261, 61))
        self.notiButton_6.setFont(font3)
        self.notiButton_6.setStyleSheet(u"QPushButton#notiButton_6 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);	color: rgb(255,255,255);\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_6:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_6:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_137 = QLabel(self.widget_11)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setGeometry(QRect(20, 350, 41, 41))
        self.label_137.setPixmap(QPixmap(u":/pics/images/Vzt78rEMgwJJdAAAAABJRU5ErkJggg==.png"))
        self.bellicon_6 = QLabel(self.widget_11)
        self.bellicon_6.setObjectName(u"bellicon_6")
        self.bellicon_6.setGeometry(QRect(20, 410, 41, 41))
        self.bellicon_6.setPixmap(QPixmap(u":/pics/images/k1DgxNmG74K3Ehe5GBarWemJDbD6cZYezwDPqoDrKR6n9dLZP+TlCbMGG3akiX8bAAAAAElFTkSuQmCC.png"))
        self.widget_12.raise_()
        self.label_86.raise_()
        self.label_103.raise_()
        self.label_28.raise_()
        self.line_5.raise_()
        self.label_82.raise_()
        self.label_106.raise_()
        self.goGoalButton_5.raise_()
        self.goDashboardButton_5.raise_()
        self.goAccountButton_5.raise_()
        self.closeButton_7.raise_()
        self.goTransButton_5.raise_()
        self.label_104.raise_()
        self.label_105.raise_()
        self.label_107.raise_()
        self.label_81.raise_()
        self.logoutButton.raise_()
        self.username_account_field.raise_()
        self.label_36.raise_()
        self.addButton_4.raise_()
        self.bugetField.raise_()
        self.label_42.raise_()
        self.editBudgetButton.raise_()
        self.label_134.raise_()
        self.ttincome.raise_()
        self.label_135.raise_()
        self.ttexpense.raise_()
        self.goBillsButton_5.raise_()
        self.ttBalance.raise_()
        self.label_255.raise_()
        self.notiButton_6.raise_()
        self.label_137.raise_()
        self.bellicon_6.raise_()
        self.stackedWidget.addWidget(self.accountPage)
        self.transactionDetailPage = QWidget()
        self.transactionDetailPage.setObjectName(u"transactionDetailPage")
        self.widget_15 = QWidget(self.transactionDetailPage)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_7 = QPushButton(self.widget_15)
        self.goGoalButton_7.setObjectName(u"goGoalButton_7")
        self.goGoalButton_7.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_7.setFont(font3)
        self.goGoalButton_7.setStyleSheet(u"QPushButton#goGoalButton_7 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goGoalButton_7:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goGoalButton_7:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.goDashboardButton_7 = QPushButton(self.widget_15)
        self.goDashboardButton_7.setObjectName(u"goDashboardButton_7")
        self.goDashboardButton_7.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_7.setFont(font3)
        self.goDashboardButton_7.setStyleSheet(u"QPushButton#goDashboardButton_7 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_7:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_7:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_115 = QLabel(self.widget_15)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(20, 170, 31, 31))
        self.label_115.setStyleSheet(u"")
        self.label_115.setPixmap(QPixmap(u":/pics/images/user.png"))
        self.label_115.setScaledContents(True)
        self.label_116 = QLabel(self.widget_15)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(100, 60, 121, 21))
        self.label_116.setFont(font2)
        self.label_116.setStyleSheet(u"color: white;\n"
"")
        self.closeButton_9 = QPushButton(self.widget_15)
        self.closeButton_9.setObjectName(u"closeButton_9")
        self.closeButton_9.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(self.closeButton_9.sizePolicy().hasHeightForWidth())
        self.closeButton_9.setSizePolicy(sizePolicy1)
        self.closeButton_9.setBaseSize(QSize(0, 0))
        self.closeButton_9.setStyleSheet(u"QPushButton#closeButton_9 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton_9:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        self.closeButton_9.setIcon(icon)
        self.label_117 = QLabel(self.widget_15)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(0, 0, 1071, 101))
        self.label_117.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.goAccountButton_7 = QPushButton(self.widget_15)
        self.goAccountButton_7.setObjectName(u"goAccountButton_7")
        self.goAccountButton_7.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_7.setFont(font3)
        self.goAccountButton_7.setStyleSheet(u"QPushButton#goAccountButton_7 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goAccountButton_7:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goAccountButton_7:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_118 = QLabel(self.widget_15)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(0, 100, 1021, 701))
        self.label_118.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_119 = QLabel(self.widget_15)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(20, 290, 31, 31))
        self.label_119.setStyleSheet(u"")
        self.label_119.setPixmap(QPixmap(u":/pics/images/goal.png"))
        self.label_119.setScaledContents(True)
        self.label_120 = QLabel(self.widget_15)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(20, 230, 31, 31))
        self.label_120.setStyleSheet(u"")
        self.label_120.setPixmap(QPixmap(u":/pics/images/trans.png"))
        self.label_120.setScaledContents(True)
        self.label_121 = QLabel(self.widget_15)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(0, 100, 251, 711))
        self.label_121.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.goTransButton_7 = QPushButton(self.widget_15)
        self.goTransButton_7.setObjectName(u"goTransButton_7")
        self.goTransButton_7.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_7.setFont(font3)
        self.goTransButton_7.setStyleSheet(u"QPushButton#goTransButton_7 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goTransButton_7:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goTransButton_7:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_122 = QLabel(self.widget_15)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(20, 110, 31, 31))
        self.label_122.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.label_37 = QLabel(self.widget_15)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(270, 120, 161, 31))
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_24 = QFrame(self.widget_15)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setGeometry(QRect(270, 150, 731, 16))
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)
        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setGeometry(QRect(70, 410, 151, 31))
        sizePolicy2.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy2)
        self.addButton_5 = QPushButton(self.widget_15)
        self.addButton_5.setObjectName(u"addButton_5")
        self.addButton_5.setGeometry(QRect(10, 680, 231, 61))
        self.addButton_5.setFont(font7)
        self.addButton_5.setStyleSheet(u"QPushButton#addButton_5{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#addButton_5:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#addButton_5:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.catLineEdit_2 = QLineEdit(self.widget_15)
        self.catLineEdit_2.setObjectName(u"catLineEdit_2")
        self.catLineEdit_2.setGeometry(QRect(290, 270, 241, 31))
        self.catLineEdit_2.setReadOnly(True)
        self.label_58 = QLabel(self.widget_15)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(290, 170, 151, 31))
        self.label_58.setFont(font8)
        self.label_58.setStyleSheet(u"color: rgb(0,0,0);")
        self.transamountLineEdit_2 = QLineEdit(self.widget_15)
        self.transamountLineEdit_2.setObjectName(u"transamountLineEdit_2")
        self.transamountLineEdit_2.setGeometry(QRect(290, 340, 241, 31))
        self.transamountLineEdit_2.setReadOnly(True)
        self.transDesc_2 = QTextEdit(self.widget_15)
        self.transDesc_2.setObjectName(u"transDesc_2")
        self.transDesc_2.setGeometry(QRect(560, 190, 431, 261))
        self.transDesc_2.setReadOnly(True)
        self.label_39 = QLabel(self.widget_15)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(290, 310, 151, 31))
        self.label_39.setFont(font8)
        self.label_39.setStyleSheet(u"color: rgb(0,0,0);")
        self.transnameLineEdit_2 = QLineEdit(self.widget_15)
        self.transnameLineEdit_2.setObjectName(u"transnameLineEdit_2")
        self.transnameLineEdit_2.setGeometry(QRect(290, 200, 241, 31))
        self.transnameLineEdit_2.setReadOnly(True)
        self.label_38 = QLabel(self.widget_15)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(570, 160, 151, 31))
        self.label_38.setFont(font8)
        self.label_38.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_67 = QLabel(self.widget_15)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(290, 240, 151, 31))
        self.label_67.setFont(font8)
        self.label_67.setStyleSheet(u"color: rgb(0,0,0);")
        self.EditButton = QPushButton(self.widget_15)
        self.EditButton.setObjectName(u"EditButton")
        self.EditButton.setGeometry(QRect(290, 380, 111, 71))
        self.EditButton.setFont(font7)
        self.EditButton.setStyleSheet(u"QPushButton#EditButton{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#EditButton:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#EditButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.SaveButton = QPushButton(self.widget_15)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setGeometry(QRect(410, 380, 111, 71))
        self.SaveButton.setFont(font7)
        self.SaveButton.setStyleSheet(u"QPushButton#SaveButton{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#SaveButton:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#SaveButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.DeleteTransButton = QPushButton(self.widget_15)
        self.DeleteTransButton.setObjectName(u"DeleteTransButton")
        self.DeleteTransButton.setGeometry(QRect(550, 700, 231, 31))
        self.DeleteTransButton.setFont(font7)
        self.DeleteTransButton.setStyleSheet(u"QPushButton#DeleteTransButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#DeleteTransButton:hover {\n"
"    background-color: rgb(200, 0, 0);\n"
"}\n"
"\n"
"QPushButton#DeleteTransButton:pressed {\n"
"    background-color: rgb(180, 0, 0);\n"
"}\n"
"")
        self.PasswordField = QLineEdit(self.widget_15)
        self.PasswordField.setObjectName(u"PasswordField")
        self.PasswordField.setGeometry(QRect(290, 700, 241, 31))
        self.PasswordField.setEchoMode(QLineEdit.Password)
        self.label_68 = QLabel(self.widget_15)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(290, 680, 141, 16))
        self.goBillsButton_6 = QPushButton(self.widget_15)
        self.goBillsButton_6.setObjectName(u"goBillsButton_6")
        self.goBillsButton_6.setGeometry(QRect(-10, 340, 261, 61))
        self.goBillsButton_6.setFont(font3)
        self.goBillsButton_6.setStyleSheet(u"QPushButton#goBillsButton_6 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goBillsButton_6:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_6:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.notiButton_7 = QPushButton(self.widget_15)
        self.notiButton_7.setObjectName(u"notiButton_7")
        self.notiButton_7.setGeometry(QRect(-10, 400, 261, 61))
        self.notiButton_7.setFont(font3)
        self.notiButton_7.setStyleSheet(u"QPushButton#notiButton_7 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);	color: rgb(255,255,255);\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_7:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_7:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_138 = QLabel(self.widget_15)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setGeometry(QRect(20, 350, 41, 41))
        self.label_138.setPixmap(QPixmap(u":/pics/images/Vzt78rEMgwJJdAAAAABJRU5ErkJggg==.png"))
        self.bellicon_7 = QLabel(self.widget_15)
        self.bellicon_7.setObjectName(u"bellicon_7")
        self.bellicon_7.setGeometry(QRect(20, 410, 41, 41))
        self.bellicon_7.setPixmap(QPixmap(u":/pics/images/k1DgxNmG74K3Ehe5GBarWemJDbD6cZYezwDPqoDrKR6n9dLZP+TlCbMGG3akiX8bAAAAAElFTkSuQmCC.png"))
        self.label_118.raise_()
        self.label_37.raise_()
        self.line_24.raise_()
        self.label_121.raise_()
        self.goTransButton_7.raise_()
        self.goGoalButton_7.raise_()
        self.goDashboardButton_7.raise_()
        self.goAccountButton_7.raise_()
        self.label_115.raise_()
        self.label_119.raise_()
        self.label_120.raise_()
        self.label_122.raise_()
        self.widget_16.raise_()
        self.addButton_5.raise_()
        self.label_117.raise_()
        self.label_116.raise_()
        self.closeButton_9.raise_()
        self.catLineEdit_2.raise_()
        self.label_58.raise_()
        self.transamountLineEdit_2.raise_()
        self.transDesc_2.raise_()
        self.label_39.raise_()
        self.transnameLineEdit_2.raise_()
        self.label_38.raise_()
        self.label_67.raise_()
        self.EditButton.raise_()
        self.SaveButton.raise_()
        self.DeleteTransButton.raise_()
        self.PasswordField.raise_()
        self.label_68.raise_()
        self.goBillsButton_6.raise_()
        self.notiButton_7.raise_()
        self.label_138.raise_()
        self.bellicon_7.raise_()
        self.stackedWidget.addWidget(self.transactionDetailPage)
        self.goalDetailPage = QWidget()
        self.goalDetailPage.setObjectName(u"goalDetailPage")
        self.widget_17 = QWidget(self.goalDetailPage)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_8 = QPushButton(self.widget_17)
        self.goGoalButton_8.setObjectName(u"goGoalButton_8")
        self.goGoalButton_8.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_8.setFont(font3)
        self.goGoalButton_8.setStyleSheet(u"QPushButton#goGoalButton_8 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goGoalButton_8:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goGoalButton_8:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.goDashboardButton_8 = QPushButton(self.widget_17)
        self.goDashboardButton_8.setObjectName(u"goDashboardButton_8")
        self.goDashboardButton_8.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_8.setFont(font3)
        self.goDashboardButton_8.setStyleSheet(u"QPushButton#goDashboardButton_8 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_8:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_8:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_123 = QLabel(self.widget_17)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setGeometry(QRect(20, 170, 31, 31))
        self.label_123.setStyleSheet(u"")
        self.label_123.setPixmap(QPixmap(u":/pics/images/user.png"))
        self.label_123.setScaledContents(True)
        self.label_124 = QLabel(self.widget_17)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setGeometry(QRect(100, 60, 121, 21))
        self.label_124.setFont(font2)
        self.label_124.setStyleSheet(u"color: white;\n"
"")
        self.closeButton_10 = QPushButton(self.widget_17)
        self.closeButton_10.setObjectName(u"closeButton_10")
        self.closeButton_10.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(self.closeButton_10.sizePolicy().hasHeightForWidth())
        self.closeButton_10.setSizePolicy(sizePolicy1)
        self.closeButton_10.setBaseSize(QSize(0, 0))
        self.closeButton_10.setStyleSheet(u"QPushButton#closeButton_10 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton_10:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        self.closeButton_10.setIcon(icon)
        self.label_125 = QLabel(self.widget_17)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setGeometry(QRect(0, 0, 1071, 101))
        self.label_125.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.goAccountButton_8 = QPushButton(self.widget_17)
        self.goAccountButton_8.setObjectName(u"goAccountButton_8")
        self.goAccountButton_8.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_8.setFont(font3)
        self.goAccountButton_8.setStyleSheet(u"QPushButton#goAccountButton_8 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goAccountButton_8:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goAccountButton_8:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_126 = QLabel(self.widget_17)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setGeometry(QRect(0, 100, 1021, 701))
        self.label_126.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_127 = QLabel(self.widget_17)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setGeometry(QRect(20, 290, 31, 31))
        self.label_127.setStyleSheet(u"")
        self.label_127.setPixmap(QPixmap(u":/pics/images/goal.png"))
        self.label_127.setScaledContents(True)
        self.label_128 = QLabel(self.widget_17)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setGeometry(QRect(20, 230, 31, 31))
        self.label_128.setStyleSheet(u"")
        self.label_128.setPixmap(QPixmap(u":/pics/images/trans.png"))
        self.label_128.setScaledContents(True)
        self.label_129 = QLabel(self.widget_17)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setGeometry(QRect(0, 100, 251, 711))
        self.label_129.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.goTransButton_8 = QPushButton(self.widget_17)
        self.goTransButton_8.setObjectName(u"goTransButton_8")
        self.goTransButton_8.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_8.setFont(font3)
        self.goTransButton_8.setStyleSheet(u"QPushButton#goTransButton_8 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goTransButton_8:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goTransButton_8:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_130 = QLabel(self.widget_17)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setGeometry(QRect(20, 110, 31, 31))
        self.label_130.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.label_43 = QLabel(self.widget_17)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(270, 120, 161, 31))
        self.label_43.setFont(font3)
        self.label_43.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_25 = QFrame(self.widget_17)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setGeometry(QRect(270, 150, 731, 16))
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)
        self.addButton_6 = QPushButton(self.widget_17)
        self.addButton_6.setObjectName(u"addButton_6")
        self.addButton_6.setGeometry(QRect(10, 680, 231, 61))
        self.addButton_6.setFont(font7)
        self.addButton_6.setStyleSheet(u"QPushButton#addButton_6{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#addButton_6:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#addButton_6:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_60 = QLabel(self.widget_17)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(290, 170, 151, 31))
        self.label_60.setFont(font8)
        self.label_60.setStyleSheet(u"color: rgb(0,0,0);")
        self.GoalamountLineEdit_3 = QLineEdit(self.widget_17)
        self.GoalamountLineEdit_3.setObjectName(u"GoalamountLineEdit_3")
        self.GoalamountLineEdit_3.setGeometry(QRect(290, 270, 241, 31))
        self.GoalamountLineEdit_3.setReadOnly(True)
        self.GoalDesc_3 = QTextEdit(self.widget_17)
        self.GoalDesc_3.setObjectName(u"GoalDesc_3")
        self.GoalDesc_3.setGeometry(QRect(560, 190, 431, 191))
        self.GoalDesc_3.setReadOnly(True)
        self.label_46 = QLabel(self.widget_17)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(290, 240, 151, 31))
        self.label_46.setFont(font8)
        self.label_46.setStyleSheet(u"color: rgb(0,0,0);")
        self.GoalnameLineEdit_3 = QLineEdit(self.widget_17)
        self.GoalnameLineEdit_3.setObjectName(u"GoalnameLineEdit_3")
        self.GoalnameLineEdit_3.setGeometry(QRect(290, 200, 241, 31))
        self.GoalnameLineEdit_3.setReadOnly(True)
        self.label_51 = QLabel(self.widget_17)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(570, 160, 151, 31))
        self.label_51.setFont(font8)
        self.label_51.setStyleSheet(u"color: rgb(0,0,0);")
        self.EditButton_2 = QPushButton(self.widget_17)
        self.EditButton_2.setObjectName(u"EditButton_2")
        self.EditButton_2.setGeometry(QRect(290, 320, 111, 71))
        self.EditButton_2.setFont(font7)
        self.EditButton_2.setStyleSheet(u"QPushButton#EditButton_2{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#EditButton_2:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#EditButton_2:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.SaveButton_2 = QPushButton(self.widget_17)
        self.SaveButton_2.setObjectName(u"SaveButton_2")
        self.SaveButton_2.setGeometry(QRect(410, 320, 111, 71))
        self.SaveButton_2.setFont(font7)
        self.SaveButton_2.setStyleSheet(u"QPushButton#SaveButton_2{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#SaveButton_2:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#SaveButton_2:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.DeleteGoalButton = QPushButton(self.widget_17)
        self.DeleteGoalButton.setObjectName(u"DeleteGoalButton")
        self.DeleteGoalButton.setGeometry(QRect(570, 700, 231, 31))
        self.DeleteGoalButton.setFont(font7)
        self.DeleteGoalButton.setStyleSheet(u"QPushButton#DeleteGoalButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#DeleteGoalButton:hover {\n"
"    background-color: rgb(200, 0, 0);\n"
"}\n"
"\n"
"QPushButton#DeleteGoalButton:pressed {\n"
"    background-color: rgb(180, 0, 0);\n"
"}\n"
"")
        self.PasswordField_2 = QLineEdit(self.widget_17)
        self.PasswordField_2.setObjectName(u"PasswordField_2")
        self.PasswordField_2.setGeometry(QRect(290, 700, 241, 31))
        self.PasswordField_2.setEchoMode(QLineEdit.Password)
        self.label_71 = QLabel(self.widget_17)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(290, 680, 141, 16))
        self.label_73 = QLabel(self.widget_17)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(290, 480, 221, 91))
        self.label_73.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.label_72 = QLabel(self.widget_17)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(300, 485, 111, 16))
        self.label_72.setFont(font4)
        self.label_72.setStyleSheet(u"color: rgb(148,148,148);")
        self.GoalBalanceLabel_2 = QLabel(self.widget_17)
        self.GoalBalanceLabel_2.setObjectName(u"GoalBalanceLabel_2")
        self.GoalBalanceLabel_2.setGeometry(QRect(380, 520, 171, 21))
        self.GoalBalanceLabel_2.setFont(font3)
        self.GoalBalanceLabel_2.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_70 = QLabel(self.widget_17)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(320, 515, 16, 31))
        self.label_70.setFont(font3)
        self.label_70.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_74 = QLabel(self.widget_17)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(290, 560, 221, 21))
        self.label_74.setStyleSheet(u"background-color: rgb(178,241,149);\n"
"")
        self.currentBalanceLabel_3 = QLabel(self.widget_17)
        self.currentBalanceLabel_3.setObjectName(u"currentBalanceLabel_3")
        self.currentBalanceLabel_3.setGeometry(QRect(650, 520, 171, 21))
        self.currentBalanceLabel_3.setFont(font3)
        self.currentBalanceLabel_3.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_87 = QLabel(self.widget_17)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(530, 560, 221, 21))
        self.label_87.setStyleSheet(u"background-color: rgb(178,241,149);\n"
"")
        self.label_109 = QLabel(self.widget_17)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(590, 515, 16, 31))
        self.label_109.setFont(font3)
        self.label_109.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_110 = QLabel(self.widget_17)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(570, 485, 111, 16))
        self.label_110.setFont(font4)
        self.label_110.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_111 = QLabel(self.widget_17)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(530, 480, 221, 91))
        self.label_111.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.progressBar = QProgressBar(self.widget_17)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(280, 610, 721, 61))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: none;\n"
"    background-color: #e5e5e5;\n"
"    height: 20px; /* Adjust the height to make it look bigger */\n"
"    margin: 10px; /* Add some margin to give it space */\n"
"    text-align: center; /* Center-align the percent text */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(81, 74, 248); /* Set the progress chunk color */\n"
"    width: 20px; /* Adjust the width to make the progress chunk wider */\n"
"}\n"
"\n"
"QProgressBar::chunk:horizontal {\n"
"    margin-right: 0px; /* Remove the right margin of the progress chunk */\n"
"}\n"
"\n"
"QProgressBar::chunk:vertical {\n"
"    margin-bottom: 0px; /* Remove the bottom margin of the progress chunk */\n"
"}\n"
"\n"
"QProgressBar::chunk::chunk {\n"
"    background-color: rgb(81, 74, 248); /* Set the progress chunk color for nested chunk */\n"
"}\n"
"\n"
"QProgressBar::chunk::chunk:vertical {\n"
"    height: 100%; /* Set the height of the nested progress chunk */\n"
"}\n"
"\n"
"QProgressBar::chunk::chunk:horiz"
                        "ontal {\n"
"    width: 100%; /* Set the width of the nested progress chunk */\n"
"}\n"
"\n"
"QProgressBar::chunk::subcontrol {\n"
"    padding-right: 2px; /* Adjust the spacing between the progress chunk and the percent text */\n"
"}\n"
"\n"
"QProgressBar::chunk::subcontrol:horizontal {\n"
"    padding: 0px;\n"
"    height: 100%; /* Set the height of the subcontrol for horizontal progress */\n"
"}\n"
"\n"
"QProgressBar::chunk::subcontrol:vertical {\n"
"    padding: 0px;\n"
"    width: 100%; /* Set the width of the subcontrol for vertical progress */\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.label_27 = QLabel(self.widget_17)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(290, 600, 91, 16))
        self.GoalBalanceLabel_4 = QLabel(self.widget_17)
        self.GoalBalanceLabel_4.setObjectName(u"GoalBalanceLabel_4")
        self.GoalBalanceLabel_4.setGeometry(QRect(620, 520, 171, 21))
        self.GoalBalanceLabel_4.setFont(font3)
        self.GoalBalanceLabel_4.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_112 = QLabel(self.widget_17)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setGeometry(QRect(560, 515, 16, 31))
        self.label_112.setFont(font3)
        self.label_112.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_113 = QLabel(self.widget_17)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(540, 485, 111, 16))
        self.label_113.setFont(font4)
        self.label_113.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_114 = QLabel(self.widget_17)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setGeometry(QRect(770, 480, 221, 91))
        self.label_114.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.label_131 = QLabel(self.widget_17)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setGeometry(QRect(770, 560, 221, 21))
        self.label_131.setStyleSheet(u"background-color: rgb(178,241,149);\n"
"")
        self.label_132 = QLabel(self.widget_17)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setGeometry(QRect(780, 485, 111, 16))
        self.label_132.setFont(font4)
        self.label_132.setStyleSheet(u"color: rgb(148,148,148);")
        self.label_133 = QLabel(self.widget_17)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setGeometry(QRect(800, 515, 16, 31))
        self.label_133.setFont(font3)
        self.label_133.setStyleSheet(u"color: rgb(0,0,0);")
        self.GoalBalanceLabel_5 = QLabel(self.widget_17)
        self.GoalBalanceLabel_5.setObjectName(u"GoalBalanceLabel_5")
        self.GoalBalanceLabel_5.setGeometry(QRect(860, 520, 171, 21))
        self.GoalBalanceLabel_5.setFont(font3)
        self.GoalBalanceLabel_5.setStyleSheet(u"color: rgb(0,0,0);")
        self.GoalFund_4 = QLineEdit(self.widget_17)
        self.GoalFund_4.setObjectName(u"GoalFund_4")
        self.GoalFund_4.setGeometry(QRect(290, 420, 231, 31))
        self.GoalFund_4.setReadOnly(False)
        self.GoalDefund_5 = QLineEdit(self.widget_17)
        self.GoalDefund_5.setObjectName(u"GoalDefund_5")
        self.GoalDefund_5.setGeometry(QRect(660, 420, 221, 31))
        self.GoalDefund_5.setReadOnly(False)
        self.FundGoalButton = QPushButton(self.widget_17)
        self.FundGoalButton.setObjectName(u"FundGoalButton")
        self.FundGoalButton.setGeometry(QRect(530, 410, 111, 51))
        self.FundGoalButton.setFont(font7)
        self.FundGoalButton.setStyleSheet(u"QPushButton#FundGoalButton{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#FundGoalButton:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#FundGoalButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.deFundGoalButton = QPushButton(self.widget_17)
        self.deFundGoalButton.setObjectName(u"deFundGoalButton")
        self.deFundGoalButton.setGeometry(QRect(890, 410, 111, 51))
        self.deFundGoalButton.setFont(font7)
        self.deFundGoalButton.setStyleSheet(u"QPushButton#deFundGoalButton{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#deFundGoalButton:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#deFundGoalButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.goBillsButton_7 = QPushButton(self.widget_17)
        self.goBillsButton_7.setObjectName(u"goBillsButton_7")
        self.goBillsButton_7.setGeometry(QRect(-10, 340, 261, 61))
        self.goBillsButton_7.setFont(font3)
        self.goBillsButton_7.setStyleSheet(u"QPushButton#goBillsButton_7 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goBillsButton_7:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_7:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.notiButton_8 = QPushButton(self.widget_17)
        self.notiButton_8.setObjectName(u"notiButton_8")
        self.notiButton_8.setGeometry(QRect(-10, 400, 261, 61))
        self.notiButton_8.setFont(font3)
        self.notiButton_8.setStyleSheet(u"QPushButton#notiButton_8 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);	color: rgb(255,255,255);\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_8:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_8:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_139 = QLabel(self.widget_17)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setGeometry(QRect(20, 350, 41, 41))
        self.label_139.setPixmap(QPixmap(u":/pics/images/Vzt78rEMgwJJdAAAAABJRU5ErkJggg==.png"))
        self.bellicon_8 = QLabel(self.widget_17)
        self.bellicon_8.setObjectName(u"bellicon_8")
        self.bellicon_8.setGeometry(QRect(20, 410, 41, 41))
        self.bellicon_8.setPixmap(QPixmap(u":/pics/images/k1DgxNmG74K3Ehe5GBarWemJDbD6cZYezwDPqoDrKR6n9dLZP+TlCbMGG3akiX8bAAAAAElFTkSuQmCC.png"))
        self.label_126.raise_()
        self.label_74.raise_()
        self.label_125.raise_()
        self.label_129.raise_()
        self.goTransButton_8.raise_()
        self.label_43.raise_()
        self.line_25.raise_()
        self.label_60.raise_()
        self.GoalamountLineEdit_3.raise_()
        self.GoalDesc_3.raise_()
        self.label_46.raise_()
        self.GoalnameLineEdit_3.raise_()
        self.label_51.raise_()
        self.EditButton_2.raise_()
        self.SaveButton_2.raise_()
        self.DeleteGoalButton.raise_()
        self.PasswordField_2.raise_()
        self.label_71.raise_()
        self.goAccountButton_8.raise_()
        self.goDashboardButton_8.raise_()
        self.goGoalButton_8.raise_()
        self.addButton_6.raise_()
        self.label_123.raise_()
        self.label_124.raise_()
        self.label_127.raise_()
        self.label_128.raise_()
        self.label_130.raise_()
        self.closeButton_10.raise_()
        self.label_73.raise_()
        self.label_72.raise_()
        self.GoalBalanceLabel_2.raise_()
        self.label_70.raise_()
        self.currentBalanceLabel_3.raise_()
        self.label_87.raise_()
        self.label_109.raise_()
        self.label_110.raise_()
        self.label_111.raise_()
        self.progressBar.raise_()
        self.label_27.raise_()
        self.GoalBalanceLabel_4.raise_()
        self.label_112.raise_()
        self.label_113.raise_()
        self.label_131.raise_()
        self.label_114.raise_()
        self.label_132.raise_()
        self.label_133.raise_()
        self.GoalBalanceLabel_5.raise_()
        self.GoalFund_4.raise_()
        self.GoalDefund_5.raise_()
        self.FundGoalButton.raise_()
        self.deFundGoalButton.raise_()
        self.goBillsButton_7.raise_()
        self.notiButton_8.raise_()
        self.label_139.raise_()
        self.bellicon_8.raise_()
        self.stackedWidget.addWidget(self.goalDetailPage)
        self.addBillPage = QWidget()
        self.addBillPage.setObjectName(u"addBillPage")
        self.widget_23 = QWidget(self.addBillPage)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_14 = QPushButton(self.widget_23)
        self.goGoalButton_14.setObjectName(u"goGoalButton_14")
        self.goGoalButton_14.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_14.setFont(font3)
        self.goGoalButton_14.setStyleSheet(u"QPushButton#goGoalButton_14 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goGoalButton_14:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goGoalButton_14:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.goDashboardButton_14 = QPushButton(self.widget_23)
        self.goDashboardButton_14.setObjectName(u"goDashboardButton_14")
        self.goDashboardButton_14.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_14.setFont(font3)
        self.goDashboardButton_14.setStyleSheet(u"QPushButton#goDashboardButton_14 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goDashboardButton_14:hover {\n"
" \n"
"   background-color: rgb(81,74,200);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_14:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_214 = QLabel(self.widget_23)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setGeometry(QRect(20, 170, 31, 31))
        self.label_214.setStyleSheet(u"")
        self.label_214.setPixmap(QPixmap(u":/pics/images/user.png"))
        self.label_214.setScaledContents(True)
        self.label_215 = QLabel(self.widget_23)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setGeometry(QRect(100, 60, 121, 21))
        self.label_215.setFont(font2)
        self.label_215.setStyleSheet(u"color: white;\n"
"")
        self.closeButton_16 = QPushButton(self.widget_23)
        self.closeButton_16.setObjectName(u"closeButton_16")
        self.closeButton_16.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(self.closeButton_16.sizePolicy().hasHeightForWidth())
        self.closeButton_16.setSizePolicy(sizePolicy1)
        self.closeButton_16.setBaseSize(QSize(0, 0))
        self.closeButton_16.setStyleSheet(u"QPushButton#closeButton_16 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton_16:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        self.closeButton_16.setIcon(icon)
        self.label_216 = QLabel(self.widget_23)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setGeometry(QRect(0, 0, 1071, 101))
        self.label_216.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.goAccountButton_14 = QPushButton(self.widget_23)
        self.goAccountButton_14.setObjectName(u"goAccountButton_14")
        self.goAccountButton_14.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_14.setFont(font3)
        self.goAccountButton_14.setStyleSheet(u"QPushButton#goAccountButton_14 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goAccountButton_14:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goAccountButton_14:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_217 = QLabel(self.widget_23)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setGeometry(QRect(0, 100, 1021, 701))
        self.label_217.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_218 = QLabel(self.widget_23)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setGeometry(QRect(20, 290, 31, 31))
        self.label_218.setStyleSheet(u"")
        self.label_218.setPixmap(QPixmap(u":/pics/images/goal.png"))
        self.label_218.setScaledContents(True)
        self.label_219 = QLabel(self.widget_23)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setGeometry(QRect(20, 230, 31, 31))
        self.label_219.setStyleSheet(u"")
        self.label_219.setPixmap(QPixmap(u":/pics/images/trans.png"))
        self.label_219.setScaledContents(True)
        self.label_220 = QLabel(self.widget_23)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setGeometry(QRect(0, 100, 251, 701))
        self.label_220.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.goTransButton_14 = QPushButton(self.widget_23)
        self.goTransButton_14.setObjectName(u"goTransButton_14")
        self.goTransButton_14.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_14.setFont(font3)
        self.goTransButton_14.setStyleSheet(u"QPushButton#goTransButton_14 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goTransButton_14:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goTransButton_14:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_221 = QLabel(self.widget_23)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setGeometry(QRect(20, 110, 31, 31))
        self.label_221.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.label_226 = QLabel(self.widget_23)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setGeometry(QRect(270, 120, 151, 31))
        self.label_226.setFont(font3)
        self.label_226.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_32 = QFrame(self.widget_23)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setGeometry(QRect(260, 150, 731, 16))
        self.line_32.setFrameShape(QFrame.HLine)
        self.line_32.setFrameShadow(QFrame.Sunken)
        self.billsnameLineEdit = QLineEdit(self.widget_23)
        self.billsnameLineEdit.setObjectName(u"billsnameLineEdit")
        self.billsnameLineEdit.setGeometry(QRect(270, 200, 241, 31))
        self.billsamountLineedit = QLineEdit(self.widget_23)
        self.billsamountLineedit.setObjectName(u"billsamountLineedit")
        self.billsamountLineedit.setGeometry(QRect(270, 280, 241, 31))
        self.label_227 = QLabel(self.widget_23)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setGeometry(QRect(270, 170, 151, 31))
        self.label_227.setFont(font8)
        self.label_227.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_228 = QLabel(self.widget_23)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setGeometry(QRect(270, 250, 151, 31))
        self.label_228.setFont(font8)
        self.label_228.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_229 = QLabel(self.widget_23)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setGeometry(QRect(560, 160, 151, 31))
        self.label_229.setFont(font8)
        self.label_229.setStyleSheet(u"color: rgb(0,0,0);")
        self.saveBillsButton = QPushButton(self.widget_23)
        self.saveBillsButton.setObjectName(u"saveBillsButton")
        self.saveBillsButton.setGeometry(QRect(270, 610, 113, 32))
        self.saveBillsButton.setStyleSheet(u"QPushButton#saveBillsButton{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#saveBillsButton:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#saveBillsButton:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.BillsDesc = QTextEdit(self.widget_23)
        self.BillsDesc.setObjectName(u"BillsDesc")
        self.BillsDesc.setGeometry(QRect(560, 200, 431, 111))
        self.goBillsButton_14 = QPushButton(self.widget_23)
        self.goBillsButton_14.setObjectName(u"goBillsButton_14")
        self.goBillsButton_14.setGeometry(QRect(-10, 340, 261, 61))
        self.goBillsButton_14.setFont(font3)
        self.goBillsButton_14.setStyleSheet(u"QPushButton#goBillsButton_14 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goBillsButton_14:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_14:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_254 = QLabel(self.widget_23)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setGeometry(QRect(270, 330, 151, 31))
        self.label_254.setFont(font8)
        self.label_254.setStyleSheet(u"color: rgb(0,0,0);")
        self.calendarWidget_2 = QCalendarWidget(self.widget_23)
        self.calendarWidget_2.setObjectName(u"calendarWidget_2")
        self.calendarWidget_2.setGeometry(QRect(270, 360, 421, 241))
        self.notiButton_9 = QPushButton(self.widget_23)
        self.notiButton_9.setObjectName(u"notiButton_9")
        self.notiButton_9.setGeometry(QRect(-10, 400, 261, 61))
        self.notiButton_9.setFont(font3)
        self.notiButton_9.setStyleSheet(u"QPushButton#notiButton_9 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);	color: rgb(255,255,255);\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_9:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_9:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_140 = QLabel(self.widget_23)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setGeometry(QRect(20, 350, 41, 41))
        self.label_140.setPixmap(QPixmap(u":/pics/images/Vzt78rEMgwJJdAAAAABJRU5ErkJggg==.png"))
        self.bellicon_9 = QLabel(self.widget_23)
        self.bellicon_9.setObjectName(u"bellicon_9")
        self.bellicon_9.setGeometry(QRect(20, 410, 41, 41))
        self.bellicon_9.setPixmap(QPixmap(u":/pics/images/k1DgxNmG74K3Ehe5GBarWemJDbD6cZYezwDPqoDrKR6n9dLZP+TlCbMGG3akiX8bAAAAAElFTkSuQmCC.png"))
        self.label_216.raise_()
        self.label_217.raise_()
        self.label_220.raise_()
        self.label_226.raise_()
        self.line_32.raise_()
        self.billsnameLineEdit.raise_()
        self.billsamountLineedit.raise_()
        self.label_227.raise_()
        self.label_228.raise_()
        self.label_229.raise_()
        self.saveBillsButton.raise_()
        self.BillsDesc.raise_()
        self.goBillsButton_14.raise_()
        self.goAccountButton_14.raise_()
        self.goDashboardButton_14.raise_()
        self.goGoalButton_14.raise_()
        self.goTransButton_14.raise_()
        self.label_214.raise_()
        self.label_215.raise_()
        self.label_218.raise_()
        self.label_219.raise_()
        self.label_221.raise_()
        self.closeButton_16.raise_()
        self.label_254.raise_()
        self.calendarWidget_2.raise_()
        self.notiButton_9.raise_()
        self.label_140.raise_()
        self.bellicon_9.raise_()
        self.stackedWidget.addWidget(self.addBillPage)
        self.billDetailPage = QWidget()
        self.billDetailPage.setObjectName(u"billDetailPage")
        self.widget_24 = QWidget(self.billDetailPage)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_16 = QPushButton(self.widget_24)
        self.goGoalButton_16.setObjectName(u"goGoalButton_16")
        self.goGoalButton_16.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_16.setFont(font3)
        self.goGoalButton_16.setStyleSheet(u"QPushButton#goGoalButton_16 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goGoalButton_16:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goGoalButton_16:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.goDashboardButton_16 = QPushButton(self.widget_24)
        self.goDashboardButton_16.setObjectName(u"goDashboardButton_16")
        self.goDashboardButton_16.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_16.setFont(font3)
        self.goDashboardButton_16.setStyleSheet(u"QPushButton#goDashboardButton_16 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_16:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goDashboardButton_16:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_240 = QLabel(self.widget_24)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setGeometry(QRect(20, 170, 31, 31))
        self.label_240.setStyleSheet(u"")
        self.label_240.setPixmap(QPixmap(u":/pics/images/user.png"))
        self.label_240.setScaledContents(True)
        self.label_241 = QLabel(self.widget_24)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setGeometry(QRect(100, 60, 121, 21))
        self.label_241.setFont(font2)
        self.label_241.setStyleSheet(u"color: white;\n"
"")
        self.closeButton_18 = QPushButton(self.widget_24)
        self.closeButton_18.setObjectName(u"closeButton_18")
        self.closeButton_18.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(self.closeButton_18.sizePolicy().hasHeightForWidth())
        self.closeButton_18.setSizePolicy(sizePolicy1)
        self.closeButton_18.setBaseSize(QSize(0, 0))
        self.closeButton_18.setStyleSheet(u"QPushButton#closeButton_18 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"}\n"
"\n"
"QPushButton#closeButton_18:hover {\n"
"    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
"    border-radius: 50%; /* set the border radius to create a circle */\n"
"}\n"
"")
        self.closeButton_18.setIcon(icon)
        self.label_242 = QLabel(self.widget_24)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setGeometry(QRect(0, 0, 1071, 101))
        self.label_242.setStyleSheet(u"background-color: rgb(81,74,248);")
        self.goAccountButton_16 = QPushButton(self.widget_24)
        self.goAccountButton_16.setObjectName(u"goAccountButton_16")
        self.goAccountButton_16.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_16.setFont(font3)
        self.goAccountButton_16.setStyleSheet(u"QPushButton#goAccountButton_16 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goAccountButton_16:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goAccountButton_16:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_243 = QLabel(self.widget_24)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setGeometry(QRect(0, 100, 1021, 701))
        self.label_243.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_244 = QLabel(self.widget_24)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setGeometry(QRect(20, 290, 31, 31))
        self.label_244.setStyleSheet(u"")
        self.label_244.setPixmap(QPixmap(u":/pics/images/goal.png"))
        self.label_244.setScaledContents(True)
        self.label_245 = QLabel(self.widget_24)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setGeometry(QRect(20, 230, 31, 31))
        self.label_245.setStyleSheet(u"")
        self.label_245.setPixmap(QPixmap(u":/pics/images/trans.png"))
        self.label_245.setScaledContents(True)
        self.label_246 = QLabel(self.widget_24)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setGeometry(QRect(0, 100, 251, 711))
        self.label_246.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.goTransButton_16 = QPushButton(self.widget_24)
        self.goTransButton_16.setObjectName(u"goTransButton_16")
        self.goTransButton_16.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_16.setFont(font3)
        self.goTransButton_16.setStyleSheet(u"QPushButton#goTransButton_16 {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton#goTransButton_16:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#goTransButton_16:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.label_247 = QLabel(self.widget_24)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setGeometry(QRect(20, 110, 31, 31))
        self.label_247.setStyleSheet(u"background-image: url(:/pics/images/home.png);")
        self.label_248 = QLabel(self.widget_24)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setGeometry(QRect(270, 120, 161, 31))
        self.label_248.setFont(font3)
        self.label_248.setStyleSheet(u"color: rgb(0,0,0);")
        self.line_33 = QFrame(self.widget_24)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setGeometry(QRect(270, 150, 731, 16))
        self.line_33.setFrameShape(QFrame.HLine)
        self.line_33.setFrameShadow(QFrame.Sunken)
        self.addButton_13 = QPushButton(self.widget_24)
        self.addButton_13.setObjectName(u"addButton_13")
        self.addButton_13.setGeometry(QRect(10, 680, 231, 61))
        self.addButton_13.setFont(font7)
        self.addButton_13.setStyleSheet(u"QPushButton#addButton_13{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#addButton_13:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#addButton_13:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.billsamountLineEdit_5 = QLineEdit(self.widget_24)
        self.billsamountLineEdit_5.setObjectName(u"billsamountLineEdit_5")
        self.billsamountLineEdit_5.setGeometry(QRect(290, 270, 241, 31))
        self.billsamountLineEdit_5.setReadOnly(True)
        self.label_249 = QLabel(self.widget_24)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setGeometry(QRect(290, 170, 151, 31))
        self.label_249.setFont(font8)
        self.label_249.setStyleSheet(u"color: rgb(0,0,0);")
        self.billsDesc_5 = QTextEdit(self.widget_24)
        self.billsDesc_5.setObjectName(u"billsDesc_5")
        self.billsDesc_5.setGeometry(QRect(560, 190, 431, 111))
        self.billsDesc_5.setReadOnly(True)
        self.label_250 = QLabel(self.widget_24)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setGeometry(QRect(290, 310, 151, 31))
        self.label_250.setFont(font8)
        self.label_250.setStyleSheet(u"color: rgb(0,0,0);")
        self.billsnameLineEdit_5 = QLineEdit(self.widget_24)
        self.billsnameLineEdit_5.setObjectName(u"billsnameLineEdit_5")
        self.billsnameLineEdit_5.setGeometry(QRect(290, 200, 241, 31))
        self.billsnameLineEdit_5.setReadOnly(True)
        self.label_251 = QLabel(self.widget_24)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setGeometry(QRect(570, 160, 151, 31))
        self.label_251.setFont(font8)
        self.label_251.setStyleSheet(u"color: rgb(0,0,0);")
        self.label_252 = QLabel(self.widget_24)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setGeometry(QRect(290, 240, 151, 31))
        self.label_252.setFont(font8)
        self.label_252.setStyleSheet(u"color: rgb(0,0,0);")
        self.EditButton_4 = QPushButton(self.widget_24)
        self.EditButton_4.setObjectName(u"EditButton_4")
        self.EditButton_4.setGeometry(QRect(290, 580, 111, 71))
        self.EditButton_4.setFont(font7)
        self.EditButton_4.setStyleSheet(u"QPushButton#EditButton_4{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#EditButton_4:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#EditButton_4:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.SaveButton_4 = QPushButton(self.widget_24)
        self.SaveButton_4.setObjectName(u"SaveButton_4")
        self.SaveButton_4.setGeometry(QRect(410, 580, 111, 71))
        self.SaveButton_4.setFont(font7)
        self.SaveButton_4.setStyleSheet(u"QPushButton#SaveButton_4{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(81, 74, 248);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#SaveButton_4:hover {\n"
"    background-color: rgb(81, 74, 200);\n"
"}\n"
"\n"
"QPushButton#SaveButton_4:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}\n"
"")
        self.deleteBillsButton = QPushButton(self.widget_24)
        self.deleteBillsButton.setObjectName(u"deleteBillsButton")
        self.deleteBillsButton.setGeometry(QRect(550, 700, 231, 31))
        self.deleteBillsButton.setFont(font7)
        self.deleteBillsButton.setStyleSheet(u"QPushButton#deleteBillsButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#deleteBillsButton:hover {\n"
"    background-color: rgb(200, 0, 0);\n"
"}\n"
"\n"
"QPushButton#deleteBillsButton:pressed {\n"
"    background-color: rgb(180, 0, 0);\n"
"}\n"
"")
        self.PasswordField_4 = QLineEdit(self.widget_24)
        self.PasswordField_4.setObjectName(u"PasswordField_4")
        self.PasswordField_4.setGeometry(QRect(290, 700, 241, 31))
        self.PasswordField_4.setEchoMode(QLineEdit.Password)
        self.label_253 = QLabel(self.widget_24)
        self.label_253.setObjectName(u"label_253")
        self.label_253.setGeometry(QRect(290, 680, 141, 16))
        self.goBillsButton_16 = QPushButton(self.widget_24)
        self.goBillsButton_16.setObjectName(u"goBillsButton_16")
        self.goBillsButton_16.setGeometry(QRect(-10, 340, 261, 61))
        self.goBillsButton_16.setFont(font3)
        self.goBillsButton_16.setStyleSheet(u"QPushButton#goBillsButton_16 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton#goBillsButton_16:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#goBillsButton_16:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.calendarWidget = QCalendarWidget(self.widget_24)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(290, 340, 391, 231))
        self.notiButton_10 = QPushButton(self.widget_24)
        self.notiButton_10.setObjectName(u"notiButton_10")
        self.notiButton_10.setGeometry(QRect(-10, 400, 261, 61))
        self.notiButton_10.setFont(font3)
        self.notiButton_10.setStyleSheet(u"QPushButton#notiButton_10 {\n"
"    border: none;\n"
"    border-radius: 10px; /* set the initial border radius */\n"
"	color: rgb(0,0,0);	color: rgb(255,255,255);\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_10:hover {\n"
"    background-color: rgb(81,74,200);\n"
"}\n"
"QPushButton#notiButton_10:pressed {\n"
"    background-color: rgb(61, 54, 180);\n"
"}")
        self.label_141 = QLabel(self.widget_24)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setGeometry(QRect(20, 350, 41, 41))
        self.label_141.setPixmap(QPixmap(u":/pics/images/Vzt78rEMgwJJdAAAAABJRU5ErkJggg==.png"))
        self.bellicon_10 = QLabel(self.widget_24)
        self.bellicon_10.setObjectName(u"bellicon_10")
        self.bellicon_10.setGeometry(QRect(20, 410, 41, 41))
        self.bellicon_10.setPixmap(QPixmap(u":/pics/images/k1DgxNmG74K3Ehe5GBarWemJDbD6cZYezwDPqoDrKR6n9dLZP+TlCbMGG3akiX8bAAAAAElFTkSuQmCC.png"))
        self.label_242.raise_()
        self.label_243.raise_()
        self.label_246.raise_()
        self.goTransButton_16.raise_()
        self.label_248.raise_()
        self.line_33.raise_()
        self.addButton_13.raise_()
        self.billsamountLineEdit_5.raise_()
        self.label_249.raise_()
        self.billsDesc_5.raise_()
        self.label_250.raise_()
        self.billsnameLineEdit_5.raise_()
        self.label_251.raise_()
        self.label_252.raise_()
        self.EditButton_4.raise_()
        self.SaveButton_4.raise_()
        self.deleteBillsButton.raise_()
        self.PasswordField_4.raise_()
        self.label_253.raise_()
        self.goBillsButton_16.raise_()
        self.closeButton_18.raise_()
        self.goAccountButton_16.raise_()
        self.goDashboardButton_16.raise_()
        self.goGoalButton_16.raise_()
        self.label_240.raise_()
        self.label_241.raise_()
        self.label_244.raise_()
        self.label_245.raise_()
        self.label_247.raise_()
        self.calendarWidget.raise_()
        self.notiButton_10.raise_()
        self.label_141.raise_()
        self.bellicon_10.raise_()
        self.stackedWidget.addWidget(self.billDetailPage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)

        self.retranslateUi(Form)
        self.closeButton.clicked.connect(Form.close)
        self.closeButton_2.clicked.connect(Form.close)
        self.closeButton_3.clicked.connect(Form.close)
        self.closeButton_4.clicked.connect(Form.close)
        self.closeButton_5.clicked.connect(Form.close)
        self.closeButton_6.clicked.connect(Form.close)
        self.closeButton_7.clicked.connect(Form.close)
        self.closeButton_9.clicked.connect(Form.close)
        self.closeButton_10.clicked.connect(Form.close)
        self.closeButton_18.clicked.connect(Form.close)
        self.closeButton_16.clicked.connect(Form.close)
        self.closeButton_14.clicked.connect(Form.close)

        self.stackedWidget.setCurrentIndex(3)


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
        self.currentBalanceLabel.setText(QCoreApplication.translate("Form", u"0", None))
        self.budgetLabel.setText(QCoreApplication.translate("Form", u"0", None))
        self.goGoalButton.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.label_41.setText("")
        self.goDashboardButton.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"Current Balance", None))
        self.label_45.setText("")
        self.label_47.setText("")
        self.label_48.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.label_49.setText("")
        self.label_50.setText(QCoreApplication.translate("Form", u"Weekly Budget", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.closeButton_3.setText("")
        self.label_53.setText("")
        self.label_54.setText(QCoreApplication.translate("Form", u"Weekly Spent", None))
        self.label_55.setText("")
        self.label_56.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_57.setText("")
        self.spentLabel.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.goAccountButton.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_61.setText("")
        self.label_62.setText("")
        self.label_63.setText("")
        self.goTransButton.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_64.setText("")
        self.label_65.setText(QCoreApplication.translate("Form", u"Recent Transactions:", None))
        self.label_66.setText("")
        self.addButton.setText(QCoreApplication.translate("Form", u"Add a Transaction / Goal", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Transaction Name", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Transaction Date", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Transaction Amount", None))
        self.label_69.setText(QCoreApplication.translate("Form", u"Goals:", None))
        self.label_108.setText("")
        self.goBillsButton.setText(QCoreApplication.translate("Form", u"Bills", None))
        self.notiButton.setText(QCoreApplication.translate("Form", u"Notification", None))
        self.label_29.setText("")
        self.bellicon.setText("")
        self.goGoalButton_2.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.goDashboardButton_2.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_75.setText("")
        self.label_76.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.closeButton_4.setText("")
        self.label_83.setText("")
        self.goAccountButton_2.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_88.setText("")
        self.label_89.setText("")
        self.label_90.setText("")
        self.label_91.setText("")
        self.goTransButton_2.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_94.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"New Transaction", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Transaction Name", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Category", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Description", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"New Goal", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Goal Name", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Goal Amount", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Description", None))
        self.income_radio.setText(QCoreApplication.translate("Form", u"Income", None))
        self.expense_radio.setText(QCoreApplication.translate("Form", u"Expense", None))
        self.saveTransButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.saveGoalButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Transaction Amount", None))
        self.goBillsButton_2.setText(QCoreApplication.translate("Form", u"Bills", None))
        self.notiButton_2.setText(QCoreApplication.translate("Form", u"Notification", None))
        self.label_30.setText("")
        self.bellicon_2.setText("")
        self.label_142.setText(QCoreApplication.translate("Form", u"Date/Time", None))
        self.goGoalButton_12.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.goDashboardButton_12.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_184.setText("")
        self.label_185.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.closeButton_14.setText("")
        self.label_186.setText("")
        self.goAccountButton_12.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_187.setText("")
        self.label_188.setText("")
        self.label_189.setText("")
        self.label_190.setText("")
        self.goTransButton_12.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_191.setText("")
        self.label_192.setText(QCoreApplication.translate("Form", u"Bills Reminder", None))
        self.label_193.setText(QCoreApplication.translate("Form", u"Bill Name", None))
        self.label_194.setText(QCoreApplication.translate("Form", u"Due Date", None))
        self.label_195.setText(QCoreApplication.translate("Form", u"Bill Amount", None))
        self.label_196.setText("")
        self.addButton_11.setText(QCoreApplication.translate("Form", u"Add a Transaction / Goal", None))
        self.goBillsButton_12.setText(QCoreApplication.translate("Form", u"Bills", None))
        self.addBillsButton.setText(QCoreApplication.translate("Form", u"Add Bills", None))
        self.notiButton_3.setText(QCoreApplication.translate("Form", u"Notification", None))
        self.label_31.setText("")
        self.bellicon_3.setText("")
        self.goGoalButton_3.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.goDashboardButton_3.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_77.setText("")
        self.label_78.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.closeButton_5.setText("")
        self.label_84.setText("")
        self.goAccountButton_3.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_92.setText("")
        self.label_93.setText("")
        self.label_95.setText("")
        self.label_96.setText("")
        self.goTransButton_3.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_97.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"Transaction", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Transaction Name", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Transaction Date", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Transaction Amount", None))
        self.label_22.setText("")
        self.addButton_2.setText(QCoreApplication.translate("Form", u"Add a Transaction / Goal", None))
        self.goBillsButton_3.setText(QCoreApplication.translate("Form", u"Bills", None))
        self.notiButton_4.setText(QCoreApplication.translate("Form", u"Notification", None))
        self.label_32.setText("")
        self.bellicon_4.setText("")
        self.goGoalButton_4.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.goDashboardButton_4.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_79.setText("")
        self.label_80.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.closeButton_6.setText("")
        self.label_85.setText("")
        self.goAccountButton_4.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_98.setText("")
        self.label_99.setText("")
        self.label_100.setText("")
        self.label_101.setText("")
        self.goTransButton_4.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_102.setText("")
        self.label_23.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Goal Name", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Progress", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Goal Amount", None))
        self.addButton_3.setText(QCoreApplication.translate("Form", u"Add a Transaction / Goal", None))
        self.goBillsButton_4.setText(QCoreApplication.translate("Form", u"Bills", None))
        self.notiButton_5.setText(QCoreApplication.translate("Form", u"Notification", None))
        self.label_136.setText("")
        self.bellicon_5.setText("")
        self.goGoalButton_5.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.goDashboardButton_5.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_81.setText("")
        self.label_82.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.closeButton_7.setText("")
        self.label_86.setText("")
        self.goAccountButton_5.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_103.setText("")
        self.label_104.setText("")
        self.label_105.setText("")
        self.label_106.setText("")
        self.goTransButton_5.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_107.setText("")
        self.label_28.setText(QCoreApplication.translate("Form", u"User", None))
        self.logoutButton.setText(QCoreApplication.translate("Form", u"Logout", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"Username", None))
        self.addButton_4.setText(QCoreApplication.translate("Form", u"Add a Transaction / Goal", None))
        self.bugetField.setText("")
        self.label_42.setText(QCoreApplication.translate("Form", u"Weekly Budget", None))
        self.editBudgetButton.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.label_134.setText(QCoreApplication.translate("Form", u"Total Income", None))
        self.ttincome.setText("")
        self.label_135.setText(QCoreApplication.translate("Form", u"Total Expense", None))
        self.ttexpense.setText("")
        self.goBillsButton_5.setText(QCoreApplication.translate("Form", u"Bills", None))
        self.ttBalance.setText("")
        self.label_255.setText(QCoreApplication.translate("Form", u"Total Balance", None))
        self.notiButton_6.setText(QCoreApplication.translate("Form", u"Notification", None))
        self.label_137.setText("")
        self.bellicon_6.setText("")
        self.goGoalButton_7.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.goDashboardButton_7.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_115.setText("")
        self.label_116.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.closeButton_9.setText("")
        self.label_117.setText("")
        self.goAccountButton_7.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_118.setText("")
        self.label_119.setText("")
        self.label_120.setText("")
        self.label_121.setText("")
        self.goTransButton_7.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_122.setText("")
        self.label_37.setText(QCoreApplication.translate("Form", u"Transaction Detail", None))
        self.addButton_5.setText(QCoreApplication.translate("Form", u"Add a Transaction / Goal", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"Transaction Name", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Transaction Amount", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Description", None))
        self.label_67.setText(QCoreApplication.translate("Form", u"Category", None))
        self.EditButton.setText(QCoreApplication.translate("Form", u"Edit ", None))
        self.SaveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.DeleteTransButton.setText(QCoreApplication.translate("Form", u"Remove this Transaction", None))
        self.label_68.setText(QCoreApplication.translate("Form", u"Enter your password:", None))
        self.goBillsButton_6.setText(QCoreApplication.translate("Form", u"Bills", None))
        self.notiButton_7.setText(QCoreApplication.translate("Form", u"Notification", None))
        self.label_138.setText("")
        self.bellicon_7.setText("")
        self.goGoalButton_8.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.goDashboardButton_8.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_123.setText("")
        self.label_124.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.closeButton_10.setText("")
        self.label_125.setText("")
        self.goAccountButton_8.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_126.setText("")
        self.label_127.setText("")
        self.label_128.setText("")
        self.label_129.setText("")
        self.goTransButton_8.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_130.setText("")
        self.label_43.setText(QCoreApplication.translate("Form", u"Goal Detail", None))
        self.addButton_6.setText(QCoreApplication.translate("Form", u"Add a Transaction / Goal", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"Goal Name", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"Goal Amount", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"Description", None))
        self.EditButton_2.setText(QCoreApplication.translate("Form", u"Edit ", None))
        self.SaveButton_2.setText(QCoreApplication.translate("Form", u"Save", None))
        self.DeleteGoalButton.setText(QCoreApplication.translate("Form", u"Remove this Goal", None))
        self.label_71.setText(QCoreApplication.translate("Form", u"Enter your password:", None))
        self.label_73.setText("")
        self.label_72.setText(QCoreApplication.translate("Form", u"Funded", None))
        self.GoalBalanceLabel_2.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_70.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.label_74.setText("")
        self.currentBalanceLabel_3.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_87.setText("")
        self.label_109.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.label_110.setText(QCoreApplication.translate("Form", u"Funded", None))
        self.label_111.setText("")
        self.label_27.setText(QCoreApplication.translate("Form", u"Goal progress", None))
        self.GoalBalanceLabel_4.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_112.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.label_113.setText(QCoreApplication.translate("Form", u"Short Of", None))
        self.label_114.setText("")
        self.label_131.setText("")
        self.label_132.setText(QCoreApplication.translate("Form", u"Goal Total", None))
        self.label_133.setText(QCoreApplication.translate("Form", u"\u0e3f", None))
        self.GoalBalanceLabel_5.setText(QCoreApplication.translate("Form", u"0", None))
        self.FundGoalButton.setText(QCoreApplication.translate("Form", u"Fund", None))
        self.deFundGoalButton.setText(QCoreApplication.translate("Form", u"Defund", None))
        self.goBillsButton_7.setText(QCoreApplication.translate("Form", u"Bills", None))
        self.notiButton_8.setText(QCoreApplication.translate("Form", u"Notification", None))
        self.label_139.setText("")
        self.bellicon_8.setText("")
        self.goGoalButton_14.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.goDashboardButton_14.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_214.setText("")
        self.label_215.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.closeButton_16.setText("")
        self.label_216.setText("")
        self.goAccountButton_14.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_217.setText("")
        self.label_218.setText("")
        self.label_219.setText("")
        self.label_220.setText("")
        self.goTransButton_14.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_221.setText("")
        self.label_226.setText(QCoreApplication.translate("Form", u"New Bill", None))
        self.label_227.setText(QCoreApplication.translate("Form", u"Bill Name", None))
        self.label_228.setText(QCoreApplication.translate("Form", u"Bill Amount", None))
        self.label_229.setText(QCoreApplication.translate("Form", u"Description", None))
        self.saveBillsButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.goBillsButton_14.setText(QCoreApplication.translate("Form", u"Bills", None))
        self.label_254.setText(QCoreApplication.translate("Form", u"Due Date", None))
        self.notiButton_9.setText(QCoreApplication.translate("Form", u"Notification", None))
        self.label_140.setText("")
        self.bellicon_9.setText("")
        self.goGoalButton_16.setText(QCoreApplication.translate("Form", u"Goals", None))
        self.goDashboardButton_16.setText(QCoreApplication.translate("Form", u"Dashboard", None))
        self.label_240.setText("")
        self.label_241.setText(QCoreApplication.translate("Form", u"Money Mate", None))
        self.closeButton_18.setText("")
        self.label_242.setText("")
        self.goAccountButton_16.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_243.setText("")
        self.label_244.setText("")
        self.label_245.setText("")
        self.label_246.setText("")
        self.goTransButton_16.setText(QCoreApplication.translate("Form", u"Transactions", None))
        self.label_247.setText("")
        self.label_248.setText(QCoreApplication.translate("Form", u"Bill Detail", None))
        self.addButton_13.setText(QCoreApplication.translate("Form", u"Add a Transaction / Goal", None))
        self.label_249.setText(QCoreApplication.translate("Form", u"Bill Name", None))
        self.label_250.setText(QCoreApplication.translate("Form", u"Due Date", None))
        self.label_251.setText(QCoreApplication.translate("Form", u"Description", None))
        self.label_252.setText(QCoreApplication.translate("Form", u"Bill Amount", None))
        self.EditButton_4.setText(QCoreApplication.translate("Form", u"Edit ", None))
        self.SaveButton_4.setText(QCoreApplication.translate("Form", u"Save", None))
        self.deleteBillsButton.setText(QCoreApplication.translate("Form", u"Remove this Transaction", None))
        self.label_253.setText(QCoreApplication.translate("Form", u"Enter your password:", None))
        self.goBillsButton_16.setText(QCoreApplication.translate("Form", u"Bills", None))
        self.notiButton_10.setText(QCoreApplication.translate("Form", u"Notification", None))
        self.label_141.setText("")
        self.bellicon_10.setText("")
    # retranslateUi

