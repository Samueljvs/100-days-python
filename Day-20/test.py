from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create a snake body
#
screen.listen()

def up():
    segments[0].setheading(90)

def down():
    segments[0].setheading(270)

def left():
    segments[0].setheading(180)

def right():
    segments[0].setheading(0)

screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)


starting_pos = [(0,0), (-20, 0), (-40,0)]
segments = []


for pos in starting_pos:  
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(pos)
    segments.append(snake) 

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    for seg_num in range(len(segments) - 1, 0,-1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)