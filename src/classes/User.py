import bcrypt
import persistent
from datetime import timedelta, datetime

from classes.Expense import Expense


class User(persistent.Persistent):
    salt = bcrypt.gensalt()
    # salt = 'hogriderisgigachad'
    # salt = 'mahnunitsnotevenoneminute'

    def __init__(self, username, password):
        self.__username = username
        b = password.encode("utf-8")
        self.__hashedpass = bcrypt.hashpw(b, User.salt)
        self.__transactions = []
        self.__goals = []
        # start session and assign session id?
        # store user info into database
        print("User created")

    def getTransactionById(self, transaction_id):
        for transaction in self.__transactions:
            if str(transaction.getID()) == transaction_id:
                return transaction
        return None

    def removeTransactionById(self, transaction_id):
        for transaction in self.__transactions:
            if str(transaction.getID()) == transaction_id:
                self.__transactions.remove(transaction)
                self._p_changed = True
                return

    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    def getHashedpass(self):
        return self.__hashedpass

    def getTransactions(self):
        return self.__transactions

    def addTransaction(self, transaction):
        self.__transactions.append(transaction)
        self._p_changed = True

    def addGoal(self, goal):
        self.__goals.append(goal)
        self._p_changed = True

    def getGoals(self):
        return self.__goals

    def getCurrentBalance(self):
        balance = 0
        for t in self.__transactions:
            if isinstance(t, Expense):
                balance -= t.getAmount()
            else:
                balance += t.getAmount()
        return balance

    def getWeeklySpent(self):
        spent = 0
        # get time rn minus 6 days
        lastweekDate = datetime.now() - timedelta(days=6)
        print(lastweekDate)
        for t in self.__transactions:
            if isinstance(t, Expense) and t.getDate() >= lastweekDate:
                spent += t.getAmount()
        return spent


# if __name__ == "__main__":
#     user = "test"
#     password = "12345"
#     user = User(user, password)
#     print(user.getUsername())
