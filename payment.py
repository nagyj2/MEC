#!/usr/local/bin/python3
from connection import Connection

# Waits on user input and breaks it into an array.
# Returns: A list of user inputted values where spaces act as delimiters.
def getInput():
    command_string = input("> ")
    food_arr = [word.strip() for word in command_string.split()]
    return food_arr
    
# Checks a ticket number to determine if it is valid to operate on.
# Param: ticketno - The ticket number to check.
# Param: db - A reference to a Connection class entity to operate on. It is
#    assumed to have our defined Ticket table.
# Returns: Boolean representing if it is ok for the ticket to be paid for.
#   Returns false if the ticket number is invalid, the ticket has already been
#   paid or there is an error executing the script.
def verifyTicket(ticketno,db):
    ticketexist = "SELECT * FROM TICKET WHERE TICKETID = {}"
    ticketpaid = "SELECT STATUS FROM TICKET WHERE TICKETID = {}"
    
    # Since the query could be interrupted by a database issue or the tables are
    #   not set up properly, so surround the queries in a try statement.
    try:
        db.opencursor()
        if (not db.query(ticketexist.format(ticketno))):
            return False
        if (0 != db.query(ticketpaid.format(ticketno))[0][0]):
            return False
    except:
        return False
    finally:
        db.closecursor()
        
    return True
    
# Performs the database operation to update the status of a ticket.
# Param: ticketno - The ticket number to update.
# Param: db - A reference to the database Connection class entity to operate on.
def payTicket(ticketno, db):
    updatestatus = "UPDATE TICKET SET STATUS = 1 WHERE TICKETID = {}"

    # Like verifyTicket, an error could occur on the database side, so the
    #   operation is surrounded in a try statement.
    try:
        db.opencursor()
        
        db.query(updatestatus.format(ticketno))
    except:
        raise Exception("Invalid ticketno")
        
    finally:
        db.closecursor()
    
    
# Function to validate a given ticket
def verifyProcess(ticketno,db):
    valid = verifyTicket(ticketno,db)
    
    if (not valid):
        # raise Exception("Ticket is not valid")
        return False
        
    payTicket(ticketno, db)
    return True
    

def cli():
    print("Running payment....")
    
    db = Connection()
    db.opencnx()
    
    while True:
        action = getInput()
        
        if (action[0] == "v"):
            # Verify ticket & Set status
            try:
                ticket_no = action[1]
            except IndexError:
                print("Error: No ticket number inserted")
                continue
            
            valid = verifyTicket(ticket_no, db)
            if (not valid):
                print("Error: Ticket is invalid")
                continue
                
            # Assumed that student always pays enough
            payTicket(ticket_no, db)
            
            
        elif (action[0] == "q"):
            break
            
        else:
            print("v # : Verify ticket number\nq : Quit program")
            
            
    print("Closing...")
    db.closecnx()
        


if __name__ == "__main__":
    cli()
