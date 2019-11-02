#!/usr/local/bin/python3
from .. import connection_library as CL

def getInput():
    command_string = input("Input (foodID1, foodID2.... -> )")
    food_arr = [word.strip() for word in command_string.split(',')]
    return food_arr
    
def verifyTicket(ticketno,db):
    ticketexist = "SELECT * FROM TICKET WHERE TICKETID = {}"
    db.opencursor()
    
    if (not db.query(ticketexist.format(ticketno))):
        return False
    
    db.closecursor()
    return True

def cli():
    print("Running payment....")
    
    db = CL.Connection()
    db.opencnx()
    
    while True:
        action = getInput()
        
        if (action[0] == "v"):
            # Verify ticket & Set status
            ticket_no = action[1]
            
            valid = verifyTicket(ticket_no, db)
            print(valid)
            
            
    db.closecnx()
        


if __name__ == "__main__":
    cli()
