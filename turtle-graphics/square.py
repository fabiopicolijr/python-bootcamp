from turtle import Turtle, Screen

su = Turtle()
su.shape("turtle")

for _ in range(4):
    su.forward(100)
    su.right(90)

screen = Screen()
screen.exitonclick()
