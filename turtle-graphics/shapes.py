from turtle import Turtle, Screen
from random import choice

su = Turtle()
su.shape("turtle")

colours = ["aquamarine", "chartreuse1", "DarkGoldenrod", "comsilk3", "coral", "DeepPink1", "DarkTurquoise", "DarkOliveGreen1"]


def draw_shape(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        su.forward(100)
        su.right(angle)


for shape_side_n in range(3, 11):
    su.color(choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
