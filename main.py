import turtle

screen = turtle.Screen()

screen.screensize(1000,1000)
screen.bgcolor("yellow")

t= turtle.Turtle()

t.fillcolor("cyan")
t.begin_fill()
t.setheading(135)
t.forward(100)
t.setheading(225)
t.forward(100)
t.setheading(315)
t.forward(100)
t.setheading(45)
t.forward(100)
t.end_fill()

t.begin_fill()
t.fillcolor("brown")
t.setheading(45)
t.forward(100)
t.setheading(315)
t.forward(100)
t.setheading(225)
t.forward(100)
t.setheading(135)
t.forward(100)
t.end_fill()

t.hideturtle()

turtle.done()