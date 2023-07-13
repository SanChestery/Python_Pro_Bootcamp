from turtle import Turtle

ALIGNMENT = "left"
FONT = ('comic sans ms', 30, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_cross = 0
        self.hideturtle()
        self.penup()
        self.goto(-275, 265)
        self.color("black")
        self.update()

    def update(self):
        self.write(arg=f"Your Score: {self.score_cross}", align=ALIGNMENT, font=FONT)

    def scored(self):
        self.score_cross += 1
        self.clear()
        self.update()

    def lost(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=('comic sans ms', 50, 'normal'))