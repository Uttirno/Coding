from tkinter import *
import datetime

today = datetime.date.today()

window = Tk()
window.geometry("400x400")
window.title("Age Calculator")

frame = Frame(master=window, height = 200, width = 360, bg="#d0efff")

lbl1 = Label(frame, text="Name", bg="#3895D3", fg='white', width=6)
lbl2 = Label(frame, text="Year", bg="#3895D3", fg='white', width=6)

name_entry = Entry(frame)
date_entry = Entry(frame)

def display():
	name = name_entry.get()
	year = today.year
	i = date_entry.get()
	yeardisplay = year - int(i)
	displayName = name
	textbox.insert(END, displayName)
	textbox.insert(END, "\n" + str(yeardisplay))


textbox = Text(bg="#BEBEBE", fg="black")

# Add Button, when pressed, message will be displayed
btn = Button(text="Create Account", command=display, bg="red")

# Arrange all widgets
frame.place(x=20, y=0)

lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
date_entry.place(x=150, y=80)
btn.place(x=130, y=210)
textbox.place(y=250)



window.mainloop()





