from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Message Box')

def click():
    # messagebox.showwarning('Warning','Hello world!')
    # messagebox.showerror('Error','Hello world :(')

    # answer = messagebox.askquestion('Question','Hello world?')
    # print(answer)
    # if answer == "yes":
    #     messagebox.showwarning('Popup','Hello world!')
    # if answer == "no":
    #     messagebox.showerror('Error','Hello world :(')

    # answer = messagebox.askokcancel('ok cancel','Hello world?')
    # print(answer)

    answer = messagebox.askyesno('yes no','Hello world?')
    print(answer)

btn = Button(root, text='Press me', command=click)
btn.pack()

root.mainloop()