from turtle import Turtle

MOVE_DIST = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.setpos(position)
        self.speed("fastest")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.left(90)
        
    def moveup(self):
        self.forward(MOVE_DIST)

    def movedown(self):
        self.backward(MOVE_DIST)