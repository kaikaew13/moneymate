class BillReminder:
    def __init__(self, title, amount, duedate, desc=''):
        self.__title = title
        self.__amount = amount
        self.__duedate = duedate
        self.__desc = desc

    def setTitle(self, title):
        self.__title = title

    def getTitle(self):
        return self.__title

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
