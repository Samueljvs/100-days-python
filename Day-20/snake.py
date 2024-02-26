## Snake class
## this will be an imported module into the main.py file that will handle the create of the snake and the 
## snakes movements

from turtle import Turtle, Screen

STRTING_POS = [(0,0), (-20, 0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
 

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STRTING_POS:  
            new_sgement = Turtle(shape="square")
            new_sgement.color("white")
            new_sgement.penup()
            new_sgement.goto(pos)
            self.segments.append(new_sgement) 
    
    def move(self):

        for seg_num in range(len(self.segments) - 1, 0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
         if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)