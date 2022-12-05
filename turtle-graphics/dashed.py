from turtle import Turtle, Screen

su = Turtle()
su.shape("turtle")

for _ in range(50):
    su.pendown()
    su.forward(5)
    su.penup()
    su.forward(5)


screen = Screen()
screen.exitonclick()
