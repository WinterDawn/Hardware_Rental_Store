from abc import ABC, abstractmethod;

class Customer(ABC):
    def __init__(self, name):
        self._name = name
        self._rental = {}

    def get_name(self):
        return self._name

    @abstractmethod
    def rent(self, tool, days):
        pass

    def get_rental(self):
        return self._rental

    def get_returns(self):
        return_tools = []
        for t in self._rental: 
            self._rental[t] -= 1
            if self._rental[t] == 0:
                return_tools.append(t)
        return return_tools

    def return_tool(self,tool):
        self._rental.pop(tool)

    @abstractmethod
    def get_type(self):
        pass


class Casual(Customer):
    def rent(self, tools, days):
        if (len(tools)>0 and len(tools)<3 and 
            days > 0 and days <3):
            for t in tools:
                self._rental[t] = days 
            return True
        else:
            return False

    def get_type(self):
        return "Casual"

class Business(Customer):
    def rent(self, tools, days):
        if (len(tools)==3 and days == 7):
            for t in tools:
                self._rental[t] = days 
            return True
        else:
            return False

    def get_type(self):
        return "Business"

class Regular(Customer):
    def rent(self, tools, days):
        if (len(tools)>0 and len(tools)<=3 and 
            days >= 3 and days <= 5):
            for t in tools:
                self._rental[t] = days 
            return True
        else:
            return False

    def get_type(self):
        return "Regular"