import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from loginPageModule import Ui_Form
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from dotenv import load_dotenv

####
script_dir = os.path.dirname(os.path.abspath(__file__))
moneymate_dir = os.path.abspath(os.path.join(script_dir, ".."))
sys.path.insert(0, moneymate_dir)
from User import User
# import คนละ folder ยากชิบหาย

load_dotenv()


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

    def on_goregisterButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.label_5.setText("Money Mate")
    def on_gosigninButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.label_10.setText("Money Mate")
    def on_loginButton_clicked(self):
        username = self.ui.lineEditUserLogin.text()
        password = self.ui.lineEditPassLogin.text()
        if username == "" or password == "":
            self.ui.label_5.setText("Please fill in all fields")
        else:
          try:
            pass # check if user exists in database then login
          except Exception as e:
            print(e)

    def on_registerButton_clicked(self):
        username = self.ui.lineEditUserRegister.text()
        password = self.ui.lineEditUserPassword.text()
        confirmpassword = self.ui.lineEditUserPassword_2.text()
        if username == "" or password == "" or confirmpassword == "":
            self.ui.label_10.setText("Please fill in all fields")
        else:
            if password == confirmpassword:
                user = User(username, password)
                try:
                    #TODO: check if user exists in database
                    #TODO: Move this to .env 
                    uri = "mongodb+srv://Natheeran:NonMongo21072002@cluster1.piovgcn.mongodb.net/?retryWrites=true&w=majority"
                    # Create a new client and connect to the server
                    client = MongoClient(uri, server_api=ServerApi('1'),tls = True,tlsAllowInvalidCertificates=True)
                    db = client.MoneyMate
                    userData = db.Username
                    user1 = user.__dict__
                    p_id = userData.insert_one(user1).inserted_id
                    print(p_id)
                except Exception as e:
                    print(e)
            else:
                self.ui.label_10.setText("Password does not match")
        
    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginPage = loginPage()
    loginPage.show()
    sys.exit(app.exec())
        