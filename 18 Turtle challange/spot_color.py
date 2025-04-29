import turtle as t
import random
tom = t.Turtle()
screen = t.Screen()
t.colormode(255)
tom.penup()
tom.speed(10)
tom.right(135)
tom.forward(350)
tom.left(135)


colors = [(28, 107, 145), (233, 151, 72), (13, 169, 208), (5, 58, 98), (29, 136, 75), (147, 77, 28), (215, 131, 162), (
141, 32, 49), (215, 94, 124), (207, 156, 19), (5, 103, 66), (217, 209, 10), (2, 70, 139), (239, 213, 82), (
15, 50, 45), (151, 189, 173), (120, 173, 192), (77, 85, 24), (53, 62, 17), (242, 168, 150), (233, 102, 33), (
120, 54, 83), (2, 92, 122), (165, 31, 26), (213, 174, 196), (71, 158, 109)]

for i in range(10):
    for j in range(10):
        tom.pendown()
        tom.dot(20, random.choice(colors))
        tom.penup()
        tom.forward(50)
    tom.left(90)
    tom.forward(50)
    tom.left(90)
    tom.forward(500)
    tom.left(180)




screen.exitonclick()