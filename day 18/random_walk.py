from turtle import Turtle,Screen
import random

timmy=Turtle()
timmy.shape("circle")

timmy.pen(fillcolor="violet", pencolor="blue", pensize=12)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy.speed(10)
timmy.shape('turtle')
directions = [0, 90, 180, 270]
def change_dir():
    timmy.setheading(random.choice(directions))


for i  in range (0,200):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    change_dir()


screen= Screen()
screen.exitonclick()