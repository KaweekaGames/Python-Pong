from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.penup()
        self.direction = 1
        self.goto(0,0)


    def change_direction(self, heading):
        if heading in range(0,180):
            new_heading = heading + 180
        else:
            new_heading = heading -180
        self.setheading(new_heading)

    def move(self):
        self.forward(.1)

