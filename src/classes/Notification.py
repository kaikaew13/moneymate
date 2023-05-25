class Notification:
    def __init__(self, goals=[], bills=[]):
        self.__read = False
        self.__goals = goals
        self.__bills = bills
        if len(self.__goals) == 0 and len(self.__bills) == 0:
            self.setRead(True)

    def setRead(self, read):
        self.__read = read

    def getRead(self):
        return self.__read

    def getBills(self):
        return self.__bills

    def getGoals(self):
        return self.__goals
