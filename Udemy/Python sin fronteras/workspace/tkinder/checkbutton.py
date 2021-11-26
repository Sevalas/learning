from tkinter import *

root = Tk()
root.title('checkbutton learning')

root.geometry('500x500')

checkButtonValue = BooleanVar()

checkButton = Checkbutton(root, text="im a checkbutton", variable=checkButtonValue, onvalue=True, offvalue=False)
checkButton.pack()

btn = Button(root, text='click', command=lambda: print(checkButtonValue.get()))
btn.pack()

root.mainloop()