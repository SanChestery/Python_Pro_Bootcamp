from turtle import Turtle

ALIGNMENT = "center"
FONT = ('arial', 40, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.update()

    def update(self):
        self.write(arg=f"{self.score_l}   |   {self.score_r}", align=ALIGNMENT, font=FONT)

    def left_scored(self):
        self.score_l += 1
        self.clear()
        self.update()

    def right_scored(self):
        self.score_r += 1
        self.clear()
        self.update()

