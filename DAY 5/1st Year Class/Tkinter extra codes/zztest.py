from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('500x500')

icon = ImageTk.PhotoImage(Image.open('image/hi.png'))
my_label = Label(image=icon)
my_label.pack()
# icon = PhotoImage(file="image/hi.png")
# Button(root, image=icon).place(x=0, y=0, relheight=1, relwidth=1)

root.mainloop()
