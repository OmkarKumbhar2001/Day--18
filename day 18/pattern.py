from turtle import Turtle,Screen
timmy=Turtle()
timmy.pen(fillcolor="violet", pencolor="blue", pensize=2)
timmy.shape('turtle')
count=3
current_angle=360
colors=['red','blue','green','yellow','violet','orange','pink']
for i in range(0,6):
    current_angle=current_angle/count
    for j in range(0,count):
        timmy.pencolor(colors[i])
        timmy.forward(100)
        timmy.right(current_angle)
    count+=1
    current_angle=360

screen= Screen()
screen.exitonclick()