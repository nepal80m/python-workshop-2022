from tkinter import messagebox
from tkinter import *
global root
root = Tk()
root.geometry('1000x700+122+0')
root.configure(bg='#8644f4')
root.title('habibi')
root.resizable(False, False)


def nextpage():
    nxt = Frame(root).place(x=250, y=150, height=340, width=500)
    tpp = Label(nxt, text='We are in next page')
    tpp.place(x=150, y=110)


def logcheck():
    uid = str(user_entry.get())
    psw = str(pw_entry.get())

    if uid == 'hi' and psw == 'yo':
        messagebox.showinfo("", "Login Success")
        logf.destroy()
        nextpage()

    else:
        messagebox.showerror("Error", "Incorrect UserName or Password")
        # return False


# log in frame
logf = Frame(root)
logf.place(x=250, y=150, height=340, width=500)

logintitle = Label(logf, text='Log in Panel', font=(
    'impact', 35, 'bold'), bg='#8081CD', fg='darkblue')
logintitle.place(x=119, y=1)

username = Label(logf, text='Username', bg='lightblue')
username.place(x=135, y=110)
user_entry = Entry(logf)
user_entry.place(x=210, y=110)

password = Label(logf, text='Password', bg='lightblue')
password.place(x=135, y=140)

pw_entry = Entry(logf, bg='lightgray', show='*')
pw_entry.place(x=210, y=141)

login = Button(logf, text='Log in', bg='#8644f4',
               command=logcheck, cursor='hand2')
login.place(x=240, y=180)


root.mainloop()
