from PySide6.QtWidgets import *
from PySide6.QtCore import *
from pageModule import Ui_Form
import os
from dotenv import load_dotenv
import bcrypt
import transaction
import ZODB.FileStorage
import ZODB
from datetime import datetime

from classes.User import User
from classes.Goal import Goal
from classes.Expense import Expense
from classes.Income import Income
from classes.billReminder import BillReminder
from classes.Notification import Notification

LOGIN_PAGE = 0
REGISTER_PAGE = 1
DASHBOARD_PAGE = 2
ADD_PAGE = 3
BILLS_PAGE = 4
TRANSACTION_PAGE = 5
GOAL_PAGE = 6
USER_PAGE = 7
TRANSACTIONDETAIL_PAGE = 8
GOALDETAIL_PAGE = 9
ADDBILL_PAGE = 10
BILLDETAIL_PAGE = 11


load_dotenv()
mongodb_uri = os.getenv("MONGODB_URI")


class Page(QWidget):
    def __init__(self, root, conn):
        QWidget.__init__(self, None)
        self._delete_trans_slot = None  # a place to store the connected function
        self._delete_goals_slot = None
        self._delete_bills_slot = None
        self.curUser: User = None
        self.notification: Notification = None
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
        self.ui.goDashboardButton_12.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_14.clicked.connect(self.on_goDashboardButton_clicked)
        self.ui.goDashboardButton_16.clicked.connect(self.on_goDashboardButton_clicked)

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
        self.ui.addButton_11.clicked.connect(self.on_addButton_clicked)
        self.ui.addButton_13.clicked.connect(self.on_addButton_clicked)

        self.ui.saveTransButton.clicked.connect(self.on_saveTransactionButton_clicked)
        self.ui.saveGoalButton.clicked.connect(self.on_savegoalButton_clicked)

        self.ui.goTransButton.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_2.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_3.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_4.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_5.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_7.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_8.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_12.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_14.clicked.connect(self.on_gotransButton_clicked)
        self.ui.goTransButton_16.clicked.connect(self.on_gotransButton_clicked)

        self.ui.goGoalButton.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_2.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_3.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_4.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_5.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_7.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_8.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_12.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_14.clicked.connect(self.on_gogoalButton_clicked)
        self.ui.goGoalButton_16.clicked.connect(self.on_gogoalButton_clicked)

        self.ui.goAccountButton.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_2.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_3.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_4.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_5.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_7.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_8.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_12.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_14.clicked.connect(self.on_goaccountButton_clicked)
        self.ui.goAccountButton_16.clicked.connect(self.on_goaccountButton_clicked)

        self.ui.logoutButton.clicked.connect(self.on_logoutButton_clicked)
        self.ui.editBudgetButton.clicked.connect(self.on_editBudgetButton_clicked)
        self.ui.EditButton.clicked.connect(self.on_editButton_clicked)
        self.ui.SaveButton.clicked.connect(self.on_saveButton_clicked)

        self.ui.goBillsButton.clicked.connect(self.on_goBillsButton_clicked)
        self.ui.goBillsButton_2.clicked.connect(self.on_goBillsButton_clicked)
        self.ui.goBillsButton_3.clicked.connect(self.on_goBillsButton_clicked)
        self.ui.goBillsButton_4.clicked.connect(self.on_goBillsButton_clicked)
        self.ui.goBillsButton_5.clicked.connect(self.on_goBillsButton_clicked)
        self.ui.goBillsButton_6.clicked.connect(self.on_goBillsButton_clicked)
        self.ui.goBillsButton_7.clicked.connect(self.on_goBillsButton_clicked)
        self.ui.goBillsButton_12.clicked.connect(self.on_goBillsButton_clicked)
        self.ui.goBillsButton_14.clicked.connect(self.on_goBillsButton_clicked)
        self.ui.goBillsButton_16.clicked.connect(self.on_goBillsButton_clicked)

        self.ui.addBillsButton.clicked.connect(self.on_addBillsButton_clicked)
        self.ui.saveBillsButton.clicked.connect(self.on_saveNewBill)

        self.ui.EditButton_2.clicked.connect(self.on_editGoalDetail_clicked)
        self.ui.SaveButton_2.clicked.connect(self.on_saveGoalDetail_clicked)

        self.ui.EditButton_4.clicked.connect(self.on_editBillDetail_clicked)
        self.ui.SaveButton_4.clicked.connect(self.on_saveBillDetail_clicked)

        self.ui.FundGoalButton.clicked.connect(self.on_fundButton_clicked)
        self.ui.deFundGoalButton.clicked.connect(self.on_defundButton_clicked)

        self.ui.notiButton.clicked.connect(self.on_notiButton_clicked)
        self.ui.notiButton_2.clicked.connect(self.on_notiButton_clicked)
        self.ui.notiButton_3.clicked.connect(self.on_notiButton_clicked)
        self.ui.notiButton_4.clicked.connect(self.on_notiButton_clicked)
        self.ui.notiButton_5.clicked.connect(self.on_notiButton_clicked)
        self.ui.notiButton_6.clicked.connect(self.on_notiButton_clicked)
        self.ui.notiButton_7.clicked.connect(self.on_notiButton_clicked)
        self.ui.notiButton_8.clicked.connect(self.on_notiButton_clicked)
        self.ui.notiButton_9.clicked.connect(self.on_notiButton_clicked)
        self.ui.notiButton_10.clicked.connect(self.on_notiButton_clicked)

        today = datetime.now()
        self.ui.calendarWidget.setMinimumDate(QDate(today.year, today.month, today.day))
        self.ui.calendarWidget_2.setMinimumDate(
            QDate(today.year, today.month, today.day)
        )

    def on_notiButton_clicked(self):
        bills = self.notification.getBills()
        goals = self.notification.getGoals()
        messageStr = ""
        if len(bills) > 0:
            messageStr += "bills that are almost due:\n"
            for b in bills:
                messageStr += f" - Bill Name: {b.getName()}\n\tAmount: {'{:.2f}'.format(b.getAmount())} Pay Before: {b.getDueDate().date()}\n"
        messageStr += "\n"
        if len(goals) > 0:
            messageStr += "goals that almost reach the target:\n"
            for g in goals:
                messageStr += f" - Goal Name: {g.getName()}\n\tProgress: {'{:.2f}'.format(g.getProgress())}/{'{:.2f}'.format(g.getAmount())} Percentage: {g.getPercentage()}%"
        self.showPopUp("Notification", messageStr)
        self.notification.setRead(True)
        self.updateDynamicComponent()

    def on_addBillsButton_clicked(self):
        self.switchPage(ADDBILL_PAGE)

    def on_goBillsButton_clicked(self):
        self.switchPage(BILLS_PAGE)

    def on_editBillDetail_clicked(self):
        self.ui.billsnameLineEdit_5.setReadOnly(False)
        self.ui.billsamountLineEdit_5.setReadOnly(False)
        self.ui.billsDesc_5.setReadOnly(False)
        self.ui.calendarWidget.setEnabled(True)
        self.ui.EditButton_4.setEnabled(False)
        self.ui.SaveButton_4.setEnabled(True)

    def on_saveBillDetail_clicked(self):
        if self.isFloat(self.ui.billsamountLineEdit_5.text()):
            button = self.sender()
            bill_id = button.objectName()
            summary = self.curUser.getSummary()
            d = self.ui.calendarWidget.selectedDate()
            summary.editBill(
                bill_id,
                self.ui.billsnameLineEdit_5.text(),
                self.ui.billsamountLineEdit_5.text(),
                datetime(d.year(), d.month(), d.day()),
                self.ui.billsDesc_5.toPlainText(),
            )
            self.ui.EditButton_4.setEnabled(True)
            self.ui.SaveButton_4.setEnabled(False)
            self.ui.billsnameLineEdit_5.setReadOnly(True)
            self.ui.billsamountLineEdit_5.setReadOnly(True)
            self.ui.billsDesc_5.setReadOnly(True)
            self.ui.calendarWidget.setEnabled(False)
            transaction.commit()
            self.updateDynamicComponent()
            self.switchPage(BILLS_PAGE)
            return
        self.showPopUp("Error", "Please enter positive number")

    def on_editGoalDetail_clicked(self):
        self.ui.GoalamountLineEdit_3.setReadOnly(False)
        self.ui.GoalnameLineEdit_3.setReadOnly(False)
        self.ui.GoalDesc_3.setReadOnly(False)
        self.ui.EditButton_2.setEnabled(False)
        self.ui.SaveButton_2.setEnabled(True)

    def on_saveGoalDetail_clicked(self):
        if self.isFloat(self.ui.GoalamountLineEdit_3.text()):
            button = self.sender()
            goal_id = button.objectName()
            summary = self.curUser.getSummary()
            summary.editGoal(
                goal_id,
                self.ui.GoalnameLineEdit_3.text(),
                self.ui.GoalamountLineEdit_3.text(),
                self.ui.GoalDesc_3.toPlainText(),
            )
            self.ui.EditButton_2.setEnabled(True)
            self.ui.GoalnameLineEdit_3.setReadOnly(True)
            self.ui.GoalamountLineEdit_3.setReadOnly(True)
            self.ui.GoalDesc_3.setReadOnly(True)
            self.ui.SaveButton_2.setEnabled(False)
            transaction.commit()
            self.updateDynamicComponent()
            self.switchPage(GOAL_PAGE)
            return
        self.showPopUp("Error", "Please enter positive number")

    def on_fundButton_clicked(self):
        button = self.sender()
        goal_id = button.objectName()
        if self.isFloat(self.ui.GoalFund_4.text()):
            f = float(self.ui.GoalFund_4.text())
            self.curUser.getSummary().addFund(goal_id, f)
            goal_obj = self.curUser.getSummary().getGoalById(goal_id)
            if goal_obj.getAmount() < goal_obj.getProgress():
                self.showPopUp(
                    "Error", "The fund added exceeds target please try again"
                )
                return
            transaction.commit()
            self.updateDynamicComponent(optional_id=goal_id)
            self.switchPage(GOALDETAIL_PAGE)
            return
        self.showPopUp("Error", "Please enter positive number")

    def showPopUp(self, title, msg):
        msgBox = QMessageBox()
        msgBox.setBaseSize(QSize(500, 300))
        msgBox.setWindowTitle(title)
        msgBox.setText(msg)
        msgBox.exec()

    def isFloat(self, numberStr):
        if numberStr != "":
            try:
                f = float(numberStr)
                if f < 0:
                    return False
            except:
                return False
            return True
        return False

    def on_defundButton_clicked(self):
        button = self.sender()
        goal_id = button.objectName()
        if self.isFloat(self.ui.GoalDefund_5.text()):
            f = float(self.ui.GoalDefund_5.text())
            self.curUser.getSummary().defund(goal_id, f)
            goal_obj = self.curUser.getSummary().getGoalById(goal_id)
            if goal_obj.getProgress() < 0:
                self.showPopUp(
                    "Error", "The current fund is less than amount defunding"
                )
                return
            transaction.commit()
            self.updateDynamicComponent(optional_id=goal_id)
            self.switchPage(GOALDETAIL_PAGE)
            return
        self.showPopUp("Error", "Please enter positive number")

    def on_editBudgetButton_clicked(self):
        t = self.ui.editBudgetButton.text()
        if t == "Edit":
            self.ui.bugetField.setReadOnly(False)
            self.ui.editBudgetButton.setText("Save")
        else:
            if self.isFloat(self.ui.bugetField.text()):
                self.curUser.getSummary().setBudget(float(self.ui.bugetField.text()))
                transaction.commit()
                self.updateDynamicComponent()
                return
            self.showPopUp("Error", "Please enter positive number")

    def on_saveButton_clicked(self):
        if self.isFloat(self.ui.transamountLineEdit_2.text()):
            button = self.sender()
            transaction_id = button.objectName()
            summary = self.curUser.getSummary()
            summary.editTransaction(
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
            transaction.commit()
            self.updateDynamicComponent()
            return
        self.showPopUp("Error", "Please enter positive number")
        # self.switchPage(TRANSACTION_PAGE)

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

    def on_deleteBillsButton_clicked(self, bill_id):
        password = self.ui.PasswordField_4.text()
        tmp = self.root["user"]
        user = tmp[self.curUser.getUsername()]
        hashedpass = user.getHashedpass()
        if bcrypt.checkpw(password.encode("utf-8"), hashedpass):
            user.getSummary().removeBillById(bill_id)
            transaction.commit()
            self.updateDynamicComponent()
            self.switchPage(BILLS_PAGE)

    def on_deleteGoalsButton_clicked(self, goal_id):
        password = self.ui.PasswordField_2.text()
        tmp = self.root["user"]
        user = tmp[self.curUser.getUsername()]
        hashedpass = user.getHashedpass()
        if bcrypt.checkpw(password.encode("utf-8"), hashedpass):
            user.getSummary().removeGoalById(goal_id)
            transaction.commit()
            self.updateDynamicComponent()
            self.switchPage(GOAL_PAGE)

    def on_deleteTransButton_clicked(self, transaction_id):
        password = self.ui.PasswordField.text()
        tmp = self.root["user"]
        user = tmp[self.curUser.getUsername()]
        hashedpass = user.getHashedpass()
        if bcrypt.checkpw(password.encode("utf-8"), hashedpass):
            user.getSummary().removeTransactionById(transaction_id)
            transaction.commit()
            self.updateDynamicComponent()
            self.switchPage(TRANSACTION_PAGE)

    def on_goal_clicked(self):
        self.ui.GoalnameLineEdit_3.setReadOnly(True)
        self.ui.GoalamountLineEdit_3.setReadOnly(True)
        self.ui.GoalDesc_3.setReadOnly(True)
        self.ui.EditButton_2.setEnabled(True)
        self.ui.SaveButton_2.setEnabled(False)
        button = self.sender()
        goal_id = button.objectName()  # Get the objectName of the button
        goal_obj = self.curUser.getSummary().getGoalById(goal_id)
        self.ui.GoalBalanceLabel_2.setText(str("{:.2f}".format(goal_obj.getProgress())))
        self.ui.GoalBalanceLabel_4.setText(
            str("{:.2f}".format(goal_obj.getAmount() - goal_obj.getProgress()))
        )
        self.ui.GoalBalanceLabel_5.setText(str("{:.2f}".format(goal_obj.getAmount())))
        self.ui.progressBar.setValue(goal_obj.getPercentage())
        self.populate_goal_details(goal_obj)

        if self._delete_goals_slot is not None:
            try:
                self.ui.DeleteTransButton.clicked.disconnect(self._delete_goals_slot)
            except RuntimeError:
                # Ignore the RuntimeError that occurs when the slot was already disconnected
                pass

        # Create a new slot
        self._delete_goals_slot = lambda _: self.on_deleteGoalsButton_clicked(goal_id)

        self.ui.DeleteGoalButton.clicked.connect(self._delete_goals_slot)
        self.ui.SaveButton_2.setObjectName(str(goal_id))
        self.ui.FundGoalButton.setObjectName(str(goal_id))
        self.ui.deFundGoalButton.setObjectName(str(goal_id))
        self.switchPage(GOALDETAIL_PAGE)

    def populate_goal_details(self, goal_obj):
        self.ui.GoalnameLineEdit_3.setText(goal_obj.getName())
        self.ui.GoalamountLineEdit_3.setText(str("{:.2f}".format(goal_obj.getAmount())))
        self.ui.GoalDesc_3.setText(goal_obj.getDesc())

    def on_bill_clicked(self):
        button = self.sender()
        bill_id = button.objectName()
        bill_obj = self.curUser.getSummary().getBillById(bill_id)
        self.populate_bill_details(bill_obj)
        self.ui.billsnameLineEdit_5.setReadOnly(True)
        self.ui.billsamountLineEdit_5.setReadOnly(True)
        self.ui.billsDesc_5.setReadOnly(True)
        self.ui.calendarWidget.setEnabled(False)
        self.ui.EditButton_4.setEnabled(True)
        self.ui.SaveButton_4.setEnabled(False)

        # Disconnect the old slot if it exists
        if self._delete_bills_slot is not None:
            try:
                self.ui.deleteBillsButton.clicked.disconnect(self._delete_bills_slot)
            except RuntimeError:
                # Ignore the RuntimeError that occurs when the slot was already disconnected
                pass
        self._delete_bills_slot = lambda _: self.on_deleteBillsButton_clicked(bill_id)

        self.ui.deleteBillsButton.clicked.connect(self._delete_bills_slot)
        self.ui.SaveButton_4.setObjectName(str(bill_id))
        self.ui.calendarWidget.setEnabled(False)
        self.switchPage(BILLDETAIL_PAGE)

    def populate_bill_details(self, bill_obj):
        self.ui.billsnameLineEdit_5.setText(bill_obj.getName())
        self.ui.billsamountLineEdit_5.setText(
            str("{:.2f}".format(bill_obj.getAmount()))
        )
        self.ui.billsDesc_5.setText(bill_obj.getDesc())
        d: datetime = bill_obj.getDueDate()
        self.ui.calendarWidget.setSelectedDate(QDate(d.year, d.month, d.day))

    def on_transaction_clicked(self):
        button = self.sender()
        transaction_id = button.objectName()  # Get the objectName of the button
        transaction_obj = self.curUser.getSummary().getTransactionById(transaction_id)
        self.populateTransactionDetails(transaction_obj)
        self.ui.EditButton.setEnabled(True)
        self.ui.SaveButton.setEnabled(False)
        self.ui.transamountLineEdit_2.setReadOnly(True)
        self.ui.catLineEdit_2.setReadOnly(True)
        self.ui.transnameLineEdit_2.setReadOnly(True)
        self.ui.transDesc_2.setReadOnly(True)

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
        self.ui.transamountLineEdit_2.setText(
            str("{:.2f}".format(transaction_obj.getAmount()))
        )
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
                    bills = self.curUser.getSummary().getAlmostDueBills()
                    goals = self.curUser.getSummary().getAlmostDoneGoals()
                    self.notification = Notification(goals, bills)
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
        if self.isFloat(self.ui.transamountLineEdit.text()):
            transName = self.ui.transnameLineEdit.text()
            transCat = self.ui.catLineEdit.text()
            transAmount = self.ui.transamountLineEdit.text()
            transDesc = self.ui.transDesc.toPlainText()

            if self.ui.income_radio.isChecked():
                tmp = self.root["user"]
                user = tmp[self.curUser.getUsername()]
                inc = Income(transName, transAmount, transCat, transDesc)
                user.getSummary().addTransaction(inc)
                transaction.commit()
                self.updateDynamicComponent()
                # self.updateScroll()
                # self.updateDashboard()
                # TODO: save Income to a transaction list in database
            elif self.ui.expense_radio.isChecked():
                tmp = self.root["user"]
                user = tmp[self.curUser.getUsername()]
                exp = Expense(transName, transAmount, transCat, transDesc)
                user.getSummary().addTransaction(exp)
                transaction.commit()
                self.updateDynamicComponent()
                # self.updateScroll()
                # self.updateDashboard()
                # TODO: save Expense to a transaction list in database (Done)
            else:
                print("Please select income or expense")
            self.switchPage(TRANSACTION_PAGE)
            return
        self.showPopUp("Error", "Please enter positive number")

    def on_gotransButton_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(TRANSACTION_PAGE)

    def on_saveNewBill(self):
        if self.isFloat(self.ui.billsamountLineedit.text()):
            billName = self.ui.billsnameLineEdit.text()
            billAmount = self.ui.billsamountLineedit.text()
            d = self.ui.calendarWidget_2.selectedDate()
            duedate = datetime(d.year(), d.month(), d.day())
            billDesc = self.ui.BillsDesc.toPlainText()
            tmp = self.root["user"]
            user = tmp[self.curUser.getUsername()]
            bill = BillReminder(billName, float(billAmount), duedate, billDesc)
            user.getSummary().addBill(bill)
            transaction.commit()
            self.updateDynamicComponent()
            self.switchPage(BILLS_PAGE)
            return
        self.showPopUp("Error", "Please enter positive number")

    def on_savegoalButton_clicked(self):
        goalName = self.ui.goalnameLineEdit.text()
        goalAmount = self.ui.goalamountLineEdit.text()
        if self.isFloat(goalAmount):
            goalDesc = self.ui.GoalDesc.toPlainText()
            tmp = self.root["user"]
            user = tmp[self.curUser.getUsername()]
            goal = Goal(goalName, float(goalAmount), goalDesc)
            user.getSummary().addGoal(goal)
            transaction.commit()
            self.updateDynamicComponent()
            self.switchPage(GOAL_PAGE)
            return
            # TODO: save goal to a goal list in database (Done)
        self.showPopUp("Error", "Please enter positive number")

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
        self.ui.PasswordField_2.setText("")
        self.ui.PasswordField_4.setText("")
        self.ui.GoalFund_4.setText("")
        self.ui.GoalDefund_5.setText("")

    # calls update on every page
    def updateDynamicComponent(self, optional_id=None):
        self.updateDashboardPage()
        self.updateTransactionPage()
        self.udpateBillsPage()
        self.updateGoalPage()
        self.UpdatelogoutPage()
        self.updateGoalDetailPage(optional_id)
        self.updateNotification()

    def updateNotification(self):
        if self.notification.getRead():
            self.ui.notiButton.hide()
            self.ui.notiButton_2.hide()
            self.ui.notiButton_3.hide()
            self.ui.notiButton_4.hide()
            self.ui.notiButton_5.hide()
            self.ui.notiButton_6.hide()
            self.ui.notiButton_7.hide()
            self.ui.notiButton_8.hide()
            self.ui.notiButton_9.hide()
            self.ui.notiButton_10.hide()
        else:
            self.ui.notiButton.show()
            self.ui.notiButton_2.show()
            self.ui.notiButton_3.show()
            self.ui.notiButton_4.show()
            self.ui.notiButton_5.show()
            self.ui.notiButton_6.show()
            self.ui.notiButton_7.show()
            self.ui.notiButton_8.show()
            self.ui.notiButton_9.show()
            self.ui.notiButton_10.show()

    def updateDashboardPage(self):
        summary = self.curUser.getSummary()
        self.ui.currentBalanceLabel.setText(
            str("{:.2f}".format(summary.getCurrentBalance()))
        )
        textColor = (
            "green"
            if summary.getCurrentBalance() > 0
            else "red"
            if summary.getCurrentBalance() < 0
            else "black"
        )
        self.ui.currentBalanceLabel.setStyleSheet(f"color: {textColor};")
        self.ui.spentLabel.setText(str("{:.2f}".format(summary.getWeeklySpent())))
        self.ui.budgetLabel.setText(
            str("{:.2f}".format(summary.getBudget() - summary.getWeeklySpent()))
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
            for t in (summary.getTransactions())[::-1]:
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
            for g in summary.getGoals():
                count += 1
                if count > 3:
                    break
                button = QPushButton()
                button.setObjectName(str(g.getID()))  # Set object name

                button.setStyleSheet(
                    """
                    #{id} {{
                        border: 1px solid black;
                        background-color: rgb(255,255,255);
                        border-radius: 10px;
                        border-color: rgb(230, 230, 230);
                    }}
                    #{id}:pressed {{
                        background-color: rgb(192, 192, 192);
                    }}
                    """.format(
                        id=button.objectName()
                    )
                )
                button_layout = QVBoxLayout(button)
                textColor = "green" if g.getPercentage() == 100 else "black"
                top_label = QLabel(g.getName(), button)
                top_label.setStyleSheet(
                    f"QLabel {{font-size: 16px; font-weight: 600;}}"
                )
                top_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                progressStr = f'{"{:.2f}".format(g.getProgress())}/{"{:.2f}".format(g.getAmount())} ({g.getPercentage()}%)'
                bottom_label = QLabel(progressStr, button)
                bottom_label.setStyleSheet(f"QLabel {{color: {textColor};}}")
                bottom_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                button_layout.addWidget(top_label)
                button_layout.addWidget(bottom_label)
                button.setLayout(button_layout)
                button.setMinimumHeight(180)
                button.setMinimumWidth(220)
                button.clicked.connect(self.on_goal_clicked)
                self.ui.horizontalLayout.layout().addWidget(button)

    def udpateBillsPage(self):
        for i in reversed(range(self.ui.scrollArea_8.widget().layout().count())):
            self.ui.scrollArea_8.widget().layout().itemAt(i).widget().setParent(None)
        scroll_widget = self.ui.scrollArea_8.widget()
        scroll_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout = scroll_widget.layout()
        layout.setSpacing(0)  # Set spacing to 0
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Align to top

        if self.curUser:
            summary = self.curUser.getSummary()
            for b in (summary.getBills())[::-1]:
                button = QPushButton()

                button.setObjectName(str(b.getID()))  # Set object name

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

                left_label = QLabel(b.getName(), button)  # Set button as parent
                middle_label = QLabel(
                    str("{:.2f}".format(b.getAmount())), button
                )  # Set button as parent
                right_label = QLabel(
                    str(b.getDueDate().date()), button
                )  # Set button as parent

                button_layout.addWidget(left_label)
                button_layout.addWidget(middle_label)
                button_layout.addWidget(right_label)

                button.setLayout(button_layout)
                button.setMinimumHeight(50)  # Set minimum height here

                # Add bottom border to the button
                button.clicked.connect(self.on_bill_clicked)
                scroll_widget.layout().addWidget(button)

    def updateTransactionPage(self):
        for i in reversed(range(self.ui.scrollArea.widget().layout().count())):
            self.ui.scrollArea.widget().layout().itemAt(i).widget().setParent(None)
        scroll_widget = self.ui.scrollArea.widget()
        scroll_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout = scroll_widget.layout()
        layout.setSpacing(0)  # Set spacing to 0
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Align to top

        if self.curUser:
            summary = self.curUser.getSummary()
            for t in (summary.getTransactions())[::-1]:
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
            summary = self.curUser.getSummary()
            for g in (summary.getGoals())[::-1]:
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

    def updateGoalDetailPage(self, goal_id):
        summary = self.curUser.getSummary()
        if goal_id:
            goal_obj = summary.getGoalById(goal_id)
            self.ui.GoalBalanceLabel_2.setText(
                str("{:.2f}".format(goal_obj.getProgress()))
            )
            self.ui.GoalBalanceLabel_4.setText(
                str("{:.2f}".format(goal_obj.getAmount() - goal_obj.getProgress()))
            )
            self.ui.GoalBalanceLabel_5.setText(
                str("{:.2f}".format(goal_obj.getAmount()))
            )
            self.ui.progressBar.setValue(
                round(goal_obj.getProgress() / goal_obj.getAmount() * 100)
            )

    def UpdatelogoutPage(self):
        self.ui.username_account_field.setText(self.curUser.getUsername())
        self.ui.bugetField.setText(
            str("{:.2f}".format(self.curUser.getSummary().getBudget()))
        )
        self.ui.bugetField.setReadOnly(True)
        self.ui.editBudgetButton.setText("Edit")
        self.ui.ttincome.setText(
            str("{:.2f}".format(self.curUser.getSummary().calculateIncome()))
        )
        self.ui.ttexpense.setText(
            str("{:.2f}".format(self.curUser.getSummary().calculateExpense()))
        )
        self.ui.ttBalance.setText(
            str("{:.2f}".format(self.curUser.getSummary().getCurrentBalance()))
        )


# class ButtonWithLabels(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         layout = QVBoxLayout(self)
#         self.label1 = QLabel(self)
#         self.label2 = QLabel(self)
#         self.button = QPushButton("Button with Labels", self)
#         layout.addWidget(self.label1)
#         layout.addWidget(self.label2)
#         layout.addWidget(self.button)
#         self.setLayout(layout)

#     def setLabel1(self, text):
#         self.label1.setText(text)

#     def setLabel2(self, text):
#         self.label2.setText(text)


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
