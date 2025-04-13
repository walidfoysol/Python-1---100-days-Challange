# from turtle import Turtle, Screen
#
# tom = Turtle()
# print(table)
# print(tom.color())
# tom.shape('turtle')
# tom.color('coral')
# tom.pensize(10)
# tom.pencolor('black')
# tom.forward(100)
# tom.right(90)
# tom.forward(100)
# tom.right(90)
# tom.forward(100)
# tom.right(90)
# tom.forward(300)
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows([["Pikachu", "Electric"],
              ["Squirtle", "Water"],
              ["Charmandar","Fire"]])
table.align = "l"
print(table)