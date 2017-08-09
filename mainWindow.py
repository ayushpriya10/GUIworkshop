from tkinter import *
import tkMessageBox

window = Tk()
window.title('Registration Form')
window.geometry('300x190')


def exit():
    global window
    window.quit()

def exitMain():
    result = tkMessageBox.askquestion("Exit", "Are you sure you want to exit?", icon = 'warning')
    if result == 'yes':
        exit()

menu = Menu(window)
window.config(menu = menu)
fileMenu = Menu(menu)
aboutMenu = Menu(menu)
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "View Records")
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = exitMain)

menu.add_cascade(label = "About", menu = aboutMenu)
aboutMenu.add_command(label = "About Us")

fnameLabel = Label(window, text = 'First Name: ')
fnameLabel.place(x = 15, y = 5)
lnameLabel = Label(window, text = 'Last Name: ')
lnameLabel.place(x = 15, y = 30)

fnameEntry = Entry(window)
fnameEntry.place(x = 100, y = 5)
lnameEntry = Entry(window)
lnameEntry.place(x = 100, y = 30)

genderLabel = Label(window, text = 'Gender: ')
genderLabel.place(x = 15, y = 60)

vRB = IntVar()
maleRB = Radiobutton(window, text = 'Male', variable = vRB, value = 1)
maleRB.place(x = 90, y = 60)
femaleRB = Radiobutton(window, text = 'Female', variable = vRB, value = 2)
femaleRB.place(x = 155, y = 60)

vCB1 = IntVar()
vCB2 = IntVar()
vCB3 = IntVar()
langLabel = Label(window, text = 'Select languages: ')
langLabel.place(x = 15, y = 85)
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
eduDropMenu = OptionMenu(window, var, *choices)
eduDropMenu.place(x = 140, y = 110)

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

    okayButton = Button(infoWindow, text = 'Okay', command = infoWindow.quit)
    okayButton.place(x = 60, y = 115)
    exitButton = Button(infoWindow, text = 'Exit', command = infoWindow.quit)
    exitButton.place(x = 120, y = 115)

printButton = Button(window, text='Show Details', command = printDetails)
printButton.place(x = 125, y = 150)
exitButton = Button(window, text = 'Exit', command = exitMain)
exitButton.place(x = 235, y = 150)

window.mainloop()
