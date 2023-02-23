from turtle import Turtle,Screen
import heroes
#from turtle import *#* means =>import everything in that  module
# import turtle as t
# timmy=t.Turtle()
timmy=Turtle()
timmy.shape("circle")
timmy.pensize(10)
timmy.circle(80)
timmy.pen(fillcolor="violet", pencolor="blue", pensize=2)

timmy.shape('turtle')
timmy.forward(10)
timmy.penup()
for i in range(0,4):
    for i in range(0,10):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
    timmy.left(90)

    














screen= Screen()
screen.exitonclick()