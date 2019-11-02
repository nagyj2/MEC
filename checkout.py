# import the library
from appJar import gui


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
            total = getCheckoutTotal(ticketNum)
            message = "Your total is $", total
            yesno = app.questionBox("Payment", message)
            if yesno == True:
                print("paid")
                #call paid
                app.infoBox("Success", "Transaction Successful")
                #reset values.
                app.clearEntry("Ticket Number")
                
            else:
                print("not paid")
                
            
def getCheckoutTotal(ticketNum):
    return 10

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

