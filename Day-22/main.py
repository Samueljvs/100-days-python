from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_one = Paddle((350, 0))
paddle_two = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_on = True

screen.listen()
screen.onkey(paddle_one.moveup, "Up")
screen.onkey(paddle_one.movedown, "Down")
screen.onkey(paddle_two.moveup, "w")
screen.onkey(paddle_two.movedown, "s")

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Dectect wall collison
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect paddle collion
    if ball.xcor() > 320 and ball.distance(paddle_one) < 50 or ball.xcor() < -320 and ball.distance(paddle_two) < 50:
        ball.hit()

    # right side miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # left side miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()