from tkinter import  *

root = Tk()
root.title('hola mundo')
root.geometry('600x400')

# label = Label(root, text='Hello! this is my first labbel').pack()
l1 = Label(root, text='Hello! this is my first labbel')
l2 = Label(root, text='')
l3 = Label(root, text='STAND TALL')

# l1.pack()
l1.grid(row=0, column=0)
l2.grid(row=1, column=1)
l3.grid(row=10, column=10)



root.mainloop()