from abc import ABC,abstractmethod;

class Customer(ABC):


	def __init__(self,name):
		self.name = name
		self.rental = {}

	def get_name(self，name):
		return self.name

	def rent(self, tool, days):
		if days <= 7 and len(self.rental) <3:
			self.rental[tool] = days
			return True
		else:
			return False


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

