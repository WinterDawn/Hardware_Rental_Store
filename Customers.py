from abc import ABC, abstractmethod
from random import randint, choices, sample

class Customer(ABC):
    def __init__(self, name):
        self._name = name
        self._rental = {}

    def get_name(self):
        return self._name

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

    @abstractmethod
    def rent(self, tool, days):
        pass

    @abstractmethod
    def make_rent(self,store):
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

    def make_rent(self,store):
        if store.num_tools() > 1:
            rent_tools = sample(store.get_tools(),k=randint(1,2))
            nights = randint(1,2)
            self.rent(rent_tools,nights)
            for rt in rent_tools:
                rt.rent()
                store.rent(self,rt,nights)
        else:
            rent_tools = store.get_tools()
            nights = randint(1,2)
            self.rent(rent_tools,nights)
            rent_tools[0].rent()
            store.rent(self,rent_tools[0],nights)

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

    def make_rent(self,store):
        rent_tools = sample(store.get_tools(),k=3)
        self.rent(rent_tools,7)
        for rt in rent_tools:
            rt.rent()
            store.rent(self,rt,7)

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

    def make_rent(self,store):
        if store.num_tools() >= 3:
            rent_tools = sample(store.get_tools(),k=randint(1,3))
            nights = randint(3,5)
            self.rent(rent_tools,nights)
            for rt in rent_tools:
                rt.rent()
                store.rent(self,rt,nights)
        elif store.num_tools() ==2 :
            rent_tools = sample(store.get_tools(),k=randint(1,2))
            nights = randint(3,5)
            self.rent(rent_tools,nights)
            for rt in rent_tools:
                rt.rent()
                store.rent(self,rt,nights)
        else:
            rent_tools = store.get_tools()
            nights = randint(3,5)
            self.rent(rent_tools,nights)
            rent_tools[0].rent()
            store.rent(self,rent_tools[0],nights)

    def get_type(self):
        return "Regular"