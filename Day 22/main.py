from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("My Pong Game")
sc.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
score = Scoreboard()


sc.listen()
sc.onkey(r_paddle.up, "Up")
sc.onkey(r_paddle.down, "Down")
sc.onkey(l_paddle.up, "w")
sc.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    sc.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with the Paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect if left has scored
    if ball.xcor() > 380:
        ball.out()
        score.left_scored()

    if ball.xcor() < -380:
        ball.out()
        score.right_scored()


sc.exitonclick()
