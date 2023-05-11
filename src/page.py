import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from pageModule import Ui_Form
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from dotenv import load_dotenv
import bcrypt
import transaction
import ZODB.FileStorage
import ZODB

from classes.User import User
from classes.Goal import Goal
from classes.Expense import Expense
from classes.Income import Income


LOGIN_PAGE = 0
REGISTER_PAGE = 1
DASHBOARD_PAGE = 2
ADD_PAGE = 3
TRANSACTION_PAGE = 4
GOAL_PAGE = 5
USER_PAGE = 6


load_dotenv()
mongodb_uri = os.getenv("MONGODB_URI")


class Page(QWidget):
    def __init__(self, root, conn):
        QWidget.__init__(self, None)
        self.curUser: User = None
        self.root = root
        self.conn = conn
        self.ui = Ui_Form()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # create a button at stackedwithget index 4

        self.ui.setupUi(self)

        self.updateScroll()

        self.ui.goDashboardButton.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_2.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_3.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_4.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_5.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.GoRegisterButton.clicked.connect(self.on_goregisterButton_clicked)
        self.ui.goSigninButton.clicked.connect(self.on_gosigninButton_clicked)
        self.ui.loginButton.clicked.connect(self.on_loginButton_clicked)
        self.ui.RegisterButton.clicked.connect(self.on_registerButton_clicked)
        self.ui.addButton.clicked.connect(self.on_addButton_clicked)
        self.ui.saveTransButton.clicked.connect(self.on_saveTransactionButton_clicked)
        self.ui.saveGoalButton.clicked.connect(self.on_savegoalButton_clicked)
        self.ui.goTransButton.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_2.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_3.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_4.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_5.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goGoalButton.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_2.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_3.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_4.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_5.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goAccountButton.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_2.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_3.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_4.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_5.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.logoutButton.clicked.connect(self.on_logoutButton_clicked)

    def on_logoutButton_clicked(self):
        self.curUser = None
        self.switchPage(LOGIN_PAGE)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

    def on_goaccountButton_clicked(self):
        self.switchPage(USER_PAGE)

    def on_gogoalButton_clicked(self):
        self.switchPage(GOAL_PAGE)

    def on_goregisterButton_clicked(self):
        self.switchPage(REGISTER_PAGE)
        self.ui.label_5.setText("Money Mate")
        self.ui.label_5.setStyleSheet("color: white")

    def on_gosigninButton_clicked(self):
        self.switchPage(LOGIN_PAGE)
        self.ui.label_10.setText("Money Mate")
        self.ui.label_10.setStyleSheet("color: white")

    def on_goDashboardButton_clicked(self):
        self.switchPage(DASHBOARD_PAGE)

    def on_loginButton_clicked(self):
        username = self.ui.lineEditUserLogin.text()
        password = self.ui.lineEditPassLogin.text()
        if username == "" or password == "":
            self.ui.label_5.setText("Please fill in all fields")
            self.ui.label_5.setStyleSheet("color: red")
        else:
            if username in self.root["user"]:
                user = self.root["user"][username]
                hashedpass = user.getHashedpass()
                if bcrypt.checkpw(password.encode("utf-8"), hashedpass):
                    self.curUser = user
                    self.updateScroll()
                    self.switchPage(DASHBOARD_PAGE)
                    self.setWindowFlags(Qt.Window)
                    self.setAttribute(Qt.WA_OpaquePaintEvent)
                    self.show()
                else:
                    print("Wrong password")
                    self.ui.label_5.setText("Password does not match")
                    self.ui.label_5.setStyleSheet("color: red")
            else:
                print("Username not found")
                self.ui.label_5.setText("Username not found")
                self.ui.label_5.setStyleSheet("color: red")
            self.ui.lineEditPassLogin.setText("")
            # try:
            #     uri = mongodb_uri
            #     # Create a new client and connect to the server
            #     client = MongoClient(uri, server_api=ServerApi('1'))
            #     db = client.get_database('MoneyMate')
            #     # db = client.MoneyMate

            #     userData = db.Username
            #     query = {"_User__username": username}
            #     # TODO: query for username, then unhash and check password.
            #     fetchedData = userData.find_one(query)
            #     if fetchedData:
            #         # Compare the hashed password with the provided password
            #         hashedpass = fetchedData['_User__hashedpass']
            #         if bcrypt.checkpw(password.encode('utf-8'), hashedpass):
            #             self.switchPage(DASHBOARD_PAGE)
            #             self.setWindowFlags(Qt.Window)
            #             self.setAttribute(Qt.WA_OpaquePaintEvent)
            #             self.show()
            #         else:
            #             print("Wrong password")
            #             self.ui.label_5.setText("Password does not match")
            #             self.ui.label_5.setStyleSheet("color: red")
            #     else:
            #         print("Username not found")
            #         self.ui.label_5.setText("Username not found")
            #         self.ui.label_5.setStyleSheet("color: red")
            #     client.close()
            # except Exception as e:
            #     print(e)

    def on_registerButton_clicked(self):
        username = self.ui.lineEditUserRegister.text()
        password = self.ui.lineEditUserPassword.text()
        confirmpassword = self.ui.lineEditUserPassword_2.text()
        if username == "" or password == "" or confirmpassword == "":
            self.ui.label_10.setText("Please fill in all fields")
            self.ui.label_10.setStyleSheet("color: red")
        else:
            if password == confirmpassword:
                if username in self.root["user"]:
                    self.ui.label_10.setText("User already exists")
                    self.ui.label_10.setStyleSheet("color: red")
                    self.ui.lineEditUserRegister.setText("")
                    self.ui.lineEditUserPassword.setText("")
                    self.ui.lineEditUserPassword_2.setText("")
                    return
                tmp = self.root["user"]
                user = User(username, password)
                tmp[username] = user
                self.root["user"] = tmp
                # self.root['user'][username] = user
                transaction.commit()
                # self.conn.close()
                self.ui.label_10.setText("User created")
                self.ui.label_10.setStyleSheet("color: green")

            # if password == confirmpassword:

            #     user = User(username, password)
            #     try:
            #         uri = mongodb_uri
            #         # Create a new client and connect to the server
            #         client = MongoClient(uri, server_api=ServerApi('1'))
            #         db = client.get_database('MoneyMate')
            #         # db = client.MoneyMate
            #         userData = db.Username
            #         user1 = user.__dict__
            #         if userData.find_one({"_User__username": user.getUsername()}):
            #             self.ui.label_10.setText("User already exists")
            #             self.ui.label_10.setStyleSheet("color: red")
            #             raise ValueError("User already exists")

            #         p_id = userData.insert_one(user1).inserted_id
            #         self.ui.label_10.setText("User created")
            #         self.ui.label_10.setStyleSheet("color: green")
            #         print(p_id)
            #     except Exception as e:
            #         print(e)
            #     client.close()
            else:
                self.ui.label_10.setText("Password does not match")
                self.ui.label_10.setStyleSheet("color: red")
        self.ui.lineEditUserRegister.setText("")
        self.ui.lineEditUserPassword.setText("")
        self.ui.lineEditUserPassword_2.setText("")

    def on_goDashboardButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_addButton_clicked(self):
        self.switchPage(ADD_PAGE)

    def on_saveTransactionButton_clicked(self):
        transName = self.ui.transnameLineEdit.text()
        transCat = self.ui.catLineEdit.text()
        transAmount = self.ui.transamountLineEdit.text()
        transDesc = self.ui.transDesc.toPlainText()

        if self.ui.income_radio.isChecked():
            tmp = self.root["user"]
            user = tmp[self.curUser.getUsername()]
            inc = Income(transName, transAmount, transCat, transDesc)
            user.addTransaction(inc)
            transaction.commit()
            self.updateScroll()
            # TODO: save Income to a transaction list in database
        elif self.ui.expense_radio.isChecked():
            tmp = self.root["user"]
            user = tmp[self.curUser.getUsername()]
            exp = Expense(transName, transAmount, transCat, transDesc)
            user.addTransaction(exp)
            transaction.commit()
            self.updateScroll()
            # TODO: save Expense to a transaction list in database
        else:
            print("Please select income or expense")

    def on_gotransButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_savegoalButton_clicked(self):
        goalName = self.ui.goalnameLineEdit.text()
        goalAmount = self.ui.goalamountLineEdit.text()
        goalDesc = self.ui.GoalDesc.toPlainText()
        tmp = self.root["user"]
        user = tmp[self.curUser.getUsername()]
        goal = Goal(goalName, goalAmount, goalDesc)
        user.addGoal(goal)
        transaction.commit()
        # TODO: save goal to a goal list in database

    def switchPage(self, page):
        self.ui.stackedWidget.setCurrentIndex(page)

    def updateScroll(self):
        for i in reversed(range(self.ui.scrollArea.widget().layout().count())):
            self.ui.scrollArea.widget().layout().itemAt(i).widget().setParent(None)
        scroll_widget = self.ui.scrollArea.widget()
        scroll_widget.setStyleSheet("background-color: rgb(248, 248, 248);")
        layout = scroll_widget.layout()
        layout.setSpacing(0)  # Set spacing to 0
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Align to top

        if self.curUser:
            for t in self.curUser.getTransactions():
                button = QPushButton()
                button.setObjectName("myButton")  # Set object name

                # Apply style using object name
                button.setStyleSheet("""
                #myButton {
                    border: 1px solid black;
                }
                #myButton:pressed {
                    background-color: rgb(192, 192, 192);
                }
                """)


                button_layout = QHBoxLayout(button)

                left_label = QLabel(t.getName(), button)  # Set button as parent
                middle_label = QLabel(str(t.getAmount()), button)  # Set button as parent
                right_label = QLabel(str(t.getDate()), button)  # Set button as parent

                button_layout.addWidget(left_label)
                button_layout.addWidget(middle_label)
                button_layout.addWidget(right_label)

                button.setLayout(button_layout)
                button.setMinimumHeight(50)  # Set minimum height here

                # Add bottom border to the button


                scroll_widget.layout().addWidget(button)




class ButtonWithLabels(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.button = QPushButton("Button with Labels", self)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def setLabel1(self, text):
        self.label1.setText(text)

    def setLabel2(self, text):
        self.label2.setText(text)


# if __name__ == "__main__":
#     storage = ZODB.FileStorage.FileStorage('testdata.fs')
#     db = ZODB.DB(storage)
#     conn = db.open()
#     root = conn.root()
#     if ('user' not in root):
#         root['user'] = {}

#     app = QApplication(sys.argv)
#     loginPage = loginPage()
#     loginPage.show()
#     sys.exit(app.exec())
