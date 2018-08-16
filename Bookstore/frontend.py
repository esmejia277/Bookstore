"""
This is a program that stores information about books:
    title, author, year, isbn.
"""
from tkinter import *
from backend import Database

database = Database()

def viewCommand():
	listB1.delete(0, END)
	for result in database.view():
		listB1.insert(END, result)

def searchCommand():
	listB1.delete(0, END)
	for result in database.search(getTitle.get(), getAuthor.get(), getYear.get(), getISBN.get()):
		listB1.insert(END, result)

def addCommand():
    database.insert(getTitle.get(), getAuthor.get(), getYear.get(), getISBN.get())
    listB1.delete(0, END)
    viewCommand()

def getSelectedRow(event): #select the records from a click
	global selected
	index = listB1.curselection()[0]
	selected = listB1.get(index)
	entryTitle.delete(0,END)
	entryTitle.insert(END, selected[1])
	entryAuthor.delete(0, END)
	entryAuthor.insert(END, selected[2])
	entryYear.delete(0,END)
	entryYear.insert(END, selected[3])
	entryISBN.delete(0,END)
	entryISBN.insert(END, selected[4])


def deleteCommand():
    database.delete(selected[0])
    viewCommand()

def updateCommand():
    database.update(selected[0], getTitle.get(), getAuthor.get(), getYear.get(), getISBN.get())
    viewCommand()

window = Tk()
window.wm_title("BookStore")

#graphic interface
labelTitle = Label(window, text = "Title: ")
labelTitle.grid(row = 0, column = 0)
labelAuthor = Label(window, text = "Author: ")
labelAuthor.grid(row = 0, column = 2)
labelYear = Label(window, text = "Year: ")
labelYear.grid(row = 1, column = 0)
labelISB = Label(window, text = "ISBN: ")
labelISB.grid(row = 1, column = 2)

#get the value of the title
getTitle = StringVar()
entryTitle = Entry(window, textvariable=getTitle)
entryTitle.grid(row = 0, column = 1)

#get the value of the author
getAuthor = StringVar()
entryAuthor = Entry(window, textvariable=getAuthor)
entryAuthor.grid(row = 0, column = 3)

#get the value of the year
getYear = StringVar()
entryYear = Entry(window, textvariable = getYear)
entryYear.grid(row = 1, column = 1)

#get the value of the ISBN
getISBN = StringVar()
entryISBN = Entry(window, textvariable = getISBN)
entryISBN.grid(row = 1, column = 3)

listB1= Listbox(window, height = 6, width = 35)
listB1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

scroll = Scrollbar(window)
scroll.grid(row = 2, column = 2, rowspan = 6)

listB1.configure(yscrollcommand = scroll.set )
scroll.configure(command = listB1.yview)

listB1.bind("<<ListboxSelect>>", getSelectedRow)

btnView = Button(window, text = "View All" , command = viewCommand)
btnView.grid(row = 2, column = 3  )

btnSearch = Button(window, text = "Search Entry", command = searchCommand)
btnSearch.grid(row = 3, column = 3  )

btnEntry = Button(window, text = "Add Entry", command = addCommand)
btnEntry.grid(row = 4, column = 3  )

btnUpdate = Button(window, text = "Update selected" , command = updateCommand)
btnUpdate.grid(row = 5, column = 3  )

btnDelete = Button(window, text = "Delete selected", command = deleteCommand)
btnDelete.grid(row = 6, column = 3  )

btnClose = Button(window, text = "Close" , command = window.destroy)
btnClose.grid(row = 7, column = 3)

window.mainloop()

#end
