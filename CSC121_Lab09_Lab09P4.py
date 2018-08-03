import turtle
turtle.setup(800, 600)
left = -300
right = 300
top = 200
bottom = -200

turtle1 = turtle.Turtle()
turtle1.hideturtle()
turtle1.penup()
turtle1.setposition(left, top)
turtle1.pendown()
turtle1.setposition(left, bottom)

turtle2 = turtle.Turtle()
turtle2.hideturtle()
turtle2.penup()
turtle2.setposition(right, top)
turtle2.pendown()
turtle2.setposition(right, bottom)

turtle3 = turtle.Turtle()
turtle3.shape("turtle")
turtle3.penup()

for i in range(2000):
    turtle3.forward(1)
    if turtle3.xcor()>=right:
        turtle3.left(180)
    if turtle3.xcor()<=left:
        turtle3.right(180)

turtle.exitonclick()
