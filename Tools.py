from abc import ABC, abstractmethod

class Tool(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._status = False

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def is_rent(self):
        return self._status

    def rent(self):
        self._status = True

    def returned(self):
        self._status = False

    @abstractmethod
    def get_type(self):
        pass



class Painting(Tool):
    def get_type(self):
        return "Painting"

class Concrete(Tool):
    def get_type(self):
        return "Concrete"

class Plumbing(Tool):
    def get_type(self):
        return "Plumbing"

class Woodwork(Tool):
    def get_type(self):
        return "Woodwork"

class Yardwork(Tool):
    def get_type(self):
        return "Yardwork"