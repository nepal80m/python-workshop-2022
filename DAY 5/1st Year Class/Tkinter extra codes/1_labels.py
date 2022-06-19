from tkinter import *
root = Tk()
root.geometry('1000x700+122+0')
root.configure(bg='#8644f4')
root.title('habibi')
root.resizable(False, False)


label1 = Label(root, text='habibi', fg='red', bg='blue',
               font=('Arial', 16)).pack(side=LEFT)
label11 = Label(
    root,
    text='habit',
    bg='red'
).pack(fill=X)
label2 = Label(
    root,
    text='habibi').place(x=1, y=1)

root.mainloop()
