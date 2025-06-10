import colorgram
import turtle
from turtle import Turtle, Screen
import random

#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

#print(rgb_colors)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
       (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
       (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
       (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

start_x = -250
start_y = -250
tim.setpos(start_x, start_y)

for row in range(10):
    for col in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.setx(start_x)
    tim.sety(start_y + (row + 1) * 50)

screen = Screen()
screen.exitonclick()
