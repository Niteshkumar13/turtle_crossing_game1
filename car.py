import turtle
import random
screen = turtle.Screen()
screen.setup(700,500)

turtle.colormode(255)
class Car():
    def __init__(self):

        self.y = 10
        self.list = []
        self.mov = 5
    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)



    def move(self):
        for i in self.list:
            i.backward(self.mov)

    def new_car(self):
        s = random.randint(1,6)
        if s == 1:
            x = turtle.Turtle()
            x.shape("square")
            x.penup()
            x.shapesize(1.2,3)
            x.color(self.random_color())
            y = random.randint(-280,190)
            x.goto(300,y)

            self.list.append(x)


    def level_up(self):
        self.mov += 10
        self.move()


class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-290,210)
        self.write(f"level  {self.score}", align="left", font=("Arial Rounded MT Bold", 24, "normal"))
    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"level  {self.score}",align="left",font=("Arial Rounded MT Bold",24,"normal"))

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(-100,0)
        self.write("Game Over", align="left", font=("Arial Rounded MT Bold", 24, "normal"))











