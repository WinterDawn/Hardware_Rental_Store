class Tool(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.status = False

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def is_rent(self):
        return self.status



class Painting(Tool):
    pass

class Concrete(Tool):
    pass

class Plumbing(Tool):
    pass

class Woodwork(Tool):
    pass

class Yardwork(Tool):
    pass