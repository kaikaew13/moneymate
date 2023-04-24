import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from loginPageModule import Ui_Form
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from dotenv import load_dotenv
import bcrypt
current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)
classes_dir_path = os.path.join(current_dir_path, 'classes')
sys.path.append(classes_dir_path)


from classes.User import User
from classes.Goal import Goal
from classes.Expense import Expense
from classes.Income import Income




LOGIN_PAGE = 0
REGISTER_PAGE = 1
DASHBOARD_PAGE = 2


load_dotenv()
mongodb_uri = os.getenv('MONGODB_URI')


class loginPage(QWidget):
    def __init__(self):

        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.setupUi(self)

        self.ui.GoRegisterButton.clicked.connect(self.on_goregisterButton_clicked)
        self.ui.goSigninButton.clicked.connect(self.on_gosigninButton_clicked)
        self.ui.loginButton.clicked.connect(self.on_loginButton_clicked)
        self.ui.RegisterButton.clicked.connect(self.on_registerButton_clicked)
        self.ui.addButton.clicked.connect(self.on_addButton_clicked)
        self.ui.goDashboardButton.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_2.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.saveTransButton.clicked.connect(self.on_saveTransactionButton_clicked)
        self.ui.saveGoalButton.clicked.connect(self.on_savegoalButton_clicked)

    def on_goregisterButton_clicked(self):
        self.switchPage(REGISTER_PAGE)
        self.ui.label_5.setText("Money Mate")
        self.ui.label_5.setStyleSheet("color: white")

    def on_gosigninButton_clicked(self):
        self.switchPage(LOGIN_PAGE)
        self.ui.label_10.setText("Money Mate")
        self.ui.label_10.setStyleSheet("color: white")

    def on_goDashboardButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)




    def on_loginButton_clicked(self):
        username = self.ui.lineEditUserLogin.text()
        password = self.ui.lineEditPassLogin.text()
        if username == "" or password == "":
            self.ui.label_5.setText("Please fill in all fields")
            self.ui.label_5.setStyleSheet("color: red")
        else:
            try:
                uri = mongodb_uri
                # Create a new client and connect to the server
                client = MongoClient(uri, server_api=ServerApi('1'))
                db = client.get_database('MoneyMate')
                # db = client.MoneyMate

                userData = db.Username
                query = {"_User__username": username}
                # TODO: query for username, then unhash and check password.
                fetchedData = userData.find_one(query)
                if fetchedData:
                    # Compare the hashed password with the provided password
                    hashedpass = fetchedData['_User__hashedpass']
                    if bcrypt.checkpw(password.encode('utf-8'), hashedpass):
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
                client.close()
            except Exception as e:
                print(e)

    def on_registerButton_clicked(self):
        username = self.ui.lineEditUserRegister.text()
        password = self.ui.lineEditUserPassword.text()
        confirmpassword = self.ui.lineEditUserPassword_2.text()
        if username == "" or password == "" or confirmpassword == "":
            self.ui.label_10.setText("Please fill in all fields")
            self.ui.label_10.setStyleSheet("color: red")
        else:
            if password == confirmpassword:
                user = User(username, password)
                try:
                    uri = mongodb_uri
                    # Create a new client and connect to the server
                    client = MongoClient(uri, server_api=ServerApi('1'))
                    db = client.get_database('MoneyMate')
                    # db = client.MoneyMate
                    userData = db.Username
                    user1 = user.__dict__
                    if userData.find_one({"_User__username": user.getUsername()}):
                        self.ui.label_10.setText("User already exists")
                        self.ui.label_10.setStyleSheet("color: red")
                        raise ValueError("User already exists")

                    p_id = userData.insert_one(user1).inserted_id
                    self.ui.label_10.setText("User created")
                    self.ui.label_10.setStyleSheet("color: green")
                    print(p_id)
                except Exception as e:
                    print(e)
                client.close()
            else:
                self.ui.label_10.setText("Password does not match")
                self.ui.label_10.setStyleSheet("color: red")


    def on_addButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def on_saveTransactionButton_clicked(self):
        transName = self.ui.transnameLineEdit.text()
        transCat = self.ui.catLineEdit.text()
        transAmount = self.ui.transamountLineEdit.text()
        transDesc = self.ui.transDesc.toPlainText()

        
        if self.ui.income_radio.isChecked():
            inc = Income(transName, transAmount, transCat, transDesc)
            # TODO: save Income to a transaction list in database
        elif self.ui.expense_radio.isChecked():
            exp = Expense(transName, transAmount, transCat, transDesc)
            # TODO: save Expense to a transaction list in database
        else:
            print("Please select income or expense")


    def on_savegoalButton_clicked(self):
        goalName = self.ui.goalnameLineEdit.text()
        goalAmount = self.ui.goalamountLineEdit.text()
        goalDesc = self.ui.GoalDesc.toPlainText()
        goal = Goal(goalName, goalAmount, goalDesc)
        # TODO: save goal to a goal list in database

    def switchPage(self, page):
        self.ui.stackedWidget.setCurrentIndex(page)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginPage = loginPage()
    loginPage.show()
    sys.exit(app.exec())
