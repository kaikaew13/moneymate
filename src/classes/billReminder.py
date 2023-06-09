import persistent
import uuid


class BillReminder(persistent.Persistent):
    def __init__(self, name, amount, duedate, desc=""):
        self.__name = name
        self.__amount = amount
        self.__duedate = duedate
        self.__desc = desc
        self.__id = uuid.uuid4()

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAmount(self, amount):
        self.__amount = amount

    def getAmount(self):
        return self.__amount

    def setDueDate(self, duedate):
        self.__duedate = duedate

    def getDueDate(self):
        return self.__duedate

    def setDesc(self, desc):
        self.__desc = desc

    def getDesc(self):
        return self.__desc

    def getID(self):
        return self.__id
