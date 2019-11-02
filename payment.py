#!/usr/local/bin/python3
from connection import Connection

def getInput():
    command_string = input("> ")
    food_arr = [word.strip() for word in command_string.split()]
    return food_arr
    
def verifyTicket(ticketno,db):
    ticketexist = "SELECT * FROM TICKET WHERE TICKETID = {}"
    ticketpaid = "SELECT STATUS FROM TICKET WHERE TICKETID = {}"
    
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
    
def payTicket(ticketno, db):
    updatestatus = "UPDATE TICKET SET STATUS = 1 WHERE TICKETID = {}"

    try:
        db.opencursor()
        
        db.query(updatestatus.format(ticketno))
    except:
        raise Exception("Invalid ticketno")
        
    finally:
        db.closecursor()
    
    
def verifyProcess(ticketno,db):
    valid = verifyTicket(ticketno,db)
    
    if (not valid):
        raise Exception("Ticket is not valid")
        
    payTicket(ticketno, db)
    

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
