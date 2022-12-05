from turtle import Turtle, Screen, colormode
from random import choice, randint

directions = [0, 90, 180, 270]

colormode(255)
su = Turtle()
su.shape("turtle")
su.speed(0)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    r_color = (r, g, b)
    return r_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        su.color(random_color())
        su.circle(100)
        su.setheading(su.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
