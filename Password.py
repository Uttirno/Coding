from tkinter import *

root = Tk()
root.geometry("200x200")
root.title("Password Length Checker")


lb1 = Label(root, text="Password")
password_entry = Entry(root, show = "*")

def display():
    l = int(len(password_entry.get()))
    if l <= 5:
        print("Weak")
    if l > 5:
        print("Medium")
    if l>8:
        print("Strong")
    if l > 12:
        print("Very Strong")

btn = Button(root, text = "Check", command = display)

lb1.place(x=50, y=50)
password_entry.place(x=50, y=100)
btn.place(x=50, y=150)
