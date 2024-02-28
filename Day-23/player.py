from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION) 
        self.left(90)
        self.move_speed = 0.2

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)
        self.move_speed *= 0.5