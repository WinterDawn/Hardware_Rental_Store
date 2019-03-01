class Store:
    def __init__(self, Name):
        self.__name = Name
        self._Tools = []
        self._rental = []
        self._income = 0

    def get_name(self):
        return self.__name

    def is_empty(self):
        if len(self._Tools)==0:
            return True
        else:
            return False

    def addTools(self, tool):
        self._Tools.append(tool)

    def __removeTools(self, tool):
        self._Tools.remove(tool)

    def num_tools(self):
        return len(self._Tools)

    def get_tools(self):
        return self._Tools

    def get_rental(self):
        return self._rental
    
    def get_income(self):
        return self._income

    def rent(self, customer, tool, days):
        payment = tool.get_price()*days
        self._income = self._income + payment
        record = {"customer":customer,"tool":tool,"nights": days,"price": payment, "active": True}
        self._rental.append(record)
        self.__removeTools(tool)
        

    def give_back(self, customer, tool):
        self.addTools(tool)
        for r in self._rental:
            if (r["customer"] == customer and
                r["tool"] == tool and
                r["active"]):
                r["active"] = False

