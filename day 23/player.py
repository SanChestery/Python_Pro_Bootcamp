from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.goto(0, -280)

    def move(self):
        new_y = self.ycor() + 5
        self.goto(0, new_y)

    def scored(self):
        self.goto(0, -280)
