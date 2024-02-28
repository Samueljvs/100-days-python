from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):

        self.cars = []

    def make_car(self):        
        for i in range(0,random.randint(0,1), 1):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(COLORS[random.randint(0, 5)])
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)


    def move_car(self):
        for car in range(0, len(self.cars), 1):
            newx = self.cars[car].xcor() - STARTING_MOVE_DISTANCE  
            self.cars[car].setx(newx)
        