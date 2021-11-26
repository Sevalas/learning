from tkinter import *

root = Tk()
root.title('Sliders learning')

def send():
    horizontaScale = sliderVertical.get()
    verticalScale = sliderHorizontal.get()
    print(horizontaScale,verticalScale)

sliderVertical = Scale(root, from_=0, to=200, orient=VERTICAL)
sliderVertical.pack()

sliderHorizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
sliderHorizontal.pack()

btn = Button(root,text='Send',command=send)
btn.pack()

root.mainloop()