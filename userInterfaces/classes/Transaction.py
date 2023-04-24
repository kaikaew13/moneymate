import uuid
from datetime import datetime


class Transaction:
    def __init__(self, amount=0, date=datetime.now()):
    
        self.__amount = amount
        self.__date = datetime.now()
        # generate random uuid
        self.__id = uuid.uuid4()

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount):
        self.__amount = amount

    def updateAmount(self, amount):
        self.setAmount(amount)

    def getDate(self):
        return self.__date

    def getID(self):
        return self.__id
