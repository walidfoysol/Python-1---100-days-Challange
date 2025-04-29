import turtle as t
import random
screen = t.Screen()
tom = t.Turtle()
t.colormode(255)
tom.pensize(2)
tom.speed(5)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

def shape(n):
    angle = 360/n
    for j in range(n):
        tom.right(angle)
        tom.forward(50)


for i in range(3,20):
    tom.color(random_color())
    tom.pendown()
    tom.pencolor(random_color())
    shape(i)



screen.exitonclick()