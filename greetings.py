from tkinter import *
def greet():
    lbl= Label(text=f'Здравствуйте,{a.get()}!', font=("Consolas", 21, "bold"), foreground='black') 
    lbl.place(x=10, y=50)
root=Tk()
root.title('Приветствие')
root.geometry('500x300')
a=Entry(root, width=10,  bg='gray', fg='white', font='consolas')
a.pack()
Button(root, text='Это я', width=10, height=2, bg='cyan',command=greet).pack()
root.mainloop() 