from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hello World')

# image = Image.open('galaxies.jpg')
# image.show()

image = ImageTk.PhotoImage(Image.open('galaxies.jpg'))

l = Label(image=image)
l.pack()

root.mainloop()