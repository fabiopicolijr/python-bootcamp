from turtle import Turtle, Screen, colormode
from random import choice, randint

directions = [0, 90, 180, 270]

colormode(255)
su = Turtle()
su.shape("turtle")
su.pensize(15)
su.speed(0)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    r_color = (r, g, b)
    return r_color


def walk(direction):
    su.setheading(direction)
    su.forward(30)


for shape_side_n in range(200):
    su.color(random_color())
    walk(choice(directions))

screen = Screen()
screen.exitonclick()
