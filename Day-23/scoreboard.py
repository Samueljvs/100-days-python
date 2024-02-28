from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-220,250)
        self.level += 1
        self.write(F"Level {self.level}", align=ALIGNMENT, font=16)
        
    def gameover(self):
        self.hideturtle()
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font = FONT)
