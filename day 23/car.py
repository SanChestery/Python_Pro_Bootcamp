from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "purple", "yellow", "orange"]
STARTING_PACE = 5
INCREMENT_PACE = 2


class Car:
    def __init__(self):
        self.cars = []
        self.pace = STARTING_PACE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_y = random.randint(-240, 240)
            new_car.goto(300, new_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.pace)

    def increase_pace(self):
        self.pace += INCREMENT_PACE
