from abc import ABC,abstractmethod;

class Customer(ABC):


	def __init__(self,name):
		self.name = name
		self.rental = {}

	def get_name(self，name):
		return self.name

	def rent(self, tool, days):
		self.rental[tool] = days

	def get_rental(self):
		return self.rental

	def give_back(self,tool):
		self.rental.pop(tool)

	@abstractmethod
	def get_type(self):
		pass



class Casual(Customer):
	pass

class Business(Customer):
	pass

class Regular(Customer):
	pass

