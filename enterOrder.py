# import the library
from appJar import gui

#set dictionary
items = {
  "sandwich": 4,
  "wrap": 3,
  "fries": 2,
  "drink": 1,
  "pizza": 5
}

#validate entry
def checkentry():
    validEntry = True

    if app.getEntry("Ticket Number") == "":
        app.infoBox("Error", "Please enter Ticket number.")
        validEntry = False

    if validEntry:
        if app.getOptionBox("Sandwich") == "0" and app.getOptionBox("Wrap") == "0" and app.getOptionBox("Fries") == "0"and app.getOptionBox("Drink") == "0" and app.getOptionBox("Pizza") == "0":
            app.infoBox("Error", "Please select food quantity.")
            validEntry = False

    return validEntry

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        if checkentry():
            ticketNum = app.getEntry("Ticket Number")

            food = []
            for i in range(0,int(app.getOptionBox("Sandwich"))):
                food.append(items["sandwich"])

            for i in range(0,int(app.getOptionBox("Wrap"))):
                food.append(items["wrap"])

            for i in range(0,int(app.getOptionBox("Pizza"))):
                food.append(items["pizza"])

            for i in range(0,int(app.getOptionBox("Fries"))):
                food.append(items["fries"])

            for i in range(0,int(app.getOptionBox("Drink"))):
                food.append(items["drink"])
            
            print("User:", ticketNum, " ", food)

            app.infoBox("Success", "Submission Successful")
            app.clearEntry("Ticket Number")
            app.clearOptionBox("Sandwich")
            app.clearOptionBox("Wrap")
            app.clearOptionBox("Pizza")
            app.clearOptionBox("Fries")
            app.clearOptionBox("Drink")

            #callAlex() #inputs to database

            

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

app.addLabelOptionBox("Sandwich", ["0","1","2","3","4","5"])
app.addLabelOptionBox("Wrap", ["0","1","2","3","4","5"])
app.addLabelOptionBox("Pizza", ["0","1","2","3","4","5"])
app.addLabelOptionBox("Fries", ["0","1","2","3","4","5"])
app.addLabelOptionBox("Drink", ["0","1","2","3","4","5"])

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

def createTicket():
    #call create ticket
    return True

app.addButtons(["Create Ticket"], createTicket)

app.setFocus("Ticket Number")

# start the GUI
app.go()
