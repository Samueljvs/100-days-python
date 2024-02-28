import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Road!")

scoreboard = Scoreboard()
player = Player()
car = CarManager()

game_is_on = True

screen.listen()
screen.onkey(player.move_player, "Up")


while game_is_on:
    time.sleep(player.move_speed)
    screen.update()
    car.make_car()
    car.move_car()

# detect car collision and print game over
    for carn in car.cars[:]:
        if player.distance(carn) < 25:
            scoreboard.gameover()
            game_is_on = False

# detect getting to end of game and reset to bottom and go faster and update level
    if player.ycor() > 280:
        time.sleep(0.2)
        player.reset_turtle()
        scoreboard.update_level()

screen.exitonclick()
