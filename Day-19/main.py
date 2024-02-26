from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width = 500, height = 400)
user_bets = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the rae \n Please Enter a color :")

all_turtles = []

colors = ["red","orange", "yellow","green","blue","purple"]
ypos = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -230, y = ypos[turtle_index])
    all_turtles.append(new_turtle)

if user_bets:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bets:
                print(f"You won!the winning color was {winning_color}")
            else:
                print(f"You lost, the winning color was {winning_color}")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        
    

    




screen.exitonclick()