from tkinter import*
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']


def new_ball():
    """Создание нового шарика на игровом поле"""
    global x, y, r
    canv.delete(ALL)
    r = rnd(30, 50)
    x = rnd(r, 800-r)
    y = rnd(r, 600-r)
    canv.create_oval((x-r, y-r), (x+r, y+r), fill=choice(colors), width=0)
    root.after(1000, new_ball)


def click(event):
    """Обработка клика левой кнопки мыши, регистрация поавдвния по шарику"""
    print(x, y, r)
    distance = ((x-event.x)**2 + (y - event.y)**2)**0.5
    if distance <= r:
        print('Got It!')
    else:
        print('miss :(')
    print(event.x, event.y, distance)


new_ball()
canv.bind('<Button-1>', click)
mainloop()