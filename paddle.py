from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(UP)

    #Move Paddle UP
    def up(self):
        self.setheading(UP)
        self.forward(20)

    #Move Paddle DOWN
    def down(self):
        self.setheading(DOWN)
        self.forward(20)

