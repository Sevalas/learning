from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('window learning')

# First Solution
# def open():
#     image = ImageTk.PhotoImage(Image.open('carrusel\galaxies.jpg'))
#     top = Toplevel()
#     top.title('This is a new Window')
#     Label(top,text='hi, world').pack()
#     Label(top,image=image).pack()
#     top.mainloop()

# Second Solution
# def open():
#     global image
#     image = ImageTk.PhotoImage(Image.open('carrusel\galaxies.jpg'))
#     top = Toplevel()
#     top.title('This is a new Window')
#     Label(top,text='hi, world').pack()
#     Label(top,image=image).pack()

# Third Solution
def open(image):
    top = Toplevel()
    top.title('This is a new Window')
    Label(top,text='hi, world').pack()
    Label(top,image=image).pack()

# For First and Second Option
# Button(root, text="Open new Window", command=open).pack()

image = ImageTk.PhotoImage(Image.open('carrusel\galaxies.jpg'))
Button(root, text="Open new Window", command=lambda: open(image)).pack()

root.mainloop()