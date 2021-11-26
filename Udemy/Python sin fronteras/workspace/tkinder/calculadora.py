from tkinter import *

root = Tk()
root.title('Feet to Meter converter')

def calculate(*args):
    try:
        value = float(feets.get())
        m = float(value/3.2808)
        meters.set(round(m,2))
    except  ValueError:
        meters.set('ERROR')

frame = Frame(root, pady=3, padx=12)
frame.grid(column=0, row=0)

Label(frame, text='Feets').grid(column=0,row=0)

feets = StringVar()
feetsInput = Entry(frame, width=7, textvariable=feets)
feetsInput.grid(column=1, row=0, sticky='nesw')

Label(frame, text='Is equal to').grid(column=0,row=1)

meters = StringVar()
metersInput = Label(frame, textvariable=meters)
metersInput.grid(column=1, row=1)

Label(frame, text='Meters').grid(column=2,row=1)

Button(frame, text="Calculate", command=calculate).grid(column=2,row=2)

feetsInput.focus()
root.bind("<Return>",calculate)

root.mainloop()