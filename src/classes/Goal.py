import persistent


class Goal(persistent.Persistent):
    def __init__(self, name, amount, desc):
        self.__name = name
        self.__amount = amount
        self.__desc = desc

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

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
