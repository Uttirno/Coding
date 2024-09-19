# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Length Convertor App')
root.geometry('320x250')

# Create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

# Add widgets
# Add Label
lbl1 = Label(frame, text="Inch", bg="#3895D3", fg='white', width=12)
# Use Entry Widget to create a text box for user to enter details
entry = Entry(frame)


# Function to display message
def display():
	entry2 = int(entry.get())
	t = int(entry2) * 2
	textbox.insert(END, t)


# Textbox to display message
textbox = Text(bg="#BEBEBE", fg="black")

# Add Button, when pressed, message will be displayed
btn = Button(text="Convert", command=display, bg="yellow")

# Arrange all widgets
frame.place(x=15, y=0)
lbl1.place(x=20, y=20)
entry.place(x=150, y=20)
btn.place(x=150, y=50)
textbox.place(x=0, y=150)

root.mainloop()

    

