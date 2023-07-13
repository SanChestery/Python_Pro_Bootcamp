from turtle import Turtle
ALIGNMENT = "center"
FONT = ('arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()

    def increase(self):
        self.score += 1
        self.update()

''' 
    This method got removed and replaced by the reset method to add a high score   
    def gameover(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
'''



