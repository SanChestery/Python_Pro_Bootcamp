from turtle import Screen
from car import Car
from score import Score
from player import Player
import time

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("white")
sc.title("My turtle crossing")
sc.tracer(0)


score = Score()
player = Player()
car = Car()

sc.listen()
sc.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    sc.update()

    car.create_car()
    car.move_cars()

    # Detect Car hitting turtle
    for curr_car in car.cars:
        if curr_car.distance(player) < 20:
            game_is_on = False
            score.lost()

    # Detect if Turtle makes it across
    if player.ycor() > 255:
        player.scored()
        score.scored()
        car.increase_pace()

sc.exitonclick()
