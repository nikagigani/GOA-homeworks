from turtle import*
width(5)
speed(10)
forward (200)
left(90)
forward (200)
left(90)
forward (200)
left(90)
forward (200)
left(90)
#end of square

#door
forward(70)
color("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto (200, 200)
pendown()
#roof
color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20, 180)
pendown()

#windows
color("red")
begin_fill()
left(30)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()

penup()
goto(140,180)
pendown()

begin_fill()
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()


















exitonclick()