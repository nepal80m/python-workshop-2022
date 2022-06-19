from cgitb import text
from tkinter import *

ws = Tk()
ws.title('yoo')
ws.geometry('400x300')
ws.config(bg='#84BF04')

# message = '''
# Dear Reader,
# The h in programming is Happiness

#  '''


def deletes():
    text_box.delete('1.0', 'end')


def extract_data():
    print(text_box.get('1.0', 'end'))
    mylb = Label(
        ws,
        text=text_box.get('1.0', 'end')
    ).pack()


text_box = Text(
    ws,
    height=12,
    width=40
)
Button(ws, text='show', command=extract_data).place(x=0, y=200)
Button(ws, text='delete', command=deletes).place(x=50, y=200)
# text_box.pack(expand=True)
text_box.place(x=10, y=20)
# text_box.insert('end', message)
text_box.insert('1.0', 'hi')
text_box.insert('1.0', 'yoo')
text_box.insert('2.0', 'what is this life')
# text_box.config(state='disabled')

# l_appointe = Text(form, height=8, width=50)
# l_appointe.place(x=150, y=410)

ws.mainloop()


# def extract_data():
# print(text_box.get('1.0', 'end'))


# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('400x300')
# ws.config(bg='#84BF04')


# message ='''
# One
# Two
# Three
# Four
# Five
# Six
# Seven
# Eight
# Nine
# Ten
# eleven
# twelve
# thirteen
# fourteen
# fifteen
# sixteen
# seventeen
# eighteen
# nineteen
# twenty

# '''

# frame = Frame(ws)

# text_box = Text(
#     frame,
#     height=13,
#     width=20,
#     wrap='word'
# )
# text_box.insert('end', message)
# text_box.pack(side=LEFT,expand=True)


# sb = Scrollbar(frame)
# sb.pack(side=RIGHT, fill=BOTH)

# text_box.config(yscrollcommand=sb.set)
# sb.config(command=text_box.yview)

# frame.pack(expand=True)

# ws.mainloop()
