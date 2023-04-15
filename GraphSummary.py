from Summary import Summary


class GraphSummary(Summary):
    def __init__(self, transactions, title):
        super().__init__(transactions)
        self.__title = title

    def setTitle(self, title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def getGraphSummary(self):
        return
