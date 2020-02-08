from tkinter import*
from random import randrange as rnd, choice
import time

WIDTH = 300
HEIGHT = 200


class BALL:
    def __init__(self):
        self.r = rnd(30, 50)
        self.x = rnd(self.r, WIDTH - self.r)
        self.y = rnd(self.r, HEIGHT - self.r)
        self.ball_id = canvas.create_oval((self.x - self.r, self.y - self.r), (self.x + self.r, self.y + self.r),
                                          fill='green', width=0)
        self.dx = 3
        self.dy = 3

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r > WIDTH or self.x - self.r < 0:
            self.dx = -self.dx
        if self.y + self.r > HEIGHT or self.y - self.r < 0:
            self.dy = -self.dy

    def draw(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def collision(self):
        pass

    def interception(self):
        pass


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
    global ball
    ball.move()
    ball.draw()
    root.after(50, tick)


def main():
    global root, canvas, ball

    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = Canvas(root)
    canvas.pack(anchor="nw", fill=BOTH)
    canvas.bind('<Button-1>', canvas_click)
    ball = BALL()


    tick()
    mainloop()


print('Программа закончена.')


if __name__== "__main__":
    main()