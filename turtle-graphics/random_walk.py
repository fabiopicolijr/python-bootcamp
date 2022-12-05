from turtle import Turtle, Screen
from random import choice

su = Turtle()
su.shape("turtle")
su.pensize(15)
su.speed(0)

colours = ["aquamarine", "chartreuse1", "DarkGoldenrod", "azure3", "coral", "DeepPink1", "DarkTurquoise",
           "DarkOliveGreen1"]
directions = [0, 90, 180, 270]


def walk(direction):
    su.setheading(direction)
    su.forward(30)


for shape_side_n in range(200):
    su.color(choice(colours))
    walk(choice(directions))

screen = Screen()
screen.exitonclick()
