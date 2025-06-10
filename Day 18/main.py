import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.pencolor("red")
tim.pensize(1)
tim.speed(0)
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

angle = 1
radius = 100

for _ in range(300):
    tim.pencolor(random_color())
    tim.circle(radius)
    tim.right(angle)
    radius += 1  # opcional: aumenta o raio para ampliar a espiral
#colors = ["green", "navy", "cornsilk", "magenta", "gold"]
#def draw_shape(num_sides):
#    angle = 360 / num_sides
#    for _ in range(num_sides):
#        tim.forward(100)
#        tim.right(angle)

#directions = [0, 90, 180, 270]  # cardinal directions

#for _ in range(100):
#    tim.pencolor(random_color())
#    tim.forward(30)
#    tim.setheading(random.choice(directions))
#
#for shape_side_n in range(3, 11):
#    tim.color(random_color())
#    draw_shape(shape_side_n)















screen = Screen()
screen.exitonclick()