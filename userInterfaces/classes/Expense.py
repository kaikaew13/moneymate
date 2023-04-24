from Transaction import Transaction

# expense categories (to add more)
FOOD = 'Food'
UTILITIES = 'Utilities'
ENTERTAINMENT = 'Entertainment'
CLOTHING = 'Clothing'
TRAVEL = 'Travel'
TAX = 'Tax'
PERSONAL = 'Personal'


class Expense(Transaction):
    def __init__(self, amount, category, desc=''):
        super().__init__(amount)
        self.__category = category
        self.__desc = desc

    def setCategory(self, category):
        self.__category = category

    def getCategory(self):
        return self.__category

    def setDesc(self, desc):
        self.__desc = desc

    def getDesc(self):
        return self.__desc
