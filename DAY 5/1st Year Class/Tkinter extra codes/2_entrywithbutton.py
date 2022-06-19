from tkinter import *
root = Tk()
root.geometry('500x500')


def click():
    value = txt.get()
    labelsh = Label(root, text=value)
    # labelsh.place(x=150, y=300)
    labelsh.pack()  # prints in open space


def delete():
    txt.delete(1, END)


txt = Entry(root, bg='yellow', width=50)
txt.place(x=100, y=0)
txt.insert(0, 'Username')

mybtn = Button(root,
               text='show',
               command=click,
               bg='red',
               fg='yellow',
               activebackground='yellow',
               height=2,
               width=20)
mybtn.place(x=150, y=100)

mybtn2 = Button(root,
                text='Delete',
                command=delete,
                height=2,
                width=20)
mybtn2.place(x=150, y=150)

root.mainloop()
