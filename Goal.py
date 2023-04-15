class Goal:
    def __init__(self, title, amount):
        self.__title = title
        self.__amount = amount

    def setTitle(self, title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def setAmount(self, amount):
        self.__amount = amount

    def getAmount(self, amount):
        return self.__amount
