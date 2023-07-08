import turtle
from turtle import Screen, Turtle
import random

turtle.colormode(255)
dot = Turtle()
dot.speed("fastest")
dot.penup()
dot.hideturtle()
dot.setposition(-300, -300)


color_list = [(242, 225, 0), (226, 0, 81), (209, 163, 1), (229, 2, 0), (0, 195, 228), (8, 198, 119), (234, 220, 103), (217, 71, 6), (221, 160, 113), (11, 29, 185), (10, 23, 64), (119, 178, 216), (13, 109, 184), (240, 7, 178), (236, 163, 201), (224, 129, 179), (241, 54, 139), (65, 19, 5), (119, 222, 237), (2, 51, 25), (11, 147, 57), (124, 193, 170), (140, 219, 204), (112, 84, 222), (64, 7, 36), (5, 104, 42)]


for _ in range(1, 101):
    dot.dot(20, random.choice(color_list))
    dot.forward(50)

    if _ % 10 == 0:
        dot.setheading(90)
        dot.forward(50)
        dot.setheading(180)
        dot.forward(500)
        dot.setheading(0)



screen = Screen()
screen.exitonclick()