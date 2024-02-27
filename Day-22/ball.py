from turtle import Turtle
import random

## ball will start moving on screen, and it will start moving in a random angle left of right each time
## ball will be white, 20h, 20w, centre start

MOVE_DIST = 20
YCOR = 10
XCOR = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setpos(0,0)
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove *= -1

    def hit(self):
        self.xmove *=-1
        self.move_speed *=0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce()


