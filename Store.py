class Store:
    def __init__(self, Name):
        self.name = Name
        self.Tools = []
        self.rental = {}
        self.initialrental()
        self.money = 0
    def isempty(self):
        if len(self.Tools)==0:
            return True
        else:
            return False
    def addTools(self, tool):
        self.Tools.append(tool)
    def removeTools(self, tool):
        self.Tools.remove(tool)
    def ToolsInStore(self):
        return len(self.Tools)
    def showTools(self):
        for i in self.Tools:
            print(i)
    def initialrental(self):
        for i in range(10):
            self.rental[i] = []
    def rent(self, customerid, tool, days):
        temp = [tool, days]
        self.rental[customerid].append(temp)
        self.removeTools(tool)
        self.money = self.money + tool.get_price()*days

    def give_back(self, customerid, tool):
        self.addTools(tool)
        self.rental[customerid].remove([tool, 0])

