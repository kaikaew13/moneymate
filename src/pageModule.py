# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginPage.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QSizePolicy,
    QStackedWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
import img_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1024, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1021, 771))
        self.loginPage = QWidget()
        self.loginPage.setObjectName("loginPage")
        self.widget = QWidget(self.loginPage)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(30, 30, 961, 731))
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(20, 80, 541, 561))
        self.label.setStyleSheet(
            "background-image: url(:/pics/images/Summary.png);\n"
            "border-top-left-radius: 50px;"
        )
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(540, 80, 411, 561))
        self.label_2.setStyleSheet(
            "background-color:rgba(255,255,255,255);\n"
            "border-bottom-right-radius: 50px;"
        )
        self.Signin_Label = QLabel(self.widget)
        self.Signin_Label.setObjectName("Signin_Label")
        self.Signin_Label.setGeometry(QRect(670, 130, 131, 51))
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.Signin_Label.setFont(font)
        self.Signin_Label.setStyleSheet("color:rgba(0,0,0,150);\n" "")
        self.lineEditUserLogin = QLineEdit(self.widget)
        self.lineEditUserLogin.setObjectName("lineEditUserLogin")
        self.lineEditUserLogin.setGeometry(QRect(600, 250, 311, 51))
        font1 = QFont()
        font1.setPointSize(18)
        self.lineEditUserLogin.setFont(font1)
        self.lineEditUserLogin.setStyleSheet(
            "background-color:rgba(0,0,0,0);\n"
            "border:none;\n"
            "border-bottom: 2px solid rgba(46,82,101,200);\n"
            "color:rgba(0,0,0,100);\n"
            "padding-bottom:7px;"
        )
        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setGeometry(QRect(600, 440, 311, 71))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.loginButton.setFont(font2)
        self.loginButton.setStyleSheet(
            "QPushButton#loginButton {\n"
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
            ""
        )
        self.GoRegisterButton = QPushButton(self.widget)
        self.GoRegisterButton.setObjectName("GoRegisterButton")
        self.GoRegisterButton.setGeometry(QRect(600, 530, 311, 71))
        self.GoRegisterButton.setFont(font2)
        self.GoRegisterButton.setStyleSheet(
            "QPushButton#GoRegisterButton {\n"
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
            ""
        )
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(20, 120, 521, 81))
        self.label_4.setStyleSheet("background-color: rgba(0,0,0,75);")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(30, 130, 501, 61))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;\n" "")
        self.lineEditPassLogin = QLineEdit(self.widget)
        self.lineEditPassLogin.setObjectName("lineEditPassLogin")
        self.lineEditPassLogin.setGeometry(QRect(600, 350, 311, 51))
        self.lineEditPassLogin.setFont(font1)
        self.lineEditPassLogin.setStyleSheet(
            "background-color:rgba(0,0,0,0);\n"
            "border:none;\n"
            "border-bottom: 2px solid rgba(46,82,101,200);\n"
            "color:rgba(0,0,0,100);\n"
            "padding-bottom:7px;"
        )
        self.lineEditPassLogin.setEchoMode(QLineEdit.Password)
        self.closeButton = QPushButton(self.widget)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setGeometry(QRect(910, 90, 31, 32))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy1)
        self.closeButton.setBaseSize(QSize(0, 0))
        self.closeButton.setStyleSheet(
            "QPushButton#closeButton {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#closeButton:hover {\n"
            "    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
            "    border-radius: 50%; /* set the border radius to create a circle */\n"
            "}\n"
            ""
        )
        icon = QIcon()
        icon.addFile(":/pics/images/x-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon)
        self.stackedWidget.addWidget(self.loginPage)
        self.registerPage = QWidget()
        self.registerPage.setObjectName("registerPage")
        self.widget_2 = QWidget(self.registerPage)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setGeometry(QRect(30, 30, 961, 731))
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(20, 80, 541, 561))
        self.label_6.setStyleSheet(
            "background-image: url(:/pics/images/Summary.png);\n"
            "border-top-left-radius: 50px;"
        )
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(540, 80, 411, 561))
        self.label_7.setStyleSheet(
            "background-color:rgba(255,255,255,255);\n"
            "border-bottom-right-radius: 50px;"
        )
        self.Reigstration_Label = QLabel(self.widget_2)
        self.Reigstration_Label.setObjectName("Reigstration_Label")
        self.Reigstration_Label.setGeometry(QRect(630, 130, 241, 51))
        self.Reigstration_Label.setFont(font)
        self.Reigstration_Label.setStyleSheet("color:rgba(0,0,0,150);\n" "")
        self.lineEditUserRegister = QLineEdit(self.widget_2)
        self.lineEditUserRegister.setObjectName("lineEditUserRegister")
        self.lineEditUserRegister.setGeometry(QRect(600, 210, 311, 51))
        self.lineEditUserRegister.setFont(font1)
        self.lineEditUserRegister.setStyleSheet(
            "background-color:rgba(0,0,0,0);\n"
            "border:none;\n"
            "border-bottom: 2px solid rgba(46,82,101,200);\n"
            "color:rgba(0,0,0,100);\n"
            "padding-bottom:7px;"
        )
        self.RegisterButton = QPushButton(self.widget_2)
        self.RegisterButton.setObjectName("RegisterButton")
        self.RegisterButton.setGeometry(QRect(600, 450, 311, 71))
        self.RegisterButton.setFont(font2)
        self.RegisterButton.setStyleSheet(
            "QPushButton#RegisterButton {\n"
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
            ""
        )
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(20, 120, 521, 81))
        self.label_9.setStyleSheet("background-color: rgba(0,0,0,75);")
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(QRect(30, 130, 501, 61))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: white;\n" "")
        self.lineEditUserPassword = QLineEdit(self.widget_2)
        self.lineEditUserPassword.setObjectName("lineEditUserPassword")
        self.lineEditUserPassword.setGeometry(QRect(600, 300, 311, 51))
        self.lineEditUserPassword.setFont(font1)
        self.lineEditUserPassword.setStyleSheet(
            "background-color:rgba(0,0,0,0);\n"
            "border:none;\n"
            "border-bottom: 2px solid rgba(46,82,101,200);\n"
            "color:rgba(0,0,0,100);\n"
            "padding-bottom:7px;"
        )
        self.lineEditUserPassword.setEchoMode(QLineEdit.Password)
        self.closeButton_2 = QPushButton(self.widget_2)
        self.closeButton_2.setObjectName("closeButton_2")
        self.closeButton_2.setGeometry(QRect(910, 90, 31, 32))
        sizePolicy1.setHeightForWidth(
            self.closeButton_2.sizePolicy().hasHeightForWidth()
        )
        self.closeButton_2.setSizePolicy(sizePolicy1)
        self.closeButton_2.setBaseSize(QSize(0, 0))
        self.closeButton_2.setStyleSheet(
            "QPushButton#closeButton_2 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#closeButton_2:hover {\n"
            "    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
            "    border-radius: 50%; /* set the border radius to create a circle */\n"
            "}\n"
            ""
        )
        self.closeButton_2.setIcon(icon)
        self.lineEditUserPassword_2 = QLineEdit(self.widget_2)
        self.lineEditUserPassword_2.setObjectName("lineEditUserPassword_2")
        self.lineEditUserPassword_2.setGeometry(QRect(600, 370, 311, 51))
        self.lineEditUserPassword_2.setFont(font1)
        self.lineEditUserPassword_2.setStyleSheet(
            "background-color:rgba(0,0,0,0);\n"
            "border:none;\n"
            "border-bottom: 2px solid rgba(46,82,101,200);\n"
            "color:rgba(0,0,0,100);\n"
            "padding-bottom:7px;"
        )
        self.lineEditUserPassword_2.setEchoMode(QLineEdit.Password)
        self.goSigninButton = QPushButton(self.widget_2)
        self.goSigninButton.setObjectName("goSigninButton")
        self.goSigninButton.setGeometry(QRect(600, 540, 311, 71))
        self.goSigninButton.setFont(font2)
        self.goSigninButton.setStyleSheet(
            "QPushButton#goSigninButton {\n"
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
            ""
        )
        self.stackedWidget.addWidget(self.registerPage)
        self.dashboardPage = QWidget()
        self.dashboardPage.setObjectName("dashboardPage")
        self.widget_3 = QWidget(self.dashboardPage)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 1021, 771))
        self.label_29 = QLabel(self.widget_3)
        self.label_29.setObjectName("label_29")
        self.label_29.setGeometry(QRect(320, 205, 171, 21))
        font3 = QFont()
        font3.setPointSize(20)
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet("color: rgb(0,0,0);")
        self.line_13 = QFrame(self.widget_3)
        self.line_13.setObjectName("line_13")
        self.line_13.setGeometry(QRect(290, 630, 751, 16))
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)
        self.CatLabel5 = QLabel(self.widget_3)
        self.CatLabel5.setObjectName("CatLabel5")
        self.CatLabel5.setGeometry(QRect(630, 530, 81, 16))
        self.CatLabel5.setStyleSheet("color: rgb(0,0,0);")
        self.AmountLabel1 = QLabel(self.widget_3)
        self.AmountLabel1.setObjectName("AmountLabel1")
        self.AmountLabel1.setGeometry(QRect(450, 370, 91, 16))
        self.AmountLabel1.setStyleSheet("color: rgb(0,0,0);")
        self.label_39 = QLabel(self.widget_3)
        self.label_39.setObjectName("label_39")
        self.label_39.setGeometry(QRect(570, 205, 171, 21))
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet("color: rgb(0,0,0);")
        self.goGoalButton = QPushButton(self.widget_3)
        self.goGoalButton.setObjectName("goGoalButton")
        self.goGoalButton.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton.setFont(font3)
        self.goGoalButton.setStyleSheet(
            "QPushButton#goGoalButton {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goGoalButton:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.label_40 = QLabel(self.widget_3)
        self.label_40.setObjectName("label_40")
        self.label_40.setGeometry(QRect(300, 200, 16, 31))
        self.label_40.setFont(font3)
        self.label_40.setStyleSheet("color: rgb(0,0,0);")
        self.label_41 = QLabel(self.widget_3)
        self.label_41.setObjectName("label_41")
        self.label_41.setGeometry(QRect(540, 176, 221, 61))
        self.label_41.setStyleSheet("background-color: rgb(255,255,255);")
        self.goDashboardButton = QPushButton(self.widget_3)
        self.goDashboardButton.setObjectName("goDashboardButton")
        self.goDashboardButton.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton.setFont(font3)
        self.goDashboardButton.setStyleSheet(
            "QPushButton#goDashboardButton {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goDashboardButton:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}\n"
            ""
        )
        self.DesLabel9 = QLabel(self.widget_3)
        self.DesLabel9.setObjectName("DesLabel9")
        self.DesLabel9.setGeometry(QRect(860, 690, 81, 16))
        self.DesLabel9.setStyleSheet("color: rgb(0,0,0);")
        self.label_42 = QLabel(self.widget_3)
        self.label_42.setObjectName("label_42")
        self.label_42.setGeometry(QRect(320, 330, 60, 16))
        font4 = QFont()
        font4.setPointSize(14)
        self.label_42.setFont(font4)
        self.label_42.setStyleSheet("color: rgb(148,148,148);")
        self.label_43 = QLabel(self.widget_3)
        self.label_43.setObjectName("label_43")
        self.label_43.setGeometry(QRect(630, 330, 60, 16))
        self.label_43.setFont(font4)
        self.label_43.setStyleSheet("color: rgb(148,148,148);")
        self.DesLabel8 = QLabel(self.widget_3)
        self.DesLabel8.setObjectName("DesLabel8")
        self.DesLabel8.setGeometry(QRect(860, 650, 81, 16))
        self.DesLabel8.setStyleSheet("color: rgb(0,0,0);")
        self.DateLabel5 = QLabel(self.widget_3)
        self.DateLabel5.setObjectName("DateLabel5")
        self.DateLabel5.setGeometry(QRect(310, 530, 81, 16))
        self.DateLabel5.setStyleSheet("color: rgb(0,0,0);")
        self.label_44 = QLabel(self.widget_3)
        self.label_44.setObjectName("label_44")
        self.label_44.setGeometry(QRect(300, 180, 111, 16))
        font5 = QFont()
        font5.setBold(True)
        self.label_44.setFont(font5)
        self.label_44.setStyleSheet("color: rgb(148,148,148);")
        self.DateLabel2 = QLabel(self.widget_3)
        self.DateLabel2.setObjectName("DateLabel2")
        self.DateLabel2.setGeometry(QRect(310, 410, 81, 16))
        self.DateLabel2.setStyleSheet("color: rgb(0,0,0);")
        self.CatLabel7 = QLabel(self.widget_3)
        self.CatLabel7.setObjectName("CatLabel7")
        self.CatLabel7.setGeometry(QRect(630, 610, 81, 16))
        self.CatLabel7.setStyleSheet("color: rgb(0,0,0);")
        self.AmountLabel6 = QLabel(self.widget_3)
        self.AmountLabel6.setObjectName("AmountLabel6")
        self.AmountLabel6.setGeometry(QRect(450, 570, 91, 16))
        self.AmountLabel6.setStyleSheet("color: rgb(0,0,0);")
        self.AmountLabel9 = QLabel(self.widget_3)
        self.AmountLabel9.setObjectName("AmountLabel9")
        self.AmountLabel9.setGeometry(QRect(450, 690, 91, 16))
        self.AmountLabel9.setStyleSheet("color: rgb(0,0,0);")
        self.DesLabel4 = QLabel(self.widget_3)
        self.DesLabel4.setObjectName("DesLabel4")
        self.DesLabel4.setGeometry(QRect(860, 490, 81, 16))
        self.DesLabel4.setStyleSheet("color: rgb(0,0,0);")
        self.DateLabel6 = QLabel(self.widget_3)
        self.DateLabel6.setObjectName("DateLabel6")
        self.DateLabel6.setGeometry(QRect(310, 570, 81, 16))
        self.DateLabel6.setStyleSheet("color: rgb(0,0,0);")
        self.DateLabel1 = QLabel(self.widget_3)
        self.DateLabel1.setObjectName("DateLabel1")
        self.DateLabel1.setGeometry(QRect(310, 370, 81, 16))
        self.DateLabel1.setStyleSheet("color: rgb(0,0,0);")
        self.CatLabel3 = QLabel(self.widget_3)
        self.CatLabel3.setObjectName("CatLabel3")
        self.CatLabel3.setGeometry(QRect(630, 450, 81, 16))
        self.CatLabel3.setStyleSheet("color: rgb(0,0,0);")
        self.label_45 = QLabel(self.widget_3)
        self.label_45.setObjectName("label_45")
        self.label_45.setGeometry(QRect(290, 220, 221, 21))
        self.label_45.setStyleSheet("background-color: rgb(178,241,149);\n" "")
        self.label_46 = QLabel(self.widget_3)
        self.label_46.setObjectName("label_46")
        self.label_46.setGeometry(QRect(460, 330, 60, 16))
        self.label_46.setFont(font4)
        self.label_46.setStyleSheet("color: rgb(148,148,148);")
        self.label_47 = QLabel(self.widget_3)
        self.label_47.setObjectName("label_47")
        self.label_47.setGeometry(QRect(20, 170, 31, 31))
        self.label_47.setStyleSheet("")
        self.label_47.setPixmap(QPixmap(":/pics/images/user.png"))
        self.label_47.setScaledContents(True)
        self.DateLabel3 = QLabel(self.widget_3)
        self.DateLabel3.setObjectName("DateLabel3")
        self.DateLabel3.setGeometry(QRect(310, 450, 81, 16))
        self.DateLabel3.setStyleSheet("color: rgb(0,0,0);")
        self.CatLabel8 = QLabel(self.widget_3)
        self.CatLabel8.setObjectName("CatLabel8")
        self.CatLabel8.setGeometry(QRect(630, 650, 81, 16))
        self.CatLabel8.setStyleSheet("color: rgb(0,0,0);")
        self.CatLabel9 = QLabel(self.widget_3)
        self.CatLabel9.setObjectName("CatLabel9")
        self.CatLabel9.setGeometry(QRect(630, 690, 81, 16))
        self.CatLabel9.setStyleSheet("color: rgb(0,0,0);")
        self.line_14 = QFrame(self.widget_3)
        self.line_14.setObjectName("line_14")
        self.line_14.setGeometry(QRect(290, 750, 751, 16))
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)
        self.label_48 = QLabel(self.widget_3)
        self.label_48.setObjectName("label_48")
        self.label_48.setGeometry(QRect(100, 60, 121, 21))
        self.label_48.setFont(font2)
        self.label_48.setStyleSheet("color: white;\n" "")
        self.AmountLabel2 = QLabel(self.widget_3)
        self.AmountLabel2.setObjectName("AmountLabel2")
        self.AmountLabel2.setGeometry(QRect(450, 410, 91, 16))
        self.AmountLabel2.setStyleSheet("color: rgb(0,0,0);")
        self.DesLabel6 = QLabel(self.widget_3)
        self.DesLabel6.setObjectName("DesLabel6")
        self.DesLabel6.setGeometry(QRect(860, 570, 81, 16))
        self.DesLabel6.setStyleSheet("color: rgb(0,0,0);")
        self.label_49 = QLabel(self.widget_3)
        self.label_49.setObjectName("label_49")
        self.label_49.setGeometry(QRect(790, 176, 221, 61))
        self.label_49.setStyleSheet("background-color: rgb(255,255,255);")
        self.label_50 = QLabel(self.widget_3)
        self.label_50.setObjectName("label_50")
        self.label_50.setGeometry(QRect(550, 180, 121, 16))
        self.label_50.setFont(font5)
        self.label_50.setStyleSheet("color: rgb(148,148,148);")
        self.CatLabel4 = QLabel(self.widget_3)
        self.CatLabel4.setObjectName("CatLabel4")
        self.CatLabel4.setGeometry(QRect(630, 490, 81, 16))
        self.CatLabel4.setStyleSheet("color: rgb(0,0,0);")
        self.line_15 = QFrame(self.widget_3)
        self.line_15.setObjectName("line_15")
        self.line_15.setGeometry(QRect(290, 670, 751, 16))
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)
        self.line_16 = QFrame(self.widget_3)
        self.line_16.setObjectName("line_16")
        self.line_16.setGeometry(QRect(290, 590, 751, 16))
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)
        self.label_51 = QLabel(self.widget_3)
        self.label_51.setObjectName("label_51")
        self.label_51.setGeometry(QRect(850, 330, 81, 16))
        self.label_51.setFont(font4)
        self.label_51.setStyleSheet("color: rgb(148,148,148);")
        self.label_52 = QLabel(self.widget_3)
        self.label_52.setObjectName("label_52")
        self.label_52.setGeometry(QRect(800, 200, 16, 31))
        self.label_52.setFont(font3)
        self.label_52.setStyleSheet("color: rgb(0,0,0);")
        self.AmountLabel5 = QLabel(self.widget_3)
        self.AmountLabel5.setObjectName("AmountLabel5")
        self.AmountLabel5.setGeometry(QRect(450, 530, 91, 16))
        self.AmountLabel5.setStyleSheet("color: rgb(0,0,0);")
        self.line_17 = QFrame(self.widget_3)
        self.line_17.setObjectName("line_17")
        self.line_17.setGeometry(QRect(290, 510, 751, 16))
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)
        self.DateLabel4 = QLabel(self.widget_3)
        self.DateLabel4.setObjectName("DateLabel4")
        self.DateLabel4.setGeometry(QRect(310, 490, 81, 16))
        self.DateLabel4.setStyleSheet("color: rgb(0,0,0);")
        self.DesLabel1 = QLabel(self.widget_3)
        self.DesLabel1.setObjectName("DesLabel1")
        self.DesLabel1.setGeometry(QRect(860, 370, 81, 16))
        self.DesLabel1.setStyleSheet("color: rgb(0,0,0);")
        self.DateLabel10 = QLabel(self.widget_3)
        self.DateLabel10.setObjectName("DateLabel10")
        self.DateLabel10.setGeometry(QRect(310, 730, 81, 16))
        self.DateLabel10.setStyleSheet("color: rgb(0,0,0);")
        self.closeButton_3 = QPushButton(self.widget_3)
        self.closeButton_3.setObjectName("closeButton_3")
        self.closeButton_3.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(
            self.closeButton_3.sizePolicy().hasHeightForWidth()
        )
        self.closeButton_3.setSizePolicy(sizePolicy1)
        self.closeButton_3.setBaseSize(QSize(0, 0))
        self.closeButton_3.setStyleSheet(
            "QPushButton#closeButton_3 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#closeButton_3:hover {\n"
            "    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
            "    border-radius: 50%; /* set the border radius to create a circle */\n"
            "}\n"
            ""
        )
        self.closeButton_3.setIcon(icon)
        self.label_53 = QLabel(self.widget_3)
        self.label_53.setObjectName("label_53")
        self.label_53.setGeometry(QRect(540, 220, 221, 21))
        self.label_53.setStyleSheet("background-color: rgb(164,202,247);\n" "")
        self.line_18 = QFrame(self.widget_3)
        self.line_18.setObjectName("line_18")
        self.line_18.setGeometry(QRect(290, 430, 751, 16))
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)
        self.label_54 = QLabel(self.widget_3)
        self.label_54.setObjectName("label_54")
        self.label_54.setGeometry(QRect(800, 180, 111, 16))
        self.label_54.setFont(font5)
        self.label_54.setStyleSheet("color: rgb(148,148,148);")
        self.CatLabel6 = QLabel(self.widget_3)
        self.CatLabel6.setObjectName("CatLabel6")
        self.CatLabel6.setGeometry(QRect(630, 570, 81, 16))
        self.CatLabel6.setStyleSheet("color: rgb(0,0,0);")
        self.label_55 = QLabel(self.widget_3)
        self.label_55.setObjectName("label_55")
        self.label_55.setGeometry(QRect(0, 0, 1071, 101))
        self.label_55.setStyleSheet("background-color: rgb(81,74,248);")
        self.AmountLabel7 = QLabel(self.widget_3)
        self.AmountLabel7.setObjectName("AmountLabel7")
        self.AmountLabel7.setGeometry(QRect(450, 610, 91, 16))
        self.AmountLabel7.setStyleSheet("color: rgb(0,0,0);")
        self.label_56 = QLabel(self.widget_3)
        self.label_56.setObjectName("label_56")
        self.label_56.setGeometry(QRect(300, 120, 241, 21))
        font6 = QFont()
        font6.setPointSize(22)
        self.label_56.setFont(font6)
        self.label_56.setStyleSheet("color: rgb(0,0,0);")
        self.DesLabel2 = QLabel(self.widget_3)
        self.DesLabel2.setObjectName("DesLabel2")
        self.DesLabel2.setGeometry(QRect(860, 410, 81, 16))
        self.DesLabel2.setStyleSheet("color: rgb(0,0,0);")
        self.label_57 = QLabel(self.widget_3)
        self.label_57.setObjectName("label_57")
        self.label_57.setGeometry(QRect(790, 220, 221, 21))
        self.label_57.setStyleSheet("background-color: rgb(213,131,131);\n" "")
        self.DateLabel8 = QLabel(self.widget_3)
        self.DateLabel8.setObjectName("DateLabel8")
        self.DateLabel8.setGeometry(QRect(310, 650, 81, 16))
        self.DateLabel8.setStyleSheet("color: rgb(0,0,0);")
        self.label_58 = QLabel(self.widget_3)
        self.label_58.setObjectName("label_58")
        self.label_58.setGeometry(QRect(820, 205, 171, 21))
        self.label_58.setFont(font3)
        self.label_58.setStyleSheet("color: rgb(0,0,0);")
        self.CatLabel10 = QLabel(self.widget_3)
        self.CatLabel10.setObjectName("CatLabel10")
        self.CatLabel10.setGeometry(QRect(630, 730, 81, 16))
        self.CatLabel10.setStyleSheet("color: rgb(0,0,0);")
        self.label_59 = QLabel(self.widget_3)
        self.label_59.setObjectName("label_59")
        self.label_59.setGeometry(QRect(550, 200, 16, 31))
        self.label_59.setFont(font3)
        self.label_59.setStyleSheet("color: rgb(0,0,0);")
        self.AmountLabel3 = QLabel(self.widget_3)
        self.AmountLabel3.setObjectName("AmountLabel3")
        self.AmountLabel3.setGeometry(QRect(450, 450, 91, 16))
        self.AmountLabel3.setStyleSheet("color: rgb(0,0,0);")
        self.CatLabel1 = QLabel(self.widget_3)
        self.CatLabel1.setObjectName("CatLabel1")
        self.CatLabel1.setGeometry(QRect(630, 370, 81, 16))
        self.CatLabel1.setStyleSheet("color: rgb(0,0,0);")
        self.CatLabel2 = QLabel(self.widget_3)
        self.CatLabel2.setObjectName("CatLabel2")
        self.CatLabel2.setGeometry(QRect(630, 410, 81, 16))
        self.CatLabel2.setStyleSheet("color: rgb(0,0,0);")
        self.goAccountButton = QPushButton(self.widget_3)
        self.goAccountButton.setObjectName("goAccountButton")
        self.goAccountButton.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton.setFont(font3)
        self.goAccountButton.setStyleSheet(
            "QPushButton#goAccountButton {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goAccountButton:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.line_19 = QFrame(self.widget_3)
        self.line_19.setObjectName("line_19")
        self.line_19.setGeometry(QRect(290, 350, 751, 16))
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)
        self.DateLabel9 = QLabel(self.widget_3)
        self.DateLabel9.setObjectName("DateLabel9")
        self.DateLabel9.setGeometry(QRect(310, 690, 81, 16))
        self.DateLabel9.setStyleSheet("color: rgb(0,0,0);")
        self.label_60 = QLabel(self.widget_3)
        self.label_60.setObjectName("label_60")
        self.label_60.setGeometry(QRect(0, 100, 1021, 701))
        self.label_60.setStyleSheet("background-color: rgb(250,250,250);")
        self.label_61 = QLabel(self.widget_3)
        self.label_61.setObjectName("label_61")
        self.label_61.setGeometry(QRect(20, 290, 31, 31))
        self.label_61.setStyleSheet("")
        self.label_61.setPixmap(QPixmap(":/pics/images/goal.png"))
        self.label_61.setScaledContents(True)
        self.label_62 = QLabel(self.widget_3)
        self.label_62.setObjectName("label_62")
        self.label_62.setGeometry(QRect(20, 230, 31, 31))
        self.label_62.setStyleSheet("")
        self.label_62.setPixmap(QPixmap(":/pics/images/trans.png"))
        self.label_62.setScaledContents(True)
        self.tabsButton = QPushButton(self.widget_3)
        self.tabsButton.setObjectName("tabsButton")
        self.tabsButton.setGeometry(QRect(50, 50, 41, 41))
        self.tabsButton.setStyleSheet(
            "QPushButton#tabsButton {\n"
            "    border: none;\n"
            "    background-color: rgb(81,74,248);\n"
            "   qproperty-iconSize: 40px;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#tabsButton:hover {\n"
            "    background-color: rgb(81,74,170);\n"
            "}\n"
            ""
        )
        icon1 = QIcon()
        icon1.addFile(":/pics/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabsButton.setIcon(icon1)
        self.line_20 = QFrame(self.widget_3)
        self.line_20.setObjectName("line_20")
        self.line_20.setGeometry(QRect(290, 550, 751, 16))
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)
        self.AmountLabel10 = QLabel(self.widget_3)
        self.AmountLabel10.setObjectName("AmountLabel10")
        self.AmountLabel10.setGeometry(QRect(450, 730, 101, 16))
        self.AmountLabel10.setStyleSheet("color: rgb(0,0,0);")
        self.AmountLabel8 = QLabel(self.widget_3)
        self.AmountLabel8.setObjectName("AmountLabel8")
        self.AmountLabel8.setGeometry(QRect(450, 650, 91, 16))
        self.AmountLabel8.setStyleSheet("color: rgb(0,0,0);")
        self.label_63 = QLabel(self.widget_3)
        self.label_63.setObjectName("label_63")
        self.label_63.setGeometry(QRect(0, 100, 251, 701))
        self.label_63.setStyleSheet("background-color: rgb(255,255,255);")
        self.DesLabel3 = QLabel(self.widget_3)
        self.DesLabel3.setObjectName("DesLabel3")
        self.DesLabel3.setGeometry(QRect(860, 450, 81, 16))
        self.DesLabel3.setStyleSheet("color: rgb(0,0,0);")
        self.DesLabel10 = QLabel(self.widget_3)
        self.DesLabel10.setObjectName("DesLabel10")
        self.DesLabel10.setGeometry(QRect(860, 730, 81, 16))
        self.DesLabel10.setStyleSheet("color: rgb(0,0,0);")
        self.DesLabel7 = QLabel(self.widget_3)
        self.DesLabel7.setObjectName("DesLabel7")
        self.DesLabel7.setGeometry(QRect(860, 610, 81, 16))
        self.DesLabel7.setStyleSheet("color: rgb(0,0,0);")
        self.DateLabel7 = QLabel(self.widget_3)
        self.DateLabel7.setObjectName("DateLabel7")
        self.DateLabel7.setGeometry(QRect(310, 610, 81, 16))
        self.DateLabel7.setStyleSheet("color: rgb(0,0,0);")
        self.line_21 = QFrame(self.widget_3)
        self.line_21.setObjectName("line_21")
        self.line_21.setGeometry(QRect(290, 470, 751, 16))
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)
        self.goTransButton = QPushButton(self.widget_3)
        self.goTransButton.setObjectName("goTransButton")
        self.goTransButton.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton.setFont(font3)
        self.goTransButton.setStyleSheet(
            "QPushButton#goTransButton {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goTransButton:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.label_64 = QLabel(self.widget_3)
        self.label_64.setObjectName("label_64")
        self.label_64.setGeometry(QRect(290, 176, 221, 61))
        self.label_64.setStyleSheet("background-color: rgb(255,255,255);")
        self.AmountLabel4 = QLabel(self.widget_3)
        self.AmountLabel4.setObjectName("AmountLabel4")
        self.AmountLabel4.setGeometry(QRect(450, 490, 91, 16))
        self.AmountLabel4.setStyleSheet("color: rgb(0,0,0);")
        self.DesLabel5 = QLabel(self.widget_3)
        self.DesLabel5.setObjectName("DesLabel5")
        self.DesLabel5.setGeometry(QRect(860, 530, 81, 16))
        self.DesLabel5.setStyleSheet("color: rgb(0,0,0);")
        self.label_65 = QLabel(self.widget_3)
        self.label_65.setObjectName("label_65")
        self.label_65.setGeometry(QRect(290, 270, 201, 21))
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(True)
        self.label_65.setFont(font7)
        self.label_65.setStyleSheet("color: rgb(0,0,0);")
        self.line_22 = QFrame(self.widget_3)
        self.line_22.setObjectName("line_22")
        self.line_22.setGeometry(QRect(290, 390, 751, 16))
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)
        self.label_66 = QLabel(self.widget_3)
        self.label_66.setObjectName("label_66")
        self.label_66.setGeometry(QRect(20, 110, 31, 31))
        self.label_66.setStyleSheet("background-image: url(:/pics/images/home.png);")
        self.line_23 = QFrame(self.widget_3)
        self.line_23.setObjectName("line_23")
        self.line_23.setGeometry(QRect(290, 710, 751, 16))
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)
        self.bg = QLabel(self.widget_3)
        self.bg.setObjectName("bg")
        self.bg.setGeometry(QRect(290, 310, 731, 451))
        self.bg.setStyleSheet("background-color: rgb(255,255,255);")
        self.addButton = QPushButton(self.widget_3)
        self.addButton.setObjectName("addButton")
        self.addButton.setGeometry(QRect(70, 600, 91, 81))
        self.addButton.setStyleSheet("color: rgb(0,0,0);")
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
        self.stackedWidget.addWidget(self.dashboardPage)
        self.addPage = QWidget()
        self.addPage.setObjectName("addPage")
        self.widget_4 = QWidget(self.addPage)
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_2 = QPushButton(self.widget_4)
        self.goGoalButton_2.setObjectName("goGoalButton_2")
        self.goGoalButton_2.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_2.setFont(font3)
        self.goGoalButton_2.setStyleSheet(
            "QPushButton#goGoalButton_2 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goGoalButton_2:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.goDashboardButton_2 = QPushButton(self.widget_4)
        self.goDashboardButton_2.setObjectName("goDashboardButton_2")
        self.goDashboardButton_2.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_2.setFont(font3)
        self.goDashboardButton_2.setStyleSheet(
            "QPushButton#goDashboardButton_2 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goDashboardButton_2:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}\n"
            ""
        )
        self.label_75 = QLabel(self.widget_4)
        self.label_75.setObjectName("label_75")
        self.label_75.setGeometry(QRect(20, 170, 31, 31))
        self.label_75.setStyleSheet("")
        self.label_75.setPixmap(QPixmap(":/pics/images/user.png"))
        self.label_75.setScaledContents(True)
        self.label_76 = QLabel(self.widget_4)
        self.label_76.setObjectName("label_76")
        self.label_76.setGeometry(QRect(100, 60, 121, 21))
        self.label_76.setFont(font2)
        self.label_76.setStyleSheet("color: white;\n" "")
        self.closeButton_4 = QPushButton(self.widget_4)
        self.closeButton_4.setObjectName("closeButton_4")
        self.closeButton_4.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(
            self.closeButton_4.sizePolicy().hasHeightForWidth()
        )
        self.closeButton_4.setSizePolicy(sizePolicy1)
        self.closeButton_4.setBaseSize(QSize(0, 0))
        self.closeButton_4.setStyleSheet(
            "QPushButton#closeButton_4 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#closeButton_4:hover {\n"
            "    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
            "    border-radius: 50%; /* set the border radius to create a circle */\n"
            "}\n"
            ""
        )
        self.closeButton_4.setIcon(icon)
        self.label_83 = QLabel(self.widget_4)
        self.label_83.setObjectName("label_83")
        self.label_83.setGeometry(QRect(0, 0, 1071, 101))
        self.label_83.setStyleSheet("background-color: rgb(81,74,248);")
        self.goAccountButton_2 = QPushButton(self.widget_4)
        self.goAccountButton_2.setObjectName("goAccountButton_2")
        self.goAccountButton_2.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_2.setFont(font3)
        self.goAccountButton_2.setStyleSheet(
            "QPushButton#goAccountButton_2 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goAccountButton_2:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.label_88 = QLabel(self.widget_4)
        self.label_88.setObjectName("label_88")
        self.label_88.setGeometry(QRect(0, 100, 1021, 701))
        self.label_88.setStyleSheet("background-color: rgb(250,250,250);")
        self.label_89 = QLabel(self.widget_4)
        self.label_89.setObjectName("label_89")
        self.label_89.setGeometry(QRect(20, 290, 31, 31))
        self.label_89.setStyleSheet("")
        self.label_89.setPixmap(QPixmap(":/pics/images/goal.png"))
        self.label_89.setScaledContents(True)
        self.label_90 = QLabel(self.widget_4)
        self.label_90.setObjectName("label_90")
        self.label_90.setGeometry(QRect(20, 230, 31, 31))
        self.label_90.setStyleSheet("")
        self.label_90.setPixmap(QPixmap(":/pics/images/trans.png"))
        self.label_90.setScaledContents(True)
        self.tabsButton_2 = QPushButton(self.widget_4)
        self.tabsButton_2.setObjectName("tabsButton_2")
        self.tabsButton_2.setGeometry(QRect(50, 50, 41, 41))
        self.tabsButton_2.setStyleSheet(
            "QPushButton#tabsButton_2 {\n"
            "    border: none;\n"
            "    background-color: rgb(81,74,248);\n"
            "   qproperty-iconSize: 40px;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#tabsButton_2:hover {\n"
            "    background-color: rgb(81,74,170);\n"
            "}\n"
            ""
        )
        self.tabsButton_2.setIcon(icon1)
        self.label_91 = QLabel(self.widget_4)
        self.label_91.setObjectName("label_91")
        self.label_91.setGeometry(QRect(0, 100, 251, 701))
        self.label_91.setStyleSheet("background-color: rgb(255,255,255);")
        self.goTransButton_2 = QPushButton(self.widget_4)
        self.goTransButton_2.setObjectName("goTransButton_2")
        self.goTransButton_2.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_2.setFont(font3)
        self.goTransButton_2.setStyleSheet(
            "QPushButton#goTransButton_2 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goTransButton_2:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.label_94 = QLabel(self.widget_4)
        self.label_94.setObjectName("label_94")
        self.label_94.setGeometry(QRect(20, 110, 31, 31))
        self.label_94.setStyleSheet("background-image: url(:/pics/images/home.png);")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(270, 120, 151, 31))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet("color: rgb(0,0,0);")
        self.line = QFrame(self.widget_4)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(270, 150, 731, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.transnameLineEdit = QLineEdit(self.widget_4)
        self.transnameLineEdit.setObjectName("transnameLineEdit")
        self.transnameLineEdit.setGeometry(QRect(270, 200, 241, 31))
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(270, 170, 151, 31))
        font8 = QFont()
        font8.setPointSize(16)
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet("color: rgb(0,0,0);")
        self.catLineEdit = QLineEdit(self.widget_4)
        self.catLineEdit.setObjectName("catLineEdit")
        self.catLineEdit.setGeometry(QRect(270, 270, 241, 31))
        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(270, 240, 151, 31))
        self.label_11.setFont(font8)
        self.label_11.setStyleSheet("color: rgb(0,0,0);")
        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(QRect(560, 170, 151, 31))
        self.label_12.setFont(font8)
        self.label_12.setStyleSheet("color: rgb(0,0,0);")
        self.label_13 = QLabel(self.widget_4)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(QRect(270, 460, 151, 31))
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet("color: rgb(0,0,0);")
        self.line_2 = QFrame(self.widget_4)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(260, 490, 731, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.goalnameLineEdit = QLineEdit(self.widget_4)
        self.goalnameLineEdit.setObjectName("goalnameLineEdit")
        self.goalnameLineEdit.setGeometry(QRect(270, 540, 241, 31))
        self.goalamountLineEdit = QLineEdit(self.widget_4)
        self.goalamountLineEdit.setObjectName("goalamountLineEdit")
        self.goalamountLineEdit.setGeometry(QRect(270, 620, 241, 31))
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName("label_14")
        self.label_14.setGeometry(QRect(270, 510, 151, 31))
        self.label_14.setFont(font8)
        self.label_14.setStyleSheet("color: rgb(0,0,0);")
        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName("label_15")
        self.label_15.setGeometry(QRect(270, 590, 151, 31))
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet("color: rgb(0,0,0);")
        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName("label_16")
        self.label_16.setGeometry(QRect(560, 500, 151, 31))
        self.label_16.setFont(font8)
        self.label_16.setStyleSheet("color: rgb(0,0,0);")
        self.income_radio = QRadioButton(self.widget_4)
        self.income_radio.setObjectName("income_radio")
        self.income_radio.setGeometry(QRect(290, 380, 100, 20))
        self.income_radio.setStyleSheet("color: rgb(0,0,0);")
        self.expense_radio = QRadioButton(self.widget_4)
        self.expense_radio.setObjectName("expense_radio")
        self.expense_radio.setGeometry(QRect(410, 380, 100, 20))
        self.expense_radio.setStyleSheet("color: rgb(0,0,0);")
        self.saveTransButton = QPushButton(self.widget_4)
        self.saveTransButton.setObjectName("saveTransButton")
        self.saveTransButton.setGeometry(QRect(270, 420, 113, 32))
        self.saveGoalButton = QPushButton(self.widget_4)
        self.saveGoalButton.setObjectName("saveGoalButton")
        self.saveGoalButton.setGeometry(QRect(270, 680, 113, 32))
        self.transamountLineEdit = QLineEdit(self.widget_4)
        self.transamountLineEdit.setObjectName("transamountLineEdit")
        self.transamountLineEdit.setGeometry(QRect(270, 340, 241, 31))
        self.label_17 = QLabel(self.widget_4)
        self.label_17.setObjectName("label_17")
        self.label_17.setGeometry(QRect(270, 310, 151, 31))
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet("color: rgb(0,0,0);")
        self.transDesc = QTextEdit(self.widget_4)
        self.transDesc.setObjectName("transDesc")
        self.transDesc.setGeometry(QRect(560, 210, 431, 261))
        self.GoalDesc = QTextEdit(self.widget_4)
        self.GoalDesc.setObjectName("GoalDesc")
        self.GoalDesc.setGeometry(QRect(560, 540, 431, 211))
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
        self.stackedWidget.addWidget(self.addPage)
        self.TransactionPage = QWidget()
        self.TransactionPage.setObjectName("TransactionPage")
        self.widget_5 = QWidget(self.TransactionPage)
        self.widget_5.setObjectName("widget_5")
        self.widget_5.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_3 = QPushButton(self.widget_5)
        self.goGoalButton_3.setObjectName("goGoalButton_3")
        self.goGoalButton_3.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_3.setFont(font3)
        self.goGoalButton_3.setStyleSheet(
            "QPushButton#goGoalButton_3 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goGoalButton_3:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.goDashboardButton_3 = QPushButton(self.widget_5)
        self.goDashboardButton_3.setObjectName("goDashboardButton_3")
        self.goDashboardButton_3.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_3.setFont(font3)
        self.goDashboardButton_3.setStyleSheet(
            "QPushButton#goDashboardButton_3 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goDashboardButton_3:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}\n"
            ""
        )
        self.label_77 = QLabel(self.widget_5)
        self.label_77.setObjectName("label_77")
        self.label_77.setGeometry(QRect(20, 170, 31, 31))
        self.label_77.setStyleSheet("")
        self.label_77.setPixmap(QPixmap(":/pics/images/user.png"))
        self.label_77.setScaledContents(True)
        self.label_78 = QLabel(self.widget_5)
        self.label_78.setObjectName("label_78")
        self.label_78.setGeometry(QRect(100, 60, 121, 21))
        self.label_78.setFont(font2)
        self.label_78.setStyleSheet("color: white;\n" "")
        self.closeButton_5 = QPushButton(self.widget_5)
        self.closeButton_5.setObjectName("closeButton_5")
        self.closeButton_5.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(
            self.closeButton_5.sizePolicy().hasHeightForWidth()
        )
        self.closeButton_5.setSizePolicy(sizePolicy1)
        self.closeButton_5.setBaseSize(QSize(0, 0))
        self.closeButton_5.setStyleSheet(
            "QPushButton#closeButton_5 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#closeButton_5:hover {\n"
            "    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
            "    border-radius: 50%; /* set the border radius to create a circle */\n"
            "}\n"
            ""
        )
        self.closeButton_5.setIcon(icon)
        self.label_84 = QLabel(self.widget_5)
        self.label_84.setObjectName("label_84")
        self.label_84.setGeometry(QRect(0, 0, 1071, 101))
        self.label_84.setStyleSheet("background-color: rgb(81,74,248);")
        self.goAccountButton_3 = QPushButton(self.widget_5)
        self.goAccountButton_3.setObjectName("goAccountButton_3")
        self.goAccountButton_3.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_3.setFont(font3)
        self.goAccountButton_3.setStyleSheet(
            "QPushButton#goAccountButton_3 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goAccountButton_3:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.label_92 = QLabel(self.widget_5)
        self.label_92.setObjectName("label_92")
        self.label_92.setGeometry(QRect(0, 100, 1021, 701))
        self.label_92.setStyleSheet("background-color: rgb(250,250,250);")
        self.label_93 = QLabel(self.widget_5)
        self.label_93.setObjectName("label_93")
        self.label_93.setGeometry(QRect(20, 290, 31, 31))
        self.label_93.setStyleSheet("")
        self.label_93.setPixmap(QPixmap(":/pics/images/goal.png"))
        self.label_93.setScaledContents(True)
        self.label_95 = QLabel(self.widget_5)
        self.label_95.setObjectName("label_95")
        self.label_95.setGeometry(QRect(20, 230, 31, 31))
        self.label_95.setStyleSheet("")
        self.label_95.setPixmap(QPixmap(":/pics/images/trans.png"))
        self.label_95.setScaledContents(True)
        self.tabsButton_3 = QPushButton(self.widget_5)
        self.tabsButton_3.setObjectName("tabsButton_3")
        self.tabsButton_3.setGeometry(QRect(50, 50, 41, 41))
        self.tabsButton_3.setStyleSheet(
            "QPushButton#tabsButton_3 {\n"
            "    border: none;\n"
            "    background-color: rgb(81,74,248);\n"
            "   qproperty-iconSize: 40px;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#tabsButton_3:hover {\n"
            "    background-color: rgb(81,74,170);\n"
            "}\n"
            ""
        )
        self.tabsButton_3.setIcon(icon1)
        self.label_96 = QLabel(self.widget_5)
        self.label_96.setObjectName("label_96")
        self.label_96.setGeometry(QRect(0, 100, 251, 701))
        self.label_96.setStyleSheet("background-color: rgb(255,255,255);")
        self.goTransButton_3 = QPushButton(self.widget_5)
        self.goTransButton_3.setObjectName("goTransButton_3")
        self.goTransButton_3.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_3.setFont(font3)
        self.goTransButton_3.setStyleSheet(
            "QPushButton#goTransButton_3 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goTransButton_3:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.label_97 = QLabel(self.widget_5)
        self.label_97.setObjectName("label_97")
        self.label_97.setGeometry(QRect(20, 110, 31, 31))
        self.label_97.setStyleSheet("background-image: url(:/pics/images/home.png);")
        self.label_18 = QLabel(self.widget_5)
        self.label_18.setObjectName("label_18")
        self.label_18.setGeometry(QRect(270, 120, 151, 31))
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet("color: rgb(0,0,0);")
        self.line_3 = QFrame(self.widget_5)
        self.line_3.setObjectName("line_3")
        self.line_3.setGeometry(QRect(270, 150, 731, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.scrollArea = QScrollArea(self.widget_5)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QRect(290, 220, 701, 511))
        self.scrollArea.setStyleSheet("background-color: rgb(240,240,240)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 699, 509))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.widget_6.setGeometry(QRect(70, 410, 151, 31))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy2)
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName("widget_7")
        self.widget_7.setGeometry(QRect(290, 190, 691, 31))
        self.label_19 = QLabel(self.widget_7)
        self.label_19.setObjectName("label_19")
        self.label_19.setGeometry(QRect(20, 10, 111, 16))
        self.label_20 = QLabel(self.widget_7)
        self.label_20.setObjectName("label_20")
        self.label_20.setGeometry(QRect(460, 10, 111, 16))
        self.label_21 = QLabel(self.widget_7)
        self.label_21.setObjectName("label_21")
        self.label_21.setGeometry(QRect(230, 10, 131, 16))
        self.label_22 = QLabel(self.widget_5)
        self.label_22.setObjectName("label_22")
        self.label_22.setGeometry(QRect(290, 180, 701, 41))
        self.label_22.setStyleSheet("background-color: rgb(240,240,240)")
        self.label_92.raise_()
        self.label_22.raise_()
        self.label_96.raise_()
        self.label_84.raise_()
        self.tabsButton_3.raise_()
        self.goTransButton_3.raise_()
        self.label_18.raise_()
        self.line_3.raise_()
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
        self.widget_6.raise_()
        self.widget_7.raise_()
        self.stackedWidget.addWidget(self.TransactionPage)
        self.goalPage = QWidget()
        self.goalPage.setObjectName("goalPage")
        self.widget_8 = QWidget(self.goalPage)
        self.widget_8.setObjectName("widget_8")
        self.widget_8.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_4 = QPushButton(self.widget_8)
        self.goGoalButton_4.setObjectName("goGoalButton_4")
        self.goGoalButton_4.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_4.setFont(font3)
        self.goGoalButton_4.setStyleSheet(
            "QPushButton#goGoalButton_4 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goGoalButton_4:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.goDashboardButton_4 = QPushButton(self.widget_8)
        self.goDashboardButton_4.setObjectName("goDashboardButton_4")
        self.goDashboardButton_4.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_4.setFont(font3)
        self.goDashboardButton_4.setStyleSheet(
            "QPushButton#goDashboardButton_4 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goDashboardButton_4:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}\n"
            ""
        )
        self.label_79 = QLabel(self.widget_8)
        self.label_79.setObjectName("label_79")
        self.label_79.setGeometry(QRect(20, 170, 31, 31))
        self.label_79.setStyleSheet("")
        self.label_79.setPixmap(QPixmap(":/pics/images/user.png"))
        self.label_79.setScaledContents(True)
        self.label_80 = QLabel(self.widget_8)
        self.label_80.setObjectName("label_80")
        self.label_80.setGeometry(QRect(100, 60, 121, 21))
        self.label_80.setFont(font2)
        self.label_80.setStyleSheet("color: white;\n" "")
        self.closeButton_6 = QPushButton(self.widget_8)
        self.closeButton_6.setObjectName("closeButton_6")
        self.closeButton_6.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(
            self.closeButton_6.sizePolicy().hasHeightForWidth()
        )
        self.closeButton_6.setSizePolicy(sizePolicy1)
        self.closeButton_6.setBaseSize(QSize(0, 0))
        self.closeButton_6.setStyleSheet(
            "QPushButton#closeButton_6 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#closeButton_6:hover {\n"
            "    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
            "    border-radius: 50%; /* set the border radius to create a circle */\n"
            "}\n"
            ""
        )
        self.closeButton_6.setIcon(icon)
        self.label_85 = QLabel(self.widget_8)
        self.label_85.setObjectName("label_85")
        self.label_85.setGeometry(QRect(0, 0, 1071, 101))
        self.label_85.setStyleSheet("background-color: rgb(81,74,248);")
        self.goAccountButton_4 = QPushButton(self.widget_8)
        self.goAccountButton_4.setObjectName("goAccountButton_4")
        self.goAccountButton_4.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_4.setFont(font3)
        self.goAccountButton_4.setStyleSheet(
            "QPushButton#goAccountButton_4 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goAccountButton_4:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.label_98 = QLabel(self.widget_8)
        self.label_98.setObjectName("label_98")
        self.label_98.setGeometry(QRect(0, 100, 1021, 701))
        self.label_98.setStyleSheet("background-color: rgb(250,250,250);")
        self.label_99 = QLabel(self.widget_8)
        self.label_99.setObjectName("label_99")
        self.label_99.setGeometry(QRect(20, 290, 31, 31))
        self.label_99.setStyleSheet("")
        self.label_99.setPixmap(QPixmap(":/pics/images/goal.png"))
        self.label_99.setScaledContents(True)
        self.label_100 = QLabel(self.widget_8)
        self.label_100.setObjectName("label_100")
        self.label_100.setGeometry(QRect(20, 230, 31, 31))
        self.label_100.setStyleSheet("")
        self.label_100.setPixmap(QPixmap(":/pics/images/trans.png"))
        self.label_100.setScaledContents(True)
        self.tabsButton_4 = QPushButton(self.widget_8)
        self.tabsButton_4.setObjectName("tabsButton_4")
        self.tabsButton_4.setGeometry(QRect(50, 50, 41, 41))
        self.tabsButton_4.setStyleSheet(
            "QPushButton#tabsButton_4 {\n"
            "    border: none;\n"
            "    background-color: rgb(81,74,248);\n"
            "   qproperty-iconSize: 40px;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#tabsButton_4:hover {\n"
            "    background-color: rgb(81,74,170);\n"
            "}\n"
            ""
        )
        self.tabsButton_4.setIcon(icon1)
        self.label_101 = QLabel(self.widget_8)
        self.label_101.setObjectName("label_101")
        self.label_101.setGeometry(QRect(0, 100, 251, 701))
        self.label_101.setStyleSheet("background-color: rgb(255,255,255);")
        self.goTransButton_4 = QPushButton(self.widget_8)
        self.goTransButton_4.setObjectName("goTransButton_4")
        self.goTransButton_4.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_4.setFont(font3)
        self.goTransButton_4.setStyleSheet(
            "QPushButton#goTransButton_4 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goTransButton_4:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.label_102 = QLabel(self.widget_8)
        self.label_102.setObjectName("label_102")
        self.label_102.setGeometry(QRect(20, 110, 31, 31))
        self.label_102.setStyleSheet("background-image: url(:/pics/images/home.png);")
        self.label_23 = QLabel(self.widget_8)
        self.label_23.setObjectName("label_23")
        self.label_23.setGeometry(QRect(270, 120, 151, 31))
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet("color: rgb(0,0,0);")
        self.line_4 = QFrame(self.widget_8)
        self.line_4.setObjectName("line_4")
        self.line_4.setGeometry(QRect(270, 150, 731, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName("widget_9")
        self.widget_9.setGeometry(QRect(70, 410, 151, 31))
        sizePolicy2.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy2)
        self.label_85.raise_()
        self.label_98.raise_()
        self.tabsButton_4.raise_()
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
        self.stackedWidget.addWidget(self.goalPage)
        self.logoutPage = QWidget()
        self.logoutPage.setObjectName("logoutPage")
        self.widget_11 = QWidget(self.logoutPage)
        self.widget_11.setObjectName("widget_11")
        self.widget_11.setGeometry(QRect(0, 0, 1021, 771))
        self.goGoalButton_5 = QPushButton(self.widget_11)
        self.goGoalButton_5.setObjectName("goGoalButton_5")
        self.goGoalButton_5.setGeometry(QRect(-10, 280, 261, 61))
        self.goGoalButton_5.setFont(font3)
        self.goGoalButton_5.setStyleSheet(
            "QPushButton#goGoalButton_5 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goGoalButton_5:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.goDashboardButton_5 = QPushButton(self.widget_11)
        self.goDashboardButton_5.setObjectName("goDashboardButton_5")
        self.goDashboardButton_5.setGeometry(QRect(-10, 100, 261, 61))
        self.goDashboardButton_5.setFont(font3)
        self.goDashboardButton_5.setStyleSheet(
            "QPushButton#goDashboardButton_5 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goDashboardButton_5:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}\n"
            ""
        )
        self.label_81 = QLabel(self.widget_11)
        self.label_81.setObjectName("label_81")
        self.label_81.setGeometry(QRect(20, 170, 31, 31))
        self.label_81.setStyleSheet("")
        self.label_81.setPixmap(QPixmap(":/pics/images/user.png"))
        self.label_81.setScaledContents(True)
        self.label_82 = QLabel(self.widget_11)
        self.label_82.setObjectName("label_82")
        self.label_82.setGeometry(QRect(100, 60, 121, 21))
        self.label_82.setFont(font2)
        self.label_82.setStyleSheet("color: white;\n" "")
        self.closeButton_7 = QPushButton(self.widget_11)
        self.closeButton_7.setObjectName("closeButton_7")
        self.closeButton_7.setGeometry(QRect(970, 30, 31, 31))
        sizePolicy1.setHeightForWidth(
            self.closeButton_7.sizePolicy().hasHeightForWidth()
        )
        self.closeButton_7.setSizePolicy(sizePolicy1)
        self.closeButton_7.setBaseSize(QSize(0, 0))
        self.closeButton_7.setStyleSheet(
            "QPushButton#closeButton_7 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#closeButton_7:hover {\n"
            "    border: 2px dashed grey; /* set the border to a solid color when hovering */\n"
            "    border-radius: 50%; /* set the border radius to create a circle */\n"
            "}\n"
            ""
        )
        self.closeButton_7.setIcon(icon)
        self.label_86 = QLabel(self.widget_11)
        self.label_86.setObjectName("label_86")
        self.label_86.setGeometry(QRect(0, 0, 1071, 101))
        self.label_86.setStyleSheet("background-color: rgb(81,74,248);")
        self.goAccountButton_5 = QPushButton(self.widget_11)
        self.goAccountButton_5.setObjectName("goAccountButton_5")
        self.goAccountButton_5.setGeometry(QRect(-10, 160, 261, 61))
        self.goAccountButton_5.setFont(font3)
        self.goAccountButton_5.setStyleSheet(
            "QPushButton#goAccountButton_5 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goAccountButton_5:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.label_103 = QLabel(self.widget_11)
        self.label_103.setObjectName("label_103")
        self.label_103.setGeometry(QRect(0, 100, 1021, 701))
        self.label_103.setStyleSheet("background-color: rgb(250,250,250);")
        self.label_104 = QLabel(self.widget_11)
        self.label_104.setObjectName("label_104")
        self.label_104.setGeometry(QRect(20, 290, 31, 31))
        self.label_104.setStyleSheet("")
        self.label_104.setPixmap(QPixmap(":/pics/images/goal.png"))
        self.label_104.setScaledContents(True)
        self.label_105 = QLabel(self.widget_11)
        self.label_105.setObjectName("label_105")
        self.label_105.setGeometry(QRect(20, 230, 31, 31))
        self.label_105.setStyleSheet("")
        self.label_105.setPixmap(QPixmap(":/pics/images/trans.png"))
        self.label_105.setScaledContents(True)
        self.tabsButton_5 = QPushButton(self.widget_11)
        self.tabsButton_5.setObjectName("tabsButton_5")
        self.tabsButton_5.setGeometry(QRect(50, 50, 41, 41))
        self.tabsButton_5.setStyleSheet(
            "QPushButton#tabsButton_5 {\n"
            "    border: none;\n"
            "    background-color: rgb(81,74,248);\n"
            "   qproperty-iconSize: 40px;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "}\n"
            "\n"
            "QPushButton#tabsButton_5:hover {\n"
            "    background-color: rgb(81,74,170);\n"
            "}\n"
            ""
        )
        self.tabsButton_5.setIcon(icon1)
        self.label_106 = QLabel(self.widget_11)
        self.label_106.setObjectName("label_106")
        self.label_106.setGeometry(QRect(0, 100, 251, 701))
        self.label_106.setStyleSheet("background-color: rgb(255,255,255);")
        self.goTransButton_5 = QPushButton(self.widget_11)
        self.goTransButton_5.setObjectName("goTransButton_5")
        self.goTransButton_5.setGeometry(QRect(-10, 220, 261, 61))
        self.goTransButton_5.setFont(font3)
        self.goTransButton_5.setStyleSheet(
            "QPushButton#goTransButton_5 {\n"
            "    border: none;\n"
            "    border-radius: 10px; /* set the initial border radius */\n"
            "	color: rgb(0,0,0);\n"
            "}\n"
            "QPushButton#goTransButton_5:hover {\n"
            "    background-color: rgb(81,74,200);\n"
            "}"
        )
        self.label_107 = QLabel(self.widget_11)
        self.label_107.setObjectName("label_107")
        self.label_107.setGeometry(QRect(20, 110, 31, 31))
        self.label_107.setStyleSheet("background-image: url(:/pics/images/home.png);")
        self.label_28 = QLabel(self.widget_11)
        self.label_28.setObjectName("label_28")
        self.label_28.setGeometry(QRect(270, 120, 151, 31))
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet("color: rgb(0,0,0);")
        self.line_5 = QFrame(self.widget_11)
        self.line_5.setObjectName("line_5")
        self.line_5.setGeometry(QRect(270, 150, 731, 16))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName("widget_12")
        self.widget_12.setGeometry(QRect(70, 410, 151, 31))
        sizePolicy2.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy2)
        self.logoutButton = QPushButton(self.widget_11)
        self.logoutButton.setObjectName("logoutButton")
        self.logoutButton.setGeometry(QRect(520, 410, 161, 71))
        self.widget_12.raise_()
        self.label_86.raise_()
        self.label_103.raise_()
        self.tabsButton_5.raise_()
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
        self.stackedWidget.addWidget(self.logoutPage)

        self.retranslateUi(Form)
        self.closeButton.clicked.connect(Form.close)
        self.closeButton_2.clicked.connect(Form.close)
        self.closeButton_3.clicked.connect(Form.close)
        self.closeButton_4.clicked.connect(Form.close)
        self.closeButton_5.clicked.connect(Form.close)
        self.closeButton_6.clicked.connect(Form.close)
        self.closeButton_7.clicked.connect(Form.close)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.Signin_Label.setText(QCoreApplication.translate("Form", "Sign In", None))
        self.lineEditUserLogin.setPlaceholderText(
            QCoreApplication.translate("Form", "Username", None)
        )
        self.loginButton.setText(
            QCoreApplication.translate("Form", "S i g n  I n", None)
        )
        self.GoRegisterButton.setText(
            QCoreApplication.translate("Form", "G o  R e g i s t er", None)
        )
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", "Money Mate", None))
        self.lineEditPassLogin.setPlaceholderText(
            QCoreApplication.translate("Form", "Password", None)
        )
        self.closeButton.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.Reigstration_Label.setText(
            QCoreApplication.translate("Form", "Registration", None)
        )
        self.lineEditUserRegister.setPlaceholderText(
            QCoreApplication.translate("Form", "Username", None)
        )
        self.RegisterButton.setText(
            QCoreApplication.translate("Form", "R e g i s t er", None)
        )
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", "Money Mate", None))
        self.lineEditUserPassword.setPlaceholderText(
            QCoreApplication.translate("Form", "Password", None)
        )
        self.closeButton_2.setText("")
        self.lineEditUserPassword_2.setPlaceholderText(
            QCoreApplication.translate("Form", "Confirm Password", None)
        )
        self.goSigninButton.setText(
            QCoreApplication.translate("Form", "B a c k  to  S i g n I n", None)
        )
        self.label_29.setText(QCoreApplication.translate("Form", "0", None))
        self.CatLabel5.setText(QCoreApplication.translate("Form", "CatLabel5", None))
        self.AmountLabel1.setText(
            QCoreApplication.translate("Form", "AmountLabel1", None)
        )
        self.label_39.setText(QCoreApplication.translate("Form", "0", None))
        self.goGoalButton.setText(QCoreApplication.translate("Form", "Goal", None))
        self.label_40.setText(QCoreApplication.translate("Form", "\u0e3f", None))
        self.label_41.setText("")
        self.goDashboardButton.setText(
            QCoreApplication.translate("Form", "Dashboard", None)
        )
        self.DesLabel9.setText(QCoreApplication.translate("Form", "DesLabel9", None))
        self.label_42.setText(QCoreApplication.translate("Form", "Date", None))
        self.label_43.setText(QCoreApplication.translate("Form", "Category", None))
        self.DesLabel8.setText(QCoreApplication.translate("Form", "DesLabel8", None))
        self.DateLabel5.setText(QCoreApplication.translate("Form", "DateLabel5", None))
        self.label_44.setText(
            QCoreApplication.translate("Form", "Current Balance", None)
        )
        self.DateLabel2.setText(QCoreApplication.translate("Form", "DateLabel2", None))
        self.CatLabel7.setText(QCoreApplication.translate("Form", "CatLabel7", None))
        self.AmountLabel6.setText(
            QCoreApplication.translate("Form", "AmountLabel6", None)
        )
        self.AmountLabel9.setText(
            QCoreApplication.translate("Form", "AmountLabel9", None)
        )
        self.DesLabel4.setText(QCoreApplication.translate("Form", "DesLabel4", None))
        self.DateLabel6.setText(QCoreApplication.translate("Form", "DateLabel6", None))
        self.DateLabel1.setText(QCoreApplication.translate("Form", "DateLabel1", None))
        self.CatLabel3.setText(QCoreApplication.translate("Form", "CatLabel3", None))
        self.label_45.setText("")
        self.label_46.setText(QCoreApplication.translate("Form", "Amount", None))
        self.label_47.setText("")
        self.DateLabel3.setText(QCoreApplication.translate("Form", "DateLabel3", None))
        self.CatLabel8.setText(QCoreApplication.translate("Form", "CatLabel8", None))
        self.CatLabel9.setText(QCoreApplication.translate("Form", "CatLabel9", None))
        self.label_48.setText(QCoreApplication.translate("Form", "Money Mate", None))
        self.AmountLabel2.setText(
            QCoreApplication.translate("Form", "AmountLabel2", None)
        )
        self.DesLabel6.setText(QCoreApplication.translate("Form", "DesLabel6", None))
        self.label_49.setText("")
        self.label_50.setText(
            QCoreApplication.translate("Form", "Available Balance", None)
        )
        self.CatLabel4.setText(QCoreApplication.translate("Form", "CatLabel4", None))
        self.label_51.setText(QCoreApplication.translate("Form", "Description", None))
        self.label_52.setText(QCoreApplication.translate("Form", "\u0e3f", None))
        self.AmountLabel5.setText(
            QCoreApplication.translate("Form", "AmountLabel5", None)
        )
        self.DateLabel4.setText(QCoreApplication.translate("Form", "DateLabel4", None))
        self.DesLabel1.setText(QCoreApplication.translate("Form", "DesLabel1", None))
        self.DateLabel10.setText(
            QCoreApplication.translate("Form", "DateLabel10", None)
        )
        self.closeButton_3.setText("")
        self.label_53.setText("")
        self.label_54.setText(
            QCoreApplication.translate("Form", "Spent This Week", None)
        )
        self.CatLabel6.setText(QCoreApplication.translate("Form", "CatLabel6", None))
        self.label_55.setText("")
        self.AmountLabel7.setText(
            QCoreApplication.translate("Form", "AmountLabel7", None)
        )
        self.label_56.setText(
            QCoreApplication.translate("Form", "\u2190 User Account", None)
        )
        self.DesLabel2.setText(QCoreApplication.translate("Form", "DesLabel2", None))
        self.label_57.setText("")
        self.DateLabel8.setText(QCoreApplication.translate("Form", "DateLabel8", None))
        self.label_58.setText(QCoreApplication.translate("Form", "0", None))
        self.CatLabel10.setText(QCoreApplication.translate("Form", "CatLabel10", None))
        self.label_59.setText(QCoreApplication.translate("Form", "\u0e3f", None))
        self.AmountLabel3.setText(
            QCoreApplication.translate("Form", "AmountLabel3", None)
        )
        self.CatLabel1.setText(QCoreApplication.translate("Form", "CatLabel1", None))
        self.CatLabel2.setText(QCoreApplication.translate("Form", "CatLabel2", None))
        self.goAccountButton.setText(
            QCoreApplication.translate("Form", "Account", None)
        )
        self.DateLabel9.setText(QCoreApplication.translate("Form", "DateLabel9", None))
        self.label_60.setText("")
        self.label_61.setText("")
        self.label_62.setText("")
        self.tabsButton.setText("")
        self.AmountLabel10.setText(
            QCoreApplication.translate("Form", "AmountLabel10", None)
        )
        self.AmountLabel8.setText(
            QCoreApplication.translate("Form", "AmountLabel8", None)
        )
        self.label_63.setText("")
        self.DesLabel3.setText(QCoreApplication.translate("Form", "DesLabel3", None))
        self.DesLabel10.setText(QCoreApplication.translate("Form", "DesLabel10", None))
        self.DesLabel7.setText(QCoreApplication.translate("Form", "DesLabel7", None))
        self.DateLabel7.setText(QCoreApplication.translate("Form", "DateLabel7", None))
        self.goTransButton.setText(
            QCoreApplication.translate("Form", "Transactions", None)
        )
        self.label_64.setText("")
        self.AmountLabel4.setText(
            QCoreApplication.translate("Form", "AmountLabel4", None)
        )
        self.DesLabel5.setText(QCoreApplication.translate("Form", "DesLabel5", None))
        self.label_65.setText(
            QCoreApplication.translate("Form", "Account Transaction:", None)
        )
        self.label_66.setText("")
        self.bg.setText("")
        self.addButton.setText(QCoreApplication.translate("Form", "add +", None))
        self.goGoalButton_2.setText(QCoreApplication.translate("Form", "Goal", None))
        self.goDashboardButton_2.setText(
            QCoreApplication.translate("Form", "Dashboard", None)
        )
        self.label_75.setText("")
        self.label_76.setText(QCoreApplication.translate("Form", "Money Mate", None))
        self.closeButton_4.setText("")
        self.label_83.setText("")
        self.goAccountButton_2.setText(
            QCoreApplication.translate("Form", "Account", None)
        )
        self.label_88.setText("")
        self.label_89.setText("")
        self.label_90.setText("")
        self.tabsButton_2.setText("")
        self.label_91.setText("")
        self.goTransButton_2.setText(
            QCoreApplication.translate("Form", "Transactions", None)
        )
        self.label_94.setText("")
        self.label_3.setText(
            QCoreApplication.translate("Form", "New Transaction", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("Form", "Transaction Name", None)
        )
        self.label_11.setText(QCoreApplication.translate("Form", "Category", None))
        self.label_12.setText(QCoreApplication.translate("Form", "Description", None))
        self.label_13.setText(QCoreApplication.translate("Form", "New Goal", None))
        self.label_14.setText(QCoreApplication.translate("Form", "Goal Name", None))
        self.label_15.setText(QCoreApplication.translate("Form", "Goal Amount", None))
        self.label_16.setText(QCoreApplication.translate("Form", "Description", None))
        self.income_radio.setText(QCoreApplication.translate("Form", "Income", None))
        self.expense_radio.setText(QCoreApplication.translate("Form", "Expense", None))
        self.saveTransButton.setText(QCoreApplication.translate("Form", "Save", None))
        self.saveGoalButton.setText(QCoreApplication.translate("Form", "Save", None))
        self.label_17.setText(
            QCoreApplication.translate("Form", "Transaction Amount", None)
        )
        self.goGoalButton_3.setText(QCoreApplication.translate("Form", "Goal", None))
        self.goDashboardButton_3.setText(
            QCoreApplication.translate("Form", "Dashboard", None)
        )
        self.label_77.setText("")
        self.label_78.setText(QCoreApplication.translate("Form", "Money Mate", None))
        self.closeButton_5.setText("")
        self.label_84.setText("")
        self.goAccountButton_3.setText(
            QCoreApplication.translate("Form", "Account", None)
        )
        self.label_92.setText("")
        self.label_93.setText("")
        self.label_95.setText("")
        self.tabsButton_3.setText("")
        self.label_96.setText("")
        self.goTransButton_3.setText(
            QCoreApplication.translate("Form", "Transactions", None)
        )
        self.label_97.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", "Transaction", None))
        self.label_19.setText(
            QCoreApplication.translate("Form", "Transaction Name", None)
        )
        self.label_20.setText(
            QCoreApplication.translate("Form", "Transaction Date", None)
        )
        self.label_21.setText(
            QCoreApplication.translate("Form", "Transaction Amount", None)
        )
        self.label_22.setText("")
        self.goGoalButton_4.setText(QCoreApplication.translate("Form", "Goal", None))
        self.goDashboardButton_4.setText(
            QCoreApplication.translate("Form", "Dashboard", None)
        )
        self.label_79.setText("")
        self.label_80.setText(QCoreApplication.translate("Form", "Money Mate", None))
        self.closeButton_6.setText("")
        self.label_85.setText("")
        self.goAccountButton_4.setText(
            QCoreApplication.translate("Form", "Account", None)
        )
        self.label_98.setText("")
        self.label_99.setText("")
        self.label_100.setText("")
        self.tabsButton_4.setText("")
        self.label_101.setText("")
        self.goTransButton_4.setText(
            QCoreApplication.translate("Form", "Transactions", None)
        )
        self.label_102.setText("")
        self.label_23.setText(QCoreApplication.translate("Form", "Goals", None))
        self.goGoalButton_5.setText(QCoreApplication.translate("Form", "Goal", None))
        self.goDashboardButton_5.setText(
            QCoreApplication.translate("Form", "Dashboard", None)
        )
        self.label_81.setText("")
        self.label_82.setText(QCoreApplication.translate("Form", "Money Mate", None))
        self.closeButton_7.setText("")
        self.label_86.setText("")
        self.goAccountButton_5.setText(
            QCoreApplication.translate("Form", "Account", None)
        )
        self.label_103.setText("")
        self.label_104.setText("")
        self.label_105.setText("")
        self.tabsButton_5.setText("")
        self.label_106.setText("")
        self.goTransButton_5.setText(
            QCoreApplication.translate("Form", "Transactions", None)
        )
        self.label_107.setText("")
        self.label_28.setText(QCoreApplication.translate("Form", "User", None))
        self.logoutButton.setText(QCoreApplication.translate("Form", "Logout", None))

    # retranslateUi
