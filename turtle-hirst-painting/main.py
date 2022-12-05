from turtle import Turtle, Screen, colormode
from random import choice

colormode(255)
su = Turtle()
# su.hideturtle()
su.speed("fastest")
su.penup()
su.shape("turtle")

color_list = [(253, 253, 250), (246, 253, 249), (181, 102, 22), (45, 104, 145), (244, 247, 251), (128, 200, 187),
              (211, 161, 12), (14, 35, 60), (254, 248, 252), (242, 83, 37), (210, 146, 117), (153, 185, 212),
              (238, 75, 91), (181, 46, 135), (97, 180, 47), (21, 91, 67), (253, 218, 0), (244, 217, 40), (62, 98, 85),
              (207, 136, 153), (157, 208, 192), (28, 45, 41), (166, 189, 220), (231, 174, 163), (233, 168, 184),
              (22, 68, 110), (162, 204, 207), (101, 130, 160), (100, 135, 152)]

number_of_dots = 100


su.setheading(225)
su.forward(300)
su.setheading(0)


def dot_walk_to_begin():
    su.setheading(90)
    su.forward(50)
    su.setheading(180)
    su.forward(500)
    su.setheading(0)


def dot_print_forward():
    su.dot(20, choice(color_list))
    su.forward(50)


for dot_count in range(1, number_of_dots + 1):
    dot_print_forward()

    if dot_count % 10 == 0:
        dot_walk_to_begin()

screen = Screen()
screen.exitonclick()
