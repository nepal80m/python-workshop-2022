from ast import Delete
from tkinter import *
root = Tk()
root.geometry('500x500+100+0')
root.title('my first UI')
root.configure(bg='purple')

# txt = Label(
#     root,
#     text='the text from label',
#     fg='red',
#     bg='blue', font=('Arial', 16))
# txt.place(x=1, y=4)


def delete():
    entrybox.delete(2, END)


def showtxt():
    value = entrybox.get()
    label2 = Label(root, text=value)
    label2.place(x=12, y=30)


entrybox = Entry(root, width=70)
entrybox.place(x=14, y=60)
entrybox.insert(0, 'finally')
Button(
    root,
    text='show',
    width=10, height=10,
    command=showtxt,
    activebackground='yellow',
    cursor='hand2').place(x=14, y=80)
Button(root, text='del', command=delete).place(x=14, y=30)


root.mainloop()
