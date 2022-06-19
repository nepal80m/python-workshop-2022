# from lib2to3.pgen2.literals import test
from tkinter import *
root = Tk()
root.geometry('400x400')


def delete():
    my_listbox.delete(ANCHOR)


def select():
    my_label.config(text=my_listbox.get(ANCHOR))


my_listbox = Listbox(root, cursor='hand2')
my_listbox.place(x=15, y=15)

my_listbox.insert(0, 'hi')
my_listbox.insert(END, 'HMM')
my_button = Button(root, text='Delete', command=delete)
my_button.place(y=200)

my_button2 = Button(root, text='Select', command=select)
my_button2.place(y=300)

my_label = Label(root, text='')
my_label.place(y=350)


root.mainloop()
