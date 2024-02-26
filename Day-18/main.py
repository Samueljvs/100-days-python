## Get colorgram'
# import colorgram

# colors = colorgram.extract('hirst-painting.jpg', 20)

# list_colrs = []
# for i in range(len(colors)):
#     list_colrs.append(tuple(list(colors[i].rgb)))

from turtle import Turtle, Screen
import random as rnd

screen = Screen()
tim = Turtle()

screen.colormode(255)


# colorgram extrated list
color_list = [(201, 157, 110), (63, 104, 124), (128, 160, 172), (153, 86, 52), 
              (124, 82, 97), (132, 173, 160), (223, 198, 132), (188, 141, 45), 
              (189, 134, 147), (47, 31, 19), (182, 93, 111), (64, 124, 112), 
              (19, 46, 57), (62, 158, 129), (204, 95, 79), (147, 25, 38)]

# 10 X 10 rows or spots
# size 20 - 50 spacing

tim.speed(0)
tim.penup()
tim.hideturtle()

x_start = -300
y_start = -250

tim.setpos(x_start, y_start)

def across_ten():
    for _ in range(10):
        tim.pencolor(rnd.choice(color_list))
        tim.dot(20)
        tim.fd(50)

for _ in range(10):
    across_ten()
    y_start += 50
    tim.setpos(x_start, y_start)


    




screen.exitonclick()
