from tkinter import *

root = Tk()
root.title('Hola Mundo')

r = StringVar()
r.set('Selected option is 5')

for index in range(7):
    Radiobutton(root, text='Option '+str(index), variable=r, value='Selected option is '+str(index)).pack()

l = Label(root, textvariable=r)
l.pack()

root.mainloop()