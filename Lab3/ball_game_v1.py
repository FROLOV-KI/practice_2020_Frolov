from tkinter import*
from random import randrange as rnd, choice

WIDTH = 1300
HEIGHT = 700


class Ball:
    def __init__(self, balls)
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.r = rnd(10, 50)
        self.x = rnd(self.r, WIDTH - self.r)
        self.y = rnd(self.r, HEIGHT - self.r)
        self.ball_id = canvas.create_oval((self.x - self.r, self.y - self.r), (self.x + self.r, self.y + self.r),
                                          fill=choice(self.colors), width=0)
        self.dx = rnd(-100, 100)/50
        self.dy = rnd(-100, 100)/50
        self.opponents = balls

    def move(self):
        """Движение в рамках холста"""
        if self.x + self.r + self.dx <= WIDTH or self.x + self.r + self.dx >= 0:
            self.x += self.dx
        else:
            self.x += self.x + self.r + self.dx - WIDTH

        if self.y + self.r + self.dy <= HEIGHT or self.y + self.r + self.dy >= 0:
            self.y += self.dy
        else:
            self.y += self.y + self.r + self.dy - HEIGHT
        """Столкновение со стенкой"""
        if self.x + self.r >= WIDTH or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r >= HEIGHT or self.y - self.r <= 0:
            self.dy = -self.dy

    def draw(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def check_collision(self):
        for ball in self.opponents:
            x = ball.info()[0]
            y = ball.info()[1]
            if x != self.x and y != self.y:
                r = ball.info()[2]
                distance = ((x - self.x)**2 + (y - self.y)**2)**0.5
                print("dist{0}: ".format(str(self.ball_id)), distance)
                print("limit: ", r + self.r)
                if distance <= r + self.r:
                    dx = ball.info()[3]
                    dy = ball.info()[4]
                    dx_1 = (dx * r * 2 + self.dx * (self.r - r)) / (r + self.r)
                    dy_1 = (dy * r * 2 + self.dy * (self.r - r)) / (r + self.r)
                    dx_2 = (self.r * 2 * self.dx + (r - self.r) * dx) / (r + self.r)
                    dy_2 = (self.r * 2 * self.dy + (r - self.r) * dy) / (r + self.r)
                    ball.collision(dx_2, dy_2)
                    self.dx = dx_1
                    self.dy = dy_1

    def collision(self, new_dx, new_dy):
        self.dx = new_dx
        self.dy = new_dy

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
        if distance <= target[2] + 5:
            print('Get {} points!'.format(50 - target[2]))
            score += ball.is_shoot()
            print(score)
            balls.remove(ball)
            if not balls or score >= 1000:
                print('Победа!')
                exit()
            break
    else:
        print('miss :(')


def make_new_balls():
    if len(balls) < 5:
        new = Ball(balls)
        balls.append(new)
    root.after(1000, make_new_balls)


def tick():
    for ball in balls:
        ball.check_collision()
        ball.move()
        ball.draw()
    root.after(10, tick)


def main():
    global root, canvas, balls, score, balls_info
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
    canvas.pack(anchor=NW, fill=BOTH)
    border = canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="white", width=5)
    canvas.bind('<Button-1>', canvas_click)
    score = 0
    balls = []
    make_new_balls()
    tick()
    mainloop()


print('Программа закончена.')


if __name__== "__main__":
    main()