import turtle

turtle.bgcolor('medium violet red')
turtle.pencolor('white')
turtle.width(23)
turtle.penup()
turtle.goto(160, -100)
turtle.pendown()
turtle.left(90)
turtle.end_fill()
for i in range(4):
    turtle.forward(250)
    turtle.circle(34, 90)
turtle.penup()
turtle.goto(85, 30)
turtle.pendown()
turtle.circle(80, 360)
turtle.penup()
turtle.goto(110, 130)
turtle.pendown()
turtle.circle(7, 360)


