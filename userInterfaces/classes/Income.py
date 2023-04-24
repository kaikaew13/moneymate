from Transaction import Transaction


class Income(Transaction):
    def __init__(self, name, amount, category, desc=''):
        super().__init__(amount)
        self.__category = category
        self.__desc = desc
        self.__name = name

    def setCategory(self, category):
        self.__category = category
    def getCategory(self):
        return self.__category
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def setDesc(self, desc):
        self.__desc = desc

    def getDesc(self):
        return self.__desc
