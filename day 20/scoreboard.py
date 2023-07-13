from turtle import Turtle
ALIGNMENT = "center"
FONT = ('arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file_highscore:
            self.high_score = int(file_highscore.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        with open("data.txt", mode="r") as file_highscore:
            self.high_score = int(file_highscore.read())
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file_highscore:
                file_highscore.write(str(self.score))
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



