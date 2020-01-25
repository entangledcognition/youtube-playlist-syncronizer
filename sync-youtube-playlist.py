from Tkinter import *
import Tkinter
import Tkconstants
import tkFileDialog

root = Tk()

root.geometry('350x200')
root.title("Welcome to Youtube PLaylist Synchronizer")

lbl = Label(root, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)


def clicked():
    lbl.configure(text="Button was clicked !!")


btn = Button(root, text="Click Me", bg="orange", fg="red", command=clicked)
btn.grid(column=1, row=0)

root.filename = filedialog.askdirectory()

root.mainloop()
print(root.filename)
