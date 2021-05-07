from tkinter import *

top = Tk()
playlist = []

def results():
    result = E1.get()
    playlist.append(result)
    E1.delete(0, END)
def printList():
    print(playList)

def exportList():
    with open('playlist.txt', 'w') as f:
        for item in playlist:
            f.write("%s\n" % item)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "block 5 project"
    LMain.grid(column = 0, row 1)
    B1Main = Button(text =("week 1", bg= "white")
    B1Main(column= 0, row = 2)
    B2Main = Button(text = "week 2", bg= "white")
    B2Main.grid(colum= 0, row = 3)
    B3Main = Button(text = "week 3", bg = "white")
    B3Main.grid(column= 0, row = 4)
    
#This is a label widget
L1 = Label(top, text="Playlist generator")
L1.grid(column= 0, row= 1)

#this is a entry widget
E1 = Entry(top, bd = 5)
E1.grid(column= 0, row= 2)

#this is a button widget
B1 = Button(text= " + ", bg="white", command= results)
B1.grid(column= 1, row= 2)

B2 = Button(text= " + ", bg="orange", command= results)
B2.grid(column= 2, row= 2)

B3 = Button(text = "Export list", bg = "#B4FFCD", command = exportLIst)
B3.grid(column= 0, row= 3)

Bexit = Button(text= "clearWindow", bg = "red", command= clearWindow)
Bexit.grid(column= 1, row= 3)

top.mainloop()
