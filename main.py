import turtle
import car
import time
turtle1 = turtle.Turtle()
n_car = car.Car()
score = car.Score()
n_car.new_car()
screen = turtle.Screen()
screen.tracer(0)
screen.setup(700,500)
def make_turtle():
    turtle1.shape("turtle")
    turtle1.pencolor("red")
    turtle1.pensize(31)
    turtle1.color("green")
    turtle1.shapesize(1.5,1.5)
    turtle1.penup()
    turtle1.setheading(270)
    turtle1.goto(0,-230)
    turtle1.setheading(90)
make_turtle()
screen.listen()
def go_up():
    turtle1.fd(20)
def go_down():
    turtle1.backward(20)
screen.onkey(go_down,"Down")
screen.onkey(go_up,"Up")
gamm_is_on = True
while gamm_is_on:
    time.sleep(0.1)
    screen.update()
    n_car.new_car()
    n_car.move()
    for cars in n_car.list:
        if turtle1.distance(cars) < 20:
            gamm_is_on = False
            score.game_over()

    if turtle1.ycor() > 220:
        n_car.level_up()
        turtle1.goto(0,-230)
        score.score_up()

screen.exitonclick()

