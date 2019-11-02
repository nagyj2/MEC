#!/usr/local/bin/python3
#from ticket import ticket
#from food import Food
from connection import Connection

def wait_for_cook_commandline():
    command_string = input("Input (foodID1, foodID2.... -> ): \n")

    cmd_arr = [word.strip() for word in command_string.split(',')]
    food_entries = cmd_arr[1:]

    assign_order(ticketID = cmd_arr[0], foodID_arr = food_entries)

def assign_order(self, table="assigned", ticketID, foodID_arr, quantity=1):
	for food in foodID_arr:
		result = db.query("insert into {} values({}, {}, {})".format(table, ticketID, food, quantity))
		print(result)
	
def main():

	while True:

    print("Running cookside....")
    wait_for_cook_commandline()


if __name__ == "__main__":


    db = Connection()
    db.opencnx()
    
    main()
        
    db.closecnx()
