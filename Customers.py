from abc import ABC,abstractmethod;

class Customer(ABC):


	def __init__(self,name,does_rent,rent_time):
		self.name=name
		self.does_rent=does_rent
		self.rent_time=rent_time

	def get_name(self，name):
		return self.name

	def get_does_rent(self,does_rent):
		return self.does_rent

	def get_rent_time(self,rent_time):
		return self.rent_time

	def rent(self,does_rent):
		does_rent= True
	def returned(self,does_rent):
		does_rent= False



class Casual(Customer):
	pass
class Business(Customer):
	pass
class Regular(Customer):
	pass

