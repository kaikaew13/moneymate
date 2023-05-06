class Goal:
    def __init__(self, title, amount, desc):
        self.__title = title
        self.__amount = amount
        self.__desc = desc

    def setTitle(self, title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def setAmount(self, amount):
        self.__amount = amount

    def getAmount(self):
        return self.__amount

    def setDesc(self, desc):
        self.__desc = desc

    def getDesc(self):
        return self.__desc


if __name__ == "__main__":
    goal = Goal("test", 1000, "test")
    print(goal.getTitle())
    print(goal.getAmount())
