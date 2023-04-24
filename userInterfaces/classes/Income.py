from Transaction import Transaction


class Income(Transaction):
    def __init__(self, amount, desc=''):
        super().__init__(amount)
        self.__desc = desc

    def setDesc(self, desc):
        self.__desc = desc

    def getDesc(self):
        return self.__desc
