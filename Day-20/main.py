from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

screen.exitonclick()


## Snakes behviour have apperance with refactor

# Snake class, food class, score board.