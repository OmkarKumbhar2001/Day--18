from turtle import Turtle,Screen
import heroes
print(heroes.gen())
#from turtle import *#* means =>import everything in that  module
# import turtle as t
# timmy=t.Turtle()
timmy=Turtle()
timmy.shape("circle")
timmy.pensize(10)
# timmy.circle(80)
timmy.color('red')
timmy.shape('turtle')
for i in range(0,4):
    timmy.forward(200)
    timmy.dot("green")
    timmy.left(90)

    














screen= Screen()
screen.exitonclick()