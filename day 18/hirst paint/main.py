from turtle import Turtle,Screen,colormode
import random
timmy = Turtle()
colormode(255)
timmy.shape("turtle")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
number_of_dots=101
timmy.speed("fastest")
# import colorgram
# colors = colorgram.extract('abc.jpg',25)
# colors_rgb=[]
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     new_color=(r, g, b)
#     colors_rgb.append(new_color)
# print(colors_rgb)

timmy.pensize(0)
img_color=[(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

for dot_count in range(1,number_of_dots):
    timmy.dot(20, random.choice(img_color))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)





screen= Screen()
screen.exitonclick()