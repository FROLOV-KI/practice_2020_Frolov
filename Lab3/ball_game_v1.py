from tkinter import*
from random import randrange as rnd, choice
import time

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, name):
        self.name = "Ball " + str(name)
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.r = rnd(30, 50)
        self.x = rnd(self.r, WIDTH - self.r)
        self.y = rnd(self.r, HEIGHT - self.r)
        self.ball_id = canvas.create_oval((self.x - self.r, self.y - self.r), (self.x + self.r, self.y + self.r),
                                          fill=choice(self.colors), width=0)
        self.dx = rnd(1,6)
        self.dy = rnd(1,6)

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

    def is_shoot(self):
        canvas.delete(self.ball_id)

    def info(self):
        return self.name, self.x, self.y, self.r


def canvas_click(event):
    """Обработка клика левой кнопки мыши, регистрация поавдвния по шарику"""
    for ball in balls:
        target = ball.info()
        distance = ((target[1] - event.x) ** 2 + (target[2] - event.y) ** 2) ** 0.5
        if distance <= target[3]:
            print('Got {}!'.format(target[0]))
            ball.is_shoot()
            balls.remove(ball)
            break
    else:
        print('miss :(')


def tick():
    for ball in balls:
        ball.move()
        ball.draw()
    root.after(50, tick)


def main():
    global root, canvas, balls

    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
    canvas.pack(anchor="nw", fill=BOTH)
    canvas.bind('<Button-1>', canvas_click)
    balls = [Ball(i) for i in range(5)]
    tick()
    mainloop()


print('Программа закончена.')


if __name__== "__main__":
    main()