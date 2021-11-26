from tkinter import *

root = Tk()
root.title('Learning option Menu')
root.geometry('500x500')

languages = ['Python', 'JavaScript', 'Java','Swift', 'GoLang', 'C#', 'C++', 'Scala']

selectedLanguage = StringVar()
selectedLanguage.set(languages[0])

def send():
    l = Label(root,text=selectedLanguage.get())
    l.pack()

btn = Button(root,text='send',command=send)
btn.pack()

optionMenu = OptionMenu(root,selectedLanguage,*languages)
optionMenu.pack()

root.mainloop()