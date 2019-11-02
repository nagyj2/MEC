import os

class Ticket():
	def __init__(self, ticketID, price = 0, state="acquired"):
		self.ticketID = ticketID
		self.foodList = []
		self.state = state
		self.price = price

	def clear_ticket():
		#Logic performed after ticket is returned

	def add_food():
		#Logic to add food order (in list) to ticket

	def remove_food():
		#Logic for re-order to different food

	def change_state():
		#Logic for state change



if __name__ == "__main__":
	main()