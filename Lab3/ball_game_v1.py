from tkinter import*
from random import randrange as rnd, choice

WIDTH = 1000
HEIGHT = 500


class Ball:
    def __init__(self, balls):

        self.colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.r = rnd(10, 50)
        self.x = rnd(self.r, WIDTH - self.r)
        self.y = rnd(self.r, HEIGHT - self.r)
        self.ball_id = canvas.create_oval((self.x - self.r, self.y - self.r), (self.x + self.r, self.y + self.r),
                                          fill=choice(self.colors), width=0)
        self.dx = rnd(-100, 100)/500
        self.dy = rnd(-100, 100)/500
        self.opponents = balls

    def move(self):
        if self.x + self.r + self.dx <= WIDTH or self.x + self.r + self.dx >= 0:
            self.x += self.dx
        else:
            self.x += self.x + self.r + self.dx - WIDTH

        if self.y + self.r + self.dy <= HEIGHT or self.y + self.r + self.dy >= 0:
            self.y += self.dy
        else:
            self.y += self.y + self.r + self.dy - HEIGHT

        if self.x + self.r >= WIDTH or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r >= HEIGHT or self.y - self.r <= 0:
            self.dy = -self.dy

    def draw(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def check_collision(self, other_ball_info):
        pass

    def is_shoot(self):
        canvas.delete(self.ball_id)
        points = 50 - self.r
        return points

    def info(self):
        return self.x, self.y, self.r, self.dx, self.dy


def canvas_click(event):
    """Обработка клика левой кнопки мыши, регистрация поавдвния по шарику"""
    global score
    for ball in balls:
        target = ball.info()
        distance = ((target[0] - event.x) ** 2 + (target[1] - event.y) ** 2) ** 0.5
        if distance <= target[2]:
            print('Get {} points!'.format(50 - target[2]))
            score += ball.is_shoot()
            print(score)
            balls.remove(ball)
            if not balls or score >= 500:
                print('Победа!')
                exit()
            break
    else:
        print('miss :(')

def make_new_balls():
    if len(balls) < 2:
        new = Ball(balls)
        balls.append(new)
    root.after(1000, make_new_balls)


def tick():
    for ball in balls:
        ball.move()
        ball.draw()
    root.after(1, tick)


def main():
    global root, canvas, balls, score, balls_info
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = Canvas(root, width=1.2*WIDTH, height=1.2*HEIGHT, bg='white')
    canvas.pack(anchor=NW, fill=BOTH)
    canvas.bind('<Button-1>', canvas_click)
    score = 0
    balls = []
    balls_info = []
    make_new_balls()
    tick()
    mainloop()


print('Программа закончена.')


if __name__== "__main__":
    main()