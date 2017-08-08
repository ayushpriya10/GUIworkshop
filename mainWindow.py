from tkinter import *

window = Tk()
window.title('Registration Form')

def exitMain():
    global window
    window.quit()

menu = Menu(window)
window.config(menu = menu)
fileMenu = Menu(menu)
aboutMenu = Menu(menu)
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "View Records")
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = exitMain)

menu.add_cascade(label = "About", menu = aboutMenu)
fileMenu.add_command(label = "About Us")

fnameLabel = Label(window, text = 'First Name: ')
fnameLabel.grid(row = 0)
lnameLabel = Label(window, text = 'Last Name: ')
lnameLabel.grid(row = 1)

fnameEntry = Entry(window)
fnameEntry.grid(row = 0, column = 1)
lnameEntry = Entry(window)
lnameEntry.grid(row = 1, column = 1)

genderLabel = Label(window, text = 'Gender: ')
genderLabel.grid(row = 2)

vRB = IntVar()
maleRB = Radiobutton(window, text = 'Male', variable = vRB, value = 1)
maleRB.grid(row = 2, column = 1)
femaleRB = Radiobutton(window, text = 'Female', variable = vRB, value = 2)
femaleRB.grid(row = 2, column = 2)

vCB1 = IntVar()
vCB2 = IntVar()
vCB3 = IntVar()
langLabel = Label(window, text = 'Select languages: ')
langLabel.grid(row = 3)
pythonCB = Checkbutton(window, text = 'Python', variable = vCB1)
pythonCB.grid(row = 3, column = 3)
cCB = Checkbutton(window, text = 'C', variable = vCB2)
cCB.grid(row = 3, column = 1)
javaCB = Checkbutton(window, text = 'Java', variable = vCB3)
javaCB.grid(row = 3, column = 2)

choices = ['Secondary School', 'High School', 'Graduate', 'Post Graduate']
var = StringVar(window)
dropMenuLabel = Label(window, text = 'Select Education: ')
dropMenuLabel.grid(row = 4)
eduDropMenu = OptionMenu(window, var, *choices)
eduDropMenu.grid(row = 4, column = 1)

def printDetails():
    global vRB, vCB1, vCB2, vCB3, fnameEntry, lnameEntry, var

    gender = str()
    if vRB.get() == 1:
        gender = 'Male'
    elif vRB.get() == 2:
        gender = 'Female'

    edu = var.get()
    print(edu)

    langs = str()
    if vCB1.get() == 1:
        langs += 'Python'
    if vCB2.get() == 1:
        langs += ' C'
    if vCB3.get() == 1:
        langs += ' Java'
    print(langs)

    infoWindow = Tk()
    infoWindow.title('User Details')

    text = 'First Name: %s\n\nLast Name: %s\n\nGender: %s\n\nLanguages: %s\n\nEducation: %s' %(fnameEntry.get(), lnameEntry.get(), gender, langs, edu)

    infoLabel = Label(infoWindow, text = text)
    infoLabel.pack()

    def exitInfo():
        #global infoWindow
        infoWindow.quit()

    def prevWindow():
        exitInfo()
        import mainWindow

    backButton = Button(infoWindow, text = 'Back', command = prevWindow)
    backButton.pack()
    exitButton = Button(infoWindow, text = 'Exit', command = exitInfo)
    exitButton.pack()

printButton = Button(window, text='Show', command = printDetails)
printButton.grid(row = 5, column = 1)
exitButton = Button(window, text = 'Exit', command = exitMain)
exitButton.grid(row = 5, column = 2)

window.mainloop()
