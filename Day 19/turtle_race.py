from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(600, 400)

colors = ["red", "blue", "green", "yellow", "cyan", "purple"]

y = 100
all_turtles = []

for turtle_index in range(0,5):
    new_turtle= Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-280, y)
    y = y - 40
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
winner = ""

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,20)
        turtle.forward(rand_distance)
        if turtle.xcor() > 240:
            is_race_on = False
            winner = turtle.fillcolor()

print(winner)
if winner == user_bet:
    screen.textinput("Congratulations!", "Congratulations, you won!")
screen.exitonclick()