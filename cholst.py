from tkinter import *
from random import *
window=Tk()
window.title('Холст')
window.geometry('500x500')
canvas = Canvas(window, height=400, width=400, bg="#ccf9ff")
def clicked():
    canvas.delete('all')
    x = choice([0,3,4])
    if x == 4: canvas.create_rectangle(30,30,370,370)
    if x == 3: canvas.create_polygon(30,30,370,30,185,185*3**0.5)
    if x == 0: canvas.create_oval(30,30,370,370)
    
Button(window, text='Построить n-угольник', width=20, height=2, bg='cyan',command=clicked).pack()
canvas.pack()
window.mainloop()