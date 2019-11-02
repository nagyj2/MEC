#!/usr/local/bin/python3
#from ticket import ticket
#from food import Food
from connection import Connection

def wait_for_cook_commandline():
	while True:
		command_string = input("Input (foodID1, foodID2.... -> ): \n")

		cmd_arr = [word.strip() for word in command_string.split(',')]
		food_entries = cmd_arr[1:]
		ticketID = cmd_arr[0]
		if check_ticket_state():
			print("Error: Ticket was not properly checked out")
		else:
			break

	assign_order(ticketID = ticketID, foodID_arr = food_entries)

def receive_cook_input(ticketID, foodID_list):

	if check_ticket_state():
		print("Error: Ticket was not properly checked out")
	else:
		assign_order(ticketID = ticketID, foodID_arr = food_entries)

def assign_order(self, ticketID, foodID_arr, quantity=1 table="assigned",):
	for food in foodID_arr:
		result = db.query("insert into {} values({}, {}, {})".format(table, ticketID, food, quantity))
		print(result)

def check_ticket_state(ticketID):
	result = dn.query("select status from ticket where ticketID = {}".format(ticketID))
	return bool(int(ticketID))

def main():

	while True:

		print("Running cookside....")
		wait_for_cook_commandline()


if __name__ == "__main__":


    db = Connection()
    db.opencnx()
    
    main()
        
    db.closecnx()
