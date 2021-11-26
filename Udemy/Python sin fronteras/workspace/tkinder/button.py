from tkinter import  *
import random

root = Tk()
root.title('Hello Button :D')

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
l = Label(root, text='Hello, this is a append label')
def click():
    l.config(fg=random.choice(colors))
    l.pack()

btn = Button(root, text='Click me!',command=click, fg='red', bg='white')
btn.pack()

root.mainloop()