from tkinter import *

root = Tk()
root.geometry("400x300")
root.title('main')

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("Toplevel")
    l2 = Label(top, text = "Top")
    l2.pack()

    top.mainloop()

l = Label(root, text = "Window")
btn = Button(root, text = "Click Me!",
command = topwin)

l.pack()
btn.pack()
