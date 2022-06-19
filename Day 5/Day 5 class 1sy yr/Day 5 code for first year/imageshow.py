from tkinter import *
# from PIL import ImageTk, Image
# from pyparsing import Optional
w1 = Tk()
w1.geometry('1000x700')
# iconn = ImageTk.PhotoImage(Image.open('image/hi.jpg'))
# my_label = Label(image=iconn)
# my_label.pack()

TopImage = PhotoImage(file="image/topbar.png")
Label(w1, image=TopImage).place(x=0, y=0)

w1.mainloop()
# in terminal run
# pip install pillow

# Assignment
# Q1: make the details of your id card using Label Widget
# image(Optional)
