'''
test
'''

from tkinter import *
from student import Student
from IOPrototype import readFile
from logService import *

studentQ = []
roster = readFile(studentQ)

window = Tk()
window.title("Cold Call")
window.geometry('350x200')
name1 = Label(window, text=roster[0].getFName() +" "+ roster[0].getLName())
name1.grid(column=0, row=0)

name2 = Label(window, text=roster[1].getFName() +" "+ roster[1].getLName())
name2.grid(column=1, row=0)

name3 = Label(window, text=roster[2].getFName() +" "+ roster[2].getLName())
name3.grid(column=2, row=0)

def remove():
	removeName = roster[0]
	removeName.correctQ += 1
	removeName.calledOnCount += 1
	del roster[0]
	newR = roster
	
	name1.config(text=newR[0].getFName() + newR[0].getLName())
	name2.config(text=newR[1].getFName() + newR[1].getLName())
	name3.config(text=newR[2].getFName() + newR[2].getLName())

	dailyRemove(removeName)

	roster.append(removeName)

removeB = Button(window, text="Remove",command=remove)
removeB.grid(column=0,row=1)

def concern():
	removeName = roster[-1]
	removeName.correctQ -= 1
	dailyConcern(removeName)

def summidk():
	return summary()

concernB = Button(window, text="Concern",command=concern)
concernB.grid(column=1,row=1)

summ = Button(window, text="Summary",command=summidk)
summ.grid(column=2,row=1)


window.mainloop()