import bcrypt
import persistent
from datetime import timedelta, datetime

from classes.Expense import Expense
from classes.Summary import Summary


class User(persistent.Persistent):
    salt = bcrypt.gensalt()
    # salt = 'hogriderisgigachad'
    # salt = 'mahnunitsnotevenoneminute'

    def __init__(self, username, password):
        self.__username = username
        b = password.encode("utf-8")
        self.__hashedpass = bcrypt.hashpw(b, User.salt)
        self.__summary = Summary()
        # self.__transactions = []
        # self.__goals = []
        # self.__bills = []
        # self.__budget = 2500
        # store user info into database (done)
        # print("User created")

    # def getTransactionById(self, transaction_id):
    #     for transaction in self.__transactions:
    #         if str(transaction.getID()) == transaction_id:
    #             return transaction
    #     return None

    # def removeTransactionById(self, transaction_id):
    #     for transaction in self.__transactions:
    #         if str(transaction.getID()) == transaction_id:
    #             self.__transactions.remove(transaction)
    #             self._p_changed = True
    #             return

    # def removeGoalById(self, goal_id):
    #     for goal in self.__goals:
    #         if str(goal.getID()) == goal_id:
    #             self.__goals.remove(goal)
    #             self._p_changed = True
    #             return

    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    def getHashedpass(self):
        return self.__hashedpass

    def getSummary(self):
        return self.__summary

    # def getTransactions(self):
    #     return self.__transactions

    # def addTransaction(self, transaction):
    #     self.__transactions.append(transaction)
    #     self._p_changed = True

    # def addGoal(self, goal):
    #     self.__goals.append(goal)
    #     self._p_changed = True

    # def addBill(self, bill):
    #     self.__bills.append(bill)
    #     self._p_changed = True

    # def getBills(self):
    #     return self.__bills

    # def getGoals(self):
    #     return self.__goals

    # def setBudget(self, budget):
    #     self.__budget = budget

    # def getBudget(self):
    #     return self.__budget

    # def getCurrentBalance(self):
    #     balance = 0
    #     for t in self.__transactions:
    #         if isinstance(t, Expense):
    #             balance -= t.getAmount()
    #         else:
    #             balance += t.getAmount()
    #     return balance

    # def editTransaction(self, transaction_id, name, amount, category, description):
    #     for transaction in self.__transactions:
    #         if str(transaction.getID()) == transaction_id:
    #             transaction.setName(name)
    #             transaction.setAmount(float(amount))
    #             transaction.setCategory(category)
    #             transaction.setDesc(description)
    #             print(transaction.getName())

    #             self._p_changed = True
    #             print("Transaction edited")
    #             return True
    #     return False

    # def editGoal(self, goal_id, name, amount, description):
    #     for goal in self.__goals:
    #         if str(goal.getID()) == goal_id:
    #             goal.setName(name)
    #             goal.setAmount(float(amount))
    #             goal.setDesc(description)
    #             self._p_changed = True
    #             return True
    #     return False

    # def addFund(self, goal_id, fund):
    #     for goal in self.__goals:
    #         if str(goal.getID()) == goal_id:
    #             goal.setProgress(goal.getProgress() + fund)
    #             self._p_changed = True
    #             return True
    #     return False

    # def defund(self, goal_id, defund):
    #     for goal in self.__goals:
    #         if str(goal.getID()) == goal_id:
    #             goal.setProgress(goal.getProgress() - defund)
    #             self._p_changed = True
    #             return True
    #     return False

    # # starts counting from closest Monday
    # def getWeeklySpent(self):
    #     spent = 0
    #     # get time rn minus 6 days
    #     monday = datetime.now()
    #     for i in range(0, 7):
    #         if (monday - timedelta(days=i)).weekday() == 0:
    #             monday -= timedelta(days=i)
    #             break
    #     for t in self.__transactions:
    #         print(t.getDate())
    #         if isinstance(t, Expense) and t.getDate().date() >= monday.date():
    #             spent += t.getAmount()
    #     return spent

    # def getGoalById(self, goal_id):
    #     for goal in self.__goals:
    #         if str(goal.getID()) == goal_id:
    #             return goal
    #     return None


# if __name__ == "__main__":
#     user = "test"
#     password = "12345"
#     user = User(user, password)
#     print(user.getUsername())
