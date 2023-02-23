from turtle import Turtle,Screen,colormode
import random

timmy=Turtle()
timmy.shape("circle")
colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    abc = (r, g, b)
    return abc

timmy.speed("fastest")
timmy.pen(fillcolor="violet", pencolor="blue", pensize=3)
for i in range(0,36):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(20)
    timmy.right(10)


screen= Screen()
screen.exitonclick()