# Day 18 

from turtle import Turtle, Screen
import random as rnd

screen = Screen()
tim = Turtle()

screen.colormode(255)
tim.speed(0)

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# tim.reset()

# for i in range(15):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# tim.reset()

# ## draw shapes 360/3 to get degress turned ##
# #

# DIVIDER = 360
# counter = 3

# def rand_colour():
#     return  (rnd.randint(0,255), rnd.randint(0,255), rnd.randint(0,255))

# while counter < 11:
#     screen.colormode(255)
#     tup = rand_colour()
#     tim.pencolor(tup)

#     for i in range(counter):
#         angle = 360/counter
#         tim.forward(100)
#         tim.right(angle)

#     counter += 1

# tim.reset()

# ## Random walk ##
# screen.colormode(255)
# tim.pensize(5)
# # random colour
# def rand_colour():
#     return  (rnd.randint(0,255), rnd.randint(0,255), rnd.randint(0,255))

# def random_walk():
#     tim.pencolor(rand_colour())  
#     choice = rnd.choice([0,90,180,-90])
#     tim.rt(choice)
#     tim.forward(30)

# for i in range(50):
#     random_walk() 

# tim.reset()

def rand_colour():
    return  (rnd.randint(0,255), rnd.randint(0,255), rnd.randint(0,255))


for i in range(60):
    tim.pencolor(rand_colour())
    tim.circle(100)
    tim.rt(6)


screen.exitonclick()