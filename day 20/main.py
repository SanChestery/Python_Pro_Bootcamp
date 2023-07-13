from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_is_one = True
while game_is_one:
    sc.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()

    # Detect collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


sc.exitonclick()