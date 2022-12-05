from turtle import Turtle, Screen, colormode
from random import choice, randint

colormode(255)

su = Turtle()
screen = Screen()
su.shape("turtle")
su.speed(0)


def move_forwards():
    su.forward(10)


def move_backwards():
    su.backward(10)


def turn_left():
    su.left(10)


def turn_right():
    su.right(10)


def clear_drawing():
    su.clear()
    su.penup()
    su.home()
    su.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
