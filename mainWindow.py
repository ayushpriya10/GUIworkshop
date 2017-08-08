from tkinter import *
import json

window = Tk()
window.title('Registration Form')

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
pythonCB = Checkbutton(window, text = 'Python', variable = vCB1)
pythonCB.grid(row = 3)
cCB = Checkbutton(window, text = 'C', variable = vCB2)
cCB.grid(row = 3, column = 1)
javaCB = Checkbutton(window, text = 'Java', variable = vCB3)
javaCB.grid(row = 3, column = 2)

def var_states():
    global vRB, vCB1, vCB2, vCB3
    print("Radio" + str(vRB.get()))
    print("Check" + str(vCB1.get()))
    print("Check" + str(vCB2.get()))
    print("Check" + str(vCB3.get()))
printButton = Button(window, text='Show', command=var_states)
printButton.grid(row = 4)
exitButton = Button(window, text = 'Exit', command=window.quit)
exitButton.grid(row = 4, column = 1)

window.mainloop()
