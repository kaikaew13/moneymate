from Income import Income
from Expense import Expense


class Summary:
    def __init__(self, transactions):
        self.__transactions = transactions
        self.__income = self.calculateIncomes()
        self.__expense = self.calculateExpense()
        # add graph object

    def calculateIncome(self):
        income = 0
        for i in self.__transactions:
            if isinstance(i, Income):
                income += i.getAmount()
        return income

    def calculateExpense(self):
        expense = 0
        for i in self.__transactions:
            if isinstance(i, Expense):
                expense += i.getAmount()
        return expense

    def getSummary():
        return
