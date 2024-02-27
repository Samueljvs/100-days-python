from turtle import Turtle

ALIGNMENT = "center"
FONT = font = ('Courier', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        self.counter = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(-10,270)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Score: {self.counter}", align=ALIGNMENT, font = FONT)

    def refrech_count(self):
        self.counter += 1
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font = FONT)