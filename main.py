from turtle import Screen
from paddle import Paddle
from ball import Ball
import random
import time

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

ball.change_direction(random.randint(5,20))
while game_running:
    screen.update()
    screen.listen()
    time.sleep(0.01)
    ball.move()

    screen.onkeypress(fun=paddle_two.up, key='Up')
    screen.onkeypress(fun=paddle_two.down, key='Down')
    screen.onkeypress(fun=paddle_one.up, key='w')
    screen.onkeypress(fun=paddle_one.down, key='s')

    if ball.ycor() > 500 or ball.ycor() < -500:
        ball.hit_wall(ball.heading())

    if paddle_one.distance(ball) < 20 or paddle_two.distance(ball) < 20:
        ball.change_direction(ball.heading())







screen.exitonclick()

