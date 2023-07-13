from turtle import Turtle
ALIGNMENT = "center"
FONT = ('arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update()

    def update(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

