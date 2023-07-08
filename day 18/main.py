from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape()
tim.color("red")

'''for _ in range(4):
    tim.forward(100)
    tim.right(90)
'''
'''for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()'''

'''
for it in range(3, 11):
    angle = 360 / it
    for time in range(it):
        tim.forward(100)
        tim.right(angle)
'''


def rand_color():
    R = random.randint(0, 255) / 255
    G = random.randint(0, 255) / 255
    B = random.randint(0, 255) / 255
    t_rgb = (R, G, B)
    return t_rgb

'''
tim.speed(5)
tim.pensize(5)

directions = [0, 90, 180, 270]


not_finished = True
while not_finished:
    tim.color(rand_color())
    tim.setheading(random.choice(directions))
    tim.forward(random.randint(10, 100))

'''


tim.speed("fastest")


def draw_spirograph(gapsize):
    for _ in range(int(360 / gapsize)):
        tim.color(rand_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gapsize)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()

