class Store:
    def __init__(self, Name):
        self.name = Name
        self.Tools = []
        self.rental = []
        self.income = 0

    def isempty(self):
        if len(self.Tools)==0:
            return True
        else:
            return False

    def addTools(self, tool):
        self.Tools.append(tool)

    def removeTools(self, tool):
        self.Tools.remove(tool)

    def num_tools(self):
        return len(self.Tools)

    def get_tools(self):
        return self.Tools

    def get_rental(self):
        return self.rental
    
    def get_income(self):
        return self.income

    # def initialrental(self):
    #     for i in range(10):
    #         self.rental[i] = []

    def rent(self, customer, tool, days):
        payment = tool.get_price()*days
        self.income = self.income + payment
        record = {"customer":customer,"tool":tool,"nights": days,"price": payment, "active": True}
        self.rental.append(record)
        self.removeTools(tool)
        

    def give_back(self, customer, tool):
        self.addTools(tool)
        for r in self.rental:
            if (r["customer"] == customer and
                r["tool"] == tool and
                r["active"]):
                r["active"] = False

