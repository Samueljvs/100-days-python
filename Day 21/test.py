from turtle import Turtle, Screen
turtle = Turtle()

counter = 0
screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

turtle.color("white")
turtle.penup()
turtle.speed("fastest")
turtle.goto(-10,270)
turtle.hideturtle()
turtle.write("Score: " + counter, align="center", font = ('Arial', 12, 'normal'))

screen.exitonclick()