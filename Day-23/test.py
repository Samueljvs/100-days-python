import random
import time
from turtle import Screen
from car_manager import CarManager


screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)
screen.title("Turtle Crossing Road!")

car = CarManager()

screen.update()

screen.exitonclick()

