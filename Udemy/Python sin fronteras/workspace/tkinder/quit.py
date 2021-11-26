from tkinter import *

root = Tk()
root.title('Hello World')

exit = Button(root, text='Exit', command=root.quit)
exit.pack()
root.mainloop()