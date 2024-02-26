## Snake class
## this will be an imported module into the main.py file that will handle the create of the snake and the 
## snakes movements

from turtle import Turtle

STRTING_POS = [(0,0), (-20, 0), (-40,0)]
MOVE_DIST = 20

class Snake:

    

    def __init__(self):

        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in STRTING_POS:  
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(pos)
            self.segments.append(snake) 
    
    def move(self):

        for seg_num in range(len(self.segments) - 1, 0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(MOVE_DIST)
