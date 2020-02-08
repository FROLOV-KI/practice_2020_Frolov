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
        self.dx = rnd(-8, 8)
        self.dy = rnd(-8, 8)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r > WIDTH or self.x - self.r < 0:
            self.dx = -self.dx
        if self.y + self.r > HEIGHT or self.y - self.r < 0:
            self.dy = -self.dy

    def draw(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def check_collision(self, other_ball_info):
        # TODO: неудачная попытка реализовать столкновения. ПЕРЕДЕЛАТЬ!
        collision_distance = self.r + other_ball_info[2]
        actual_distance = ((self.x - other_ball_info[0]) ** 2 + (self.y - other_ball_info[0]) ** 2) ** 0.5
        if not actual_distance == 0:
            if actual_distance <= collision_distance:
                self.dx = other_ball_info[3]
                self.dy = other_ball_info[4]

    def is_shoot(self):
        canvas.delete(self.ball_id)

    def info(self):
        return self.x, self.y, self.r, self.dx, self.dy


def canvas_click(event):
    """Обработка клика левой кнопки мыши, регистрация поавдвния по шарику"""
    points = 0
    for ball in balls:
        target = ball.info()
        distance = ((target[0] - event.x) ** 2 + (target[1] - event.y) ** 2) ** 0.5
        if distance <= target[2]:
            print('Get {} points!'.format(50 - target[2]))
            ball.is_shoot()
            balls.remove(ball)
            points += (50 - target[2])
            if not balls or points >= 500:
                print('Победа!')
                exit()
            break
    else:
        print('miss :(')


def collisions():
    for ball in balls:
        for other_ball in balls:
            if ball is not other_ball:
                ball.check_collision(other_ball.info())
    root.after(35, collisions)


def make_new_balls():
    if len(balls) < 10:
        balls.append(Ball())
    root.after(1000, make_new_balls)


def tick():
    for ball in balls:
        ball.move()
        ball.draw()
    root.after(30, tick)


def main():
    global root, canvas, balls
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
    canvas.pack(anchor=NW, fill=BOTH)
    canvas.bind('<Button-1>', canvas_click)
    balls = []
    make_new_balls()
    tick()
    mainloop()


print('Программа закончена.')


if __name__== "__main__":
    main()