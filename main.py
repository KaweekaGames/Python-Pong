from turtle import Screen
from paddle import Paddle
from ball import Ball
import random

screen = Screen()
screen.setup(width=1400, height=1000)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)

game_running = True

paddle_one = Paddle()
paddle_two = Paddle()
paddle_one.goto(-680, 0)
paddle_two.goto(680,0)
ball = Ball()
obstacles = []
obstacles.append(paddle_one)
obstacles.append(paddle_two)

ball.change_direction(random.randint(0,15))
while game_running:
    screen.update()
    screen.listen()

    ball.move()

    screen.onkeypress(fun=paddle_two.up, key='Up')
    screen.onkeypress(fun=paddle_two.down, key='Down')
    screen.onkeypress(fun=paddle_one.up, key='w')
    screen.onkeypress(fun=paddle_one.down, key='s')

    for obstacle in obstacles:
        if ball.distance(obstacle) < 20:
            heading = ball.heading()
            ball.change_direction(heading)
            print("bounce")







screen.exitonclick()

