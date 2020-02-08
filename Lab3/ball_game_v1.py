from tkinter import*
from random import randrange as rnd, choice
import time

WIDTH = 1366
HEIGHT = 700


class Ball:
    def __init__(self):
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.r = rnd(10, 50)
        self.x = rnd(self.r, WIDTH - self.r)
        self.y = rnd(self.r, HEIGHT - self.r)
        self.ball_id = canvas.create_oval((self.x - self.r, self.y - self.r), (self.x + self.r, self.y + self.r),
                                          fill=choice(self.colors), width=0)
        self.dx = rnd(-6, 6)
        self.dy = rnd(-6, 6)

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
        return self.x, self.y, self.r


def canvas_click(event):
    """Обработка клика левой кнопки мыши, регистрация поавдвния по шарику"""
    points = 0
    for ball in balls:
        target = ball.info()
        distance = ((target[0] - event.x) ** 2 + (target[1] - event.y) ** 2) ** 0.5
        if distance <= target[2]:
            print('Got {} points!'.format(target[2]))
            ball.is_shoot()
            balls.remove(ball)
            points += 50 - target[2]
            if not balls or points >= 500:
                print('Победа')
                exit()
            break
    else:
        print('miss :(')


def make_new_balls():
    if len(balls) < 10:
        balls.append(Ball())
    root.after(1000, make_new_balls)


def tick():
    for ball in balls:
        ball.move()
        ball.draw()
    root.after(50, tick)


def main():
    global root, canvas, balls, num
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
    canvas.pack(anchor="nw", fill=BOTH)
    canvas.bind('<Button-1>', canvas_click)
    balls = []
    num = 0
    make_new_balls()
    tick()
    mainloop()


print('Программа закончена.')


if __name__== "__main__":
    main()