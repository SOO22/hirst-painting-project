import colorgram
import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

jesus = Turtle()
jesus.speed("fastest")
jesus.penup()
jesus.hideturtle()
jesus.goto(-230, -200)


y = -150
for row in range(10):
    for column in range(10):
        jesus.dot(20, random.choice(rgb_colors))
        jesus.forward(50)

    jesus.setposition(-230, y)
    y += 50


screen = Screen()
screen.exitonclick()
