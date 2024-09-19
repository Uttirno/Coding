# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Login App')
root.geometry('400x400')

# Create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

# Add widgets
# Add Label
lbl1 = Label(frame, text="Number 1", bg="black", fg='white', width=12)
lbl2 = Label(frame, text="Number 2", bg="black", fg='white', width=12)

# Use Entry Widget to create a text box for user to enter details
no1e = Entry(frame)
no2e = Entry(frame)


# Function to display message
def display():
	no1 = no1e.get()
	no2 = no2e.get()
	textbox.insert(END, int(no1) * int(no2))



# Textbox to display message
textbox = Text(bg="white", fg="black")

# Add Button, when pressed, message will be displayed
btn = Button(text="Create Account", command=display, bg="blue")

# Arrange all widgets
frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
no1e.place(x=150, y=20)
lbl2.place(x=20, y=80)
no2e.place(x=150, y=80)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()

    

