# import the library
from appJar import gui
from payment import verifyTicket, payTicket
from connection import Connection

db = Connection()
db.opencnx()

#validate entry
def checkentry():
    validEntry = True

    if app.getEntry("Ticket Number") == "":
        app.infoBox("Error", "Please enter Ticket number.")
        validEntry = False
    
    return validEntry

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        if checkentry():
            ticketNum = app.getEntry("Ticket Number")
            
            if (verifyTicket(ticketNum,db)):
            
                total = getCheckoutTotal(ticketNum)
                message = "Your total is $", total
                yesno = app.questionBox("Payment", message)
                
                if yesno == True:
                    completed = payTicket(ticketNum,db)
                    #call paid
                    if (completed):
                        app.infoBox("Success", "Transaction Successful")
                        #reset values.
                        app.clearEntry("Ticket Number")
                    else:
                        print("Unknown Error")
                
            else:
                app.infoBox("Failure", "Invalid ticket number")
                
            
def getCheckoutTotal(ticketNum):
    getprice = "SELECT Price FROM Ticket WHERE TicketID = {}"
    
    db.opencursor()
    answer = db.query(getprice.format(ticketNum))
    db.closecursor()
    
    return answer

# create a GUI variable called app
app = gui("Login Window", "400x200")
app.setBg("orange")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to Quick Checkout")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

# add labels and entries
app.addLabelEntry("Ticket Number")

# link the buttons to the function called press
app.addButtons(["Pay", "Cancel"], press)

#app.setFocus("Username")
app.setFocus("Ticket Number")

# start the GUI
app.go()
db.closecnx()
