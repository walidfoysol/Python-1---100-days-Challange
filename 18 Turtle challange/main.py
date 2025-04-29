import turtle as t
import random

tom = t.Turtle()
t.colormode(255)
tom.pensize(2)
tom.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


for i in range(72):
    tom.right(5)
    tom.color(random_color())
    tom.pendown()
    tom.pencolor(random_color())
    tom.circle(120, 360)


screen = t.Screen()
screen.exitonclick()