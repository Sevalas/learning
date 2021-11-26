from tkinter import  *
import random

root = Tk()
root.title('Hello Input :S')
root.geometry('500x500')
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

e = Entry(root, width=50)
e.pack()
e.insert(0,'insert the text here')

def click(event=None):
    text = e.get()
    l.configure(fg=random.choice(colors))
    textvariable.set(text)
    e.delete(0, END)

b = Button(root, text='Click me', command=click)
b.pack()

root.bind('<Return>',click)

textvariable = StringVar()
l = Label(textvariable=textvariable)
l.pack()

root.mainloop()