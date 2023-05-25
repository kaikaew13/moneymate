import persistent
import uuid


class Goal(persistent.Persistent):
    def __init__(self, name, amount, desc):
        self.__name = name
        self.__amount = amount
        self.__desc = desc
        self.__progress = 0
        self.__id = uuid.uuid4()

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

    def setProgress(self, progress):
        self.__progress = progress

    def getProgress(self):
        return self.__progress

    def getPercentage(self):
        return round(self.__progress / self.__amount * 100)

    def getID(self):
        return self.__id


# if __name__ == "__main__":
#     goal = Goal("test", 1000, "test")
#     print(goal.getTitle())
#     print(goal.getAmount())
