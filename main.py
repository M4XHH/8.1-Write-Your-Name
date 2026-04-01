from turtle import *

screen = Screen()
screen.bgcolor("teal")
screen.setup(width= 1000, height= 600)

turt = Turtle()
turt.shape("turtle")
turt.color("red")
turt.speed(4)
turt.penup()
turt.goto(-450,-220)
turt.pendown()
turt.pensize(7)
turt.goto(-450,220)
turt.goto(-380,-180)
turt.goto(-310,220)
turt.goto(-310,-220)
turt.penup()
turt.goto(-260,-220)
turt.pendown()
turt.color("orange")
turt.setheading(85)
turt.forward(440)
turt.setheading(-85)
turt.forward(220)
turt.setheading(180)
turt.forward(40)
turt.backward(40)
turt.setheading(-85)
turt.forward(220)
turt.penup()
turt.goto(-130,-220)
turt.color("yellow")
turt











screen.exitonclick()