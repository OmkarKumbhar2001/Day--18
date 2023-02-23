from turtle import Turtle,Screen,colormode
import random

timmy=Turtle()
timmy.shape("circle")
colormode(255)




timmy.pen(fillcolor="violet", pencolor="blue", pensize=12)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy.speed(10)
timmy.shape('turtle')
directions = [0, 90, 180, 270]


def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    abc = (r, g, b)
    return abc

def change_dir():
    timmy.setheading(random.choice(directions))


for i  in range (0,200):
    timmy.color(random_color())
    timmy.forward(30)
    change_dir()


screen= Screen()
screen.exitonclick()