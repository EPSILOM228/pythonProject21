from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry('300x300')
window['bg']='red'

name1 = Label(text='Фамилия', fg='white', bg='black')
name1.pack()
frame2 = Frame(master=window, bg = 'blue', borderwidth=3, relief=SUNKEN)
frame2.pack()
line1=Entry(master=frame2)
line1.pack()
name2 = Label(text='Имя', fg='white', bg='black')
name2.pack()
line2=Entry()
line2.pack()




def save():
    x = line1.get()
    x2 = line2.get()
    lin= f'Данные пользователя: {str(x)},{str(x2)}'
    messagebox.showinfo(message=lin)

frame = Frame(master=window, bg = 'blue', borderwidth=3, relief=SUNKEN)
frame.pack()

clik1 = Button(master=frame, text='Сохранить все', command=save)
clik1.pack()
#clik1.place(x=70, y = 150)
#clik1.place(x=70, y = 150)
#clik1.place(x=70, y = 150)м#clik1.place(x=70, y = 150)
#clik1.place(x=70, y = 150)м#clik1.place(x=70, y = 150)



def Clear():
   x =line1.delete(0, END)
   x2 = line2.delete(0,END)

clik2 = Button(text='Очистить', command=Clear)
clik2.pack()
#clik2.place(x=150, y = 150)

window.mainloop()