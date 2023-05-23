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
TRANSACTIONDETAIL_PAGE = 7
GOALDETAIL_PAGE = 8


load_dotenv()
mongodb_uri = os.getenv("MONGODB_URI")


class Page(QWidget):
    def __init__(self, root, conn):
        QWidget.__init__(self, None)
        self._delete_trans_slot = None  # a place to store the connected function
        self.curUser: User = None
        self.root = root
        self.conn = conn
        self.ui = Ui_Form()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # create a button at stackedwithget index 4

        self.ui.setupUi(self)
        # self.updateScroll()

        self.ui.goDashboardButton.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_2.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_3.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_4.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_5.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_7.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_8.clicked.connect(self.on_goDashboardButton_clicked)


        self.ui.GoRegisterButton.clicked.connect(self.on_goregisterButton_clicked)
        self.ui.goSigninButton.clicked.connect(self.on_gosigninButton_clicked)
        self.ui.loginButton.clicked.connect(self.on_loginButton_clicked)
        self.ui.RegisterButton.clicked.connect(self.on_registerButton_clicked)
        self.ui.addButton.clicked.connect(self.on_addButton_clicked)
        self.ui.addButton_2.clicked.connect(self.on_addButton_clicked)
        self.ui.addButton_3.clicked.connect(self.on_addButton_clicked)
        self.ui.addButton_4.clicked.connect(self.on_addButton_clicked)
        self.ui.addButton_5.clicked.connect(self.on_addButton_clicked)
        self.ui.addButton_6.clicked.connect(self.on_addButton_clicked)

        self.ui.saveTransButton.clicked.connect(self.on_saveTransactionButton_clicked)
        self.ui.saveGoalButton.clicked.connect(self.on_savegoalButton_clicked)

        self.ui.goTransButton.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_2.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_3.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_4.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_5.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_7.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_8.clicked.connect(self.on_gotransButton_clicked)

        self.ui.goGoalButton.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_2.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_3.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_4.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_5.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_7.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_8.clicked.connect(self.on_gogoalButton_clicked)    

        self.ui.goAccountButton.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_2.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_3.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_4.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_5.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_7.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_8.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.logoutButton.clicked.connect(self.on_logoutButton_clicked)
        self.ui.editBudgetButton.clicked.connect(self.on_editBudgetButton_clicked)
        self.ui.EditButton.clicked.connect(self.on_editButton_clicked)
        self.ui.SaveButton.clicked.connect(self.on_saveButton_clicked)

    def on_editBudgetButton_clicked(self):
        t = self.ui.editBudgetButton.text()
        if t == "Edit":
            self.ui.bugetField.setReadOnly(False)
            self.ui.editBudgetButton.setText("Save")
        else:
            self.curUser.setBudget(float(self.ui.bugetField.text()))
            transaction.commit()
            self.updateDynamicComponent()

    def on_saveButton_clicked(self):
        button = self.sender()
        transaction_id = button.objectName()
        print(transaction_id)
        self.curUser.editTransaction(
            transaction_id,
            self.ui.transnameLineEdit_2.text(),
            self.ui.transamountLineEdit_2.text(),
            self.ui.catLineEdit_2.text(),
            self.ui.transDesc_2.toPlainText(),
        )
        self.ui.EditButton.setEnabled(True)
        self.ui.transamountLineEdit_2.setReadOnly(True)
        self.ui.catLineEdit_2.setReadOnly(True)
        self.ui.transnameLineEdit_2.setReadOnly(True)
        self.ui.transDesc_2.setReadOnly(True)
        self.ui.SaveButton.setEnabled(False)
        self.updateDynamicComponent()
        self.switchPage(TRANSACTION_PAGE)

    def on_editButton_clicked(self):
        self.ui.transamountLineEdit_2.setReadOnly(False)
        self.ui.catLineEdit_2.setReadOnly(False)
        self.ui.transnameLineEdit_2.setReadOnly(False)

        self.ui.transDesc_2.setReadOnly(False)
        self.ui.EditButton.setEnabled(False)
        self.ui.SaveButton.setEnabled(True)

        # self.ui.DeleteTransButton.clicked.connect(self.on_deleteTransButton_clicked)

    def on_logoutButton_clicked(self):
        self.curUser = None
        self.switchPage(LOGIN_PAGE)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()

    def on_goaccountButton_clicked(self):
        self.switchPage(USER_PAGE)

    def on_deleteTransButton_clicked(self, transaction_id):
        password = self.ui.PasswordField.text()
        tmp = self.root["user"]
        user = tmp[self.curUser.getUsername()]
        hashedpass = user.getHashedpass()
        if bcrypt.checkpw(password.encode("utf-8"), hashedpass):
            user.removeTransactionById(transaction_id)
            transaction.commit()
            self.updateDynamicComponent()
            self.switchPage(TRANSACTION_PAGE)
    
    def on_goal_clicked(self):
        button = self.sender()
        goal_id = button.objectName()  # Get the objectName of the button
        goal_obj = self.curUser.getGoalById(goal_id)
        self.switchPage(GOALDETAIL_PAGE)
        print(goal_id)
        print(goal_obj)

    def on_transaction_clicked(self):
        button = self.sender()
        transaction_id = button.objectName()  # Get the objectName of the button
        transaction_obj = self.curUser.getTransactionById(transaction_id)
        self.populateTransactionDetails(transaction_obj)
        self.ui.SaveButton.setEnabled(False)

        # Disconnect the old slot if it exists
        if self._delete_trans_slot is not None:
            try:
                self.ui.DeleteTransButton.clicked.disconnect(self._delete_trans_slot)
            except RuntimeError:
                # Ignore the RuntimeError that occurs when the slot was already disconnected
                pass

        # Create a new slot
        self._delete_trans_slot = lambda _: self.on_deleteTransButton_clicked(
            transaction_id
        )

        # Connect the new slot
        self.ui.DeleteTransButton.clicked.connect(self._delete_trans_slot)
        self.ui.SaveButton.setObjectName(str(transaction_id))
        self.switchPage(TRANSACTIONDETAIL_PAGE)

    def populateTransactionDetails(self, transaction_obj):
        self.ui.transnameLineEdit_2.setText(str(transaction_obj.getName()))
        self.ui.transamountLineEdit_2.setText(str(transaction_obj.getAmount()))
        self.ui.catLineEdit_2.setText(str(transaction_obj.getCategory()))
        self.ui.transDesc_2.setText(str(transaction_obj.getDesc()))

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
                    self.updateDynamicComponent()
                    # self.updateScroll()
                    # self.updateDashboard()
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
            self.updateDynamicComponent()
            # self.updateScroll()
            # self.updateDashboard()
            # TODO: save Income to a transaction list in database
        elif self.ui.expense_radio.isChecked():
            tmp = self.root["user"]
            user = tmp[self.curUser.getUsername()]
            exp = Expense(transName, transAmount, transCat, transDesc)
            user.addTransaction(exp)
            transaction.commit()
            self.updateDynamicComponent()
            # self.updateScroll()
            # self.updateDashboard()
            # TODO: save Expense to a transaction list in database (Done)
        else:
            print("Please select income or expense")
        self.switchPage(TRANSACTION_PAGE)

    def on_gotransButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(TRANSACTION_PAGE)

    def on_savegoalButton_clicked(self):
        goalName = self.ui.goalnameLineEdit.text()
        goalAmount = self.ui.goalamountLineEdit.text()
        goalDesc = self.ui.GoalDesc.toPlainText()
        tmp = self.root["user"]
        user = tmp[self.curUser.getUsername()]
        goal = Goal(goalName, float(goalAmount), goalDesc)
        user.addGoal(goal)
        transaction.commit()
        self.updateDynamicComponent()
        self.switchPage(GOAL_PAGE)
        # TODO: save goal to a goal list in database (Done)

    def switchPage(self, page):
        self.ui.stackedWidget.setCurrentIndex(page)
        self.clearLineEdits()

    def clearLineEdits(self):
        self.ui.PasswordField.setText("")
        self.ui.transnameLineEdit.setText("")
        self.ui.catLineEdit.setText("")
        self.ui.transamountLineEdit.setText("")
        self.ui.transDesc.setText("")
        self.ui.goalnameLineEdit.setText("")
        self.ui.goalamountLineEdit.setText("")
        self.ui.GoalDesc.setText("")

    # calls update on every page
    def updateDynamicComponent(self):
        self.updateDashboardPage()
        self.updateTransactionPage()
        self.updateGoalPage()
        self.UpdatelogoutPage()

    def updateDashboardPage(self):
        self.ui.currentBalanceLabel.setText(
            str("{:.2f}".format(self.curUser.getCurrentBalance()))
        )
        textColor = (
            "green"
            if self.curUser.getCurrentBalance() > 0
            else "red"
            if self.curUser.getCurrentBalance() < 0
            else "black"
        )
        self.ui.currentBalanceLabel.setStyleSheet(f"color: {textColor};")
        self.ui.spentLabel.setText(str("{:.2f}".format(self.curUser.getWeeklySpent())))
        self.ui.budgetLabel.setText(
            str(
                "{:.2f}".format(
                    self.curUser.getBudget() - self.curUser.getWeeklySpent()
                )
            )
        )

        for i in reversed(range(self.ui.scrollArea_2.widget().layout().count())):
            self.ui.scrollArea_2.widget().layout().itemAt(i).widget().setParent(None)
        scroll_widget = self.ui.scrollArea_2.widget()
        scroll_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout = scroll_widget.layout()
        layout.setSpacing(0)  # Set spacing to 0
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Align to top

        if self.curUser:
            count = 0
            for t in (self.curUser.getTransactions())[::-1]:
                count += 1
                if count > 3:
                    break
                button = QPushButton()

                button.setObjectName(str(t.getID()))  # Set object name

                button.setStyleSheet(
                    """
                    #{id} {{
                        border: 1px solid black;
                    }}
                    #{id}:pressed {{
                        background-color: rgb(192, 192, 192);
                    }}
                    """.format(
                        id=button.objectName()
                    )
                )
                button_layout = QHBoxLayout(button)

                left_label = QLabel(t.getName(), button)  # Set button as parent
                middle_label = QLabel(
                    str("{:.2f}".format(t.getAmount())), button
                )  # Set button as parent
                textColor = "green" if isinstance(t, Income) else "red"
                middle_label.setStyleSheet(f"QLabel {{color: {textColor};}}")
                right_label = QLabel(
                    str(t.getDate().date()), button
                )  # Set button as parent

                button_layout.addWidget(left_label)
                button_layout.addWidget(middle_label)
                button_layout.addWidget(right_label)

                button.setLayout(button_layout)
                button.setMinimumHeight(50)  # Set minimum height here

                # Add bottom border to the button
                button.clicked.connect(self.on_transaction_clicked)
                scroll_widget.layout().addWidget(button)

            # for goals display on dashboard
            count = 0
            for i in reversed(range(self.ui.horizontalLayout.layout().count())):
                self.ui.horizontalLayout.layout().itemAt(i).widget().setParent(None)

            layout = self.ui.horizontalLayout.layout()
            layout.setSpacing(25)  # Set spacing to 0
            layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            for g in self.curUser.getGoals():
                count += 1
                if count > 3:
                    break
                button = QPushButton()
                button_layout = QVBoxLayout(button)
                top_label = QLabel(g.getName(), button)
                progressStr = f'{"{:.2f}".format(g.getProgress())}/{"{:.2f}".format(g.getAmount())} ({round(g.getProgress() / g.getAmount() * 100)}%)'
                bottom_label = QLabel(progressStr, button)
                button_layout.addWidget(top_label)
                button_layout.addWidget(bottom_label)
                button.setLayout(button_layout)
                button.setMinimumHeight(180)
                button.setMinimumWidth(220)
                self.ui.horizontalLayout.layout().addWidget(button)

    def updateTransactionPage(self):
        for i in reversed(range(self.ui.scrollArea.widget().layout().count())):
            self.ui.scrollArea.widget().layout().itemAt(i).widget().setParent(None)
        scroll_widget = self.ui.scrollArea.widget()
        scroll_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout = scroll_widget.layout()
        layout.setSpacing(0)  # Set spacing to 0
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Align to top

        if self.curUser:
            for t in (self.curUser.getTransactions())[::-1]:
                button = QPushButton()

                button.setObjectName(str(t.getID()))  # Set object name

                button.setStyleSheet(
                    """
                    #{id} {{
                        border: 1px solid black;
                    }}
                    #{id}:pressed {{
                        background-color: rgb(192, 192, 192);
                    }}
                    """.format(
                        id=button.objectName()
                    )
                )
                button_layout = QHBoxLayout(button)

                left_label = QLabel(t.getName(), button)  # Set button as parent
                middle_label = QLabel(
                    str("{:.2f}".format(t.getAmount())), button
                )  # Set button as parent
                textColor = "green" if isinstance(t, Income) else "red"
                middle_label.setStyleSheet(f"QLabel {{color: {textColor};}}")
                right_label = QLabel(
                    str(t.getDate().date()), button
                )  # Set button as parent

                button_layout.addWidget(left_label)
                button_layout.addWidget(middle_label)
                button_layout.addWidget(right_label)

                button.setLayout(button_layout)
                button.setMinimumHeight(50)  # Set minimum height here

                # Add bottom border to the button
                button.clicked.connect(self.on_transaction_clicked)
                scroll_widget.layout().addWidget(button)

    def updateGoalPage(self):
        for i in reversed(range(self.ui.scrollArea_3.widget().layout().count())):
            self.ui.scrollArea_3.widget().layout().itemAt(i).widget().setParent(None)
        scroll_widget = self.ui.scrollArea_3.widget()
        scroll_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout = scroll_widget.layout()
        layout.setSpacing(0)  # Set spacing to 0
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Align to top

        if self.curUser:
            for g in (self.curUser.getGoals())[::-1]:
                button = QPushButton()
                button.setObjectName(str(g.getID()))  # Set object name

                button.setStyleSheet(
                    """
                    #{id} {{
                        border: 1px solid black;
                    }}
                    #{id}:pressed {{
                        background-color: rgb(192, 192, 192);
                    }}
                    """.format(
                        id=button.objectName()
                    )
                )

                button_layout = QHBoxLayout(button)

                left_label = QLabel(g.getName(), button)  # Set button as parent
                middle_label = QLabel(
                    str("{:.2f}".format(g.getAmount())), button
                )  # Set button as parent
                progressStr = f'{"{:.2f}".format(g.getProgress())}/{"{:.2f}".format(g.getAmount())} ({round(g.getProgress() / g.getAmount() * 100)}%)'
                right_label = QLabel(progressStr, button)  # Set button as parent

                button_layout.addWidget(left_label)
                button_layout.addWidget(middle_label)
                button_layout.addWidget(right_label)

                button.setLayout(button_layout)
                button.setMinimumHeight(50)  # Set minimum height here

                # Add bottom border to the button
                # button.clicked.connect(self.on_transaction_clicked)
                button.clicked.connect(self.on_goal_clicked)
                scroll_widget.layout().addWidget(button)

    def UpdatelogoutPage(self):
        self.ui.username_account_field.setText(self.curUser.getUsername())
        self.ui.bugetField.setText(str('{:.2f}'.format(self.curUser.getBudget())))
        self.ui.bugetField.setReadOnly(True)
        self.ui.editBudgetButton.setText("Edit")


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
