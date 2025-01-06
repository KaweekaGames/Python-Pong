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
            new_heading = 180- heading
        else:
            new_heading = 540- heading
        self.setheading(new_heading)

    def hit_wall(self, heading):
        new_heading = 360- heading
        self.setheading(new_heading)

    def move(self):
        self.forward(5)

