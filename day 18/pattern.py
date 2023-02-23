from turtle import Turtle,Screen
import random
timmy=Turtle()
timmy.pen(fillcolor="violet", pencolor="blue", pensize=2)
timmy.shape('turtle')
count=3

colors=['red','blue','green','yellow','violet','orange','pink','black']
def dra_shape(count,current_angle):
    timmy.pencolor(random.choice(colors))
    for j in range(0,count):
        timmy.forward(100)
        timmy.right(current_angle)


for i in range(0,10):
    current_angle=360/count
    dra_shape(count,current_angle)
    count+=1


screen= Screen()
screen.exitonclick()