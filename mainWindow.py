#import statements to include the required modules
from tkinter import *
import tkMessageBox
from functools import partial

#Creating the root instance of the GUI
window = Tk()
window.title('Registration Form')
window.geometry('300x190')

#Defining exit function
def exit():
    global window
    window.quit()

#Defining exit prompt function
def exitMain():
    result = tkMessageBox.askquestion("Exit", "Are you sure you want to exit?", icon = 'warning')
    if result == 'yes':
        exit()

#Adding the Menubar
menu = Menu(window)
window.config(menu = menu)

#Headings/titles in the menubar
fileMenu = Menu(menu)
aboutMenu = Menu(menu)

#Adding options in the menubar headings
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "View Records")
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = exitMain)
menu.add_cascade(label = "About", menu = aboutMenu)
aboutMenu.add_command(label = "About Us")

#Creating labels to display text on the GUI
fnameLabel = Label(window, text = 'First Name: ')
fnameLabel.place(x = 15, y = 5)
lnameLabel = Label(window, text = 'Last Name: ')
lnameLabel.place(x = 15, y = 30)

#Creating Entry/Text boxes
fnameEntry = Entry(window)
fnameEntry.place(x = 100, y = 5)
lnameEntry = Entry(window)
lnameEntry.place(x = 100, y = 30)

genderLabel = Label(window, text = 'Gender: ')
genderLabel.place(x = 15, y = 60)

#Initialising a variable to store integer data
vRB = IntVar()

#Creating radio buttons
maleRB = Radiobutton(window, text = 'Male', variable = vRB, value = 1)
maleRB.place(x = 90, y = 60)
femaleRB = Radiobutton(window, text = 'Female', variable = vRB, value = 2)
femaleRB.place(x = 155, y = 60)

vCB1 = IntVar()
vCB2 = IntVar()
vCB3 = IntVar()
langLabel = Label(window, text = 'Select languages: ')
langLabel.place(x = 15, y = 85)

#Creating check boxes/buttons
pythonCB = Checkbutton(window, text = 'Python', variable = vCB1)
pythonCB.place(x = 135, y = 85)
cCB = Checkbutton(window, text = 'C', variable = vCB2)
cCB.place(x = 200, y = 85)
javaCB = Checkbutton(window, text = 'Java', variable = vCB3)
javaCB.place(x = 235, y = 85)

choices = ['Secondary School', 'High School', 'Graduate', 'Post Graduate']
var = StringVar(window)
dropMenuLabel = Label(window, text = 'Select Education: ')
dropMenuLabel.place(x = 15, y = 115)

#Creating a drop down menu
eduDropMenu = OptionMenu(window, var, *choices)
eduDropMenu.place(x = 140, y = 110)

#Function to display the data entered
def printDetails():
    global vRB, vCB1, vCB2, vCB3, fnameEntry, lnameEntry, var

    fname = fnameEntry.get()
    lname = lnameEntry.get()

    gender = str()
    if vRB.get() == 1:
        gender = 'Male'
    elif vRB.get() == 2:
        gender = 'Female'

    edu = var.get()

    langs = str()
    if vCB1.get() == 1:
        langs += 'Python'
    if vCB2.get() == 1:
        langs += ' C'
    if vCB3.get() == 1:
        langs += ' Java'

    #A secondary window to display entered information
    infoWindow = Tk()
    infoWindow.title('User Details')
    infoWindow.geometry('180x155')

    fnameLabel = Label(infoWindow, text = 'First Name: ' + fname)
    fnameLabel.place(x = 5, y = 5)
    lnameLabel = Label(infoWindow, text = 'last Name: ' + lname)
    lnameLabel.place(x = 5, y = 25)
    genderLabel = Label(infoWindow, text = 'Gender: ' + gender)
    genderLabel.place(x = 5, y = 45)
    langLabel = Label(infoWindow, text = 'Languages: ' + langs)
    langLabel.place(x = 5, y = 65)
    eduLabel = Label(infoWindow, text = 'Education: ' + edu)
    eduLabel.place(x = 5, y = 85)

    okayButton = Button(infoWindow, text = 'Okay', command = partial(Quit,infoWindow))
    okayButton.place(x = 60, y = 115)
    exitButton = Button(infoWindow, text = 'Exit', command = infoWindow.quit)
    exitButton.place(x = 120, y = 115)

def Quit(id):
    id.destroy()
    
printButton = Button(window, text='Show Details', command = printDetails)
printButton.place(x = 125, y = 150)
exitButton = Button(window, text = 'Exit', command = exitMain)
exitButton.place(x = 235, y = 150)

window.mainloop()
