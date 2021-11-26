from tkinter import  *

root = Tk()
root.title('Hello Frame :S')

labelFrame = LabelFrame(root,
    text='login',
    padx=50,
    pady=50,
    borderwidth=5)
labelFrame.pack(padx=50, pady=50)

frame = Frame(root,
    padx=50,
    pady=50,
    borderwidth=5)
frame.pack(padx=50, pady=50)

l = Label(labelFrame, text='label inside Labelframe')
b = Button(labelFrame, text='Salir', command=root.quit)
l.pack()
b.pack()

l2 = Label(frame, text='label inside frame')
b2 = Button(frame, text='Salir', command=root.quit)
l2.pack()
b2.pack()

root.mainloop()