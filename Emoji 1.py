import turtle
turtle. bgcolor('pink')
turtle.speed(10)
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()

turtle. color("yellow")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()
turtle.color("black")
turtle.goto(0,-201)
turtle.pensize(5)
turtle.circle(201)

turtle.penup()
turtle.goto(-60,30)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.left(60)
turtle.forward(70)
turtle.circle(40,200)
turtle.left(70)
turtle.circle(-40,-200)
turtle.forward(-60)
turtle.end_fill()

turtle.penup()
turtle.goto(60,30)
turtle.pendown()
turtle.begin_fill()
turtle.right(50)
turtle.forward(70)
turtle.circle(-40,200)
turtle.right(250)
turtle.circle(-40,200)
turtle.forward(65)
turtle.end_fill()

turtle.penup()
turtle.goto(140,-40)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.left(-115)
turtle.circle(150,-150)
turtle.left(50)
turtle.circle(340,50)
turtle.end_fill()

turtle.hideturtle()
turtle.done()





