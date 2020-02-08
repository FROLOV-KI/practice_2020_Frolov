from tkinter import*
from random import randrange as rnd, choice
import time
WIDTH = 300
HEIGHT = 200


def canvas_click(event):
    """Обработка клика левой кнопки мыши, регистрация поавдвния по шарику"""
    print(x, y, r)
    distance = ((x - event.x) ** 2 + (y - event.y) ** 2) ** 0.5
    if distance <= r:
        print('Got It!')
    else:
        print('miss :(')
    print(event.x, event.y, distance)


def tick():
    global x, y, dx, dy
    x += dx
    y += dy
    if x + r > WIDTH or x - r < 0:
        dx = -dx
    if y + r > HEIGHT or y - r < 0:
        dy = -dy
    canvas.move(ball_id, dx, dy)
    root.after(50, tick)

def main():
    global root, canvas
    global ball_id, x, y, r, dx, dy  # TODO: сделать ООП рефакторинг

    dx = 3
    dy = 3
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = Canvas(root)
    canvas.pack(anchor="nw", fill=BOTH)
    canvas.bind('<Button-1>', canvas_click)

    r = rnd(30, 50)
    x = rnd(r, WIDTH - r)
    y = rnd(r, HEIGHT - r)
    ball_id = canvas.create_oval((x-r, y-r), (x+r, y+r), fill='green', width=0)

    tick()
    mainloop()


print('Программа закончена.')


if __name__== "__main__":
    main()