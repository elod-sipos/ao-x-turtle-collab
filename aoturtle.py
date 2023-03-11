import turtle

ao = turtle.Turtle()
ao.speed(0)

def orange():
    ao.color("Orange")
    ao.begin_fill()
    ao.circle(100)
    ao.end_fill()

def eyes():
    ao.penup()
    ao.goto(-40, 100)
    ao.pendown()
    ao.color("White")
    ao.begin_fill()
    ao.circle(20)
    ao.end_fill()

    ao.penup() 
    ao.goto(40,100)
    ao.pendown()
    ao.begin_fill()
    ao.circle(20)
    ao.end_fill()

    ao.penup()
    ao.goto(-40,105)
    ao.pendown()
    ao.color("Black")
    ao.begin_fill()
    ao.circle(10)
    ao.end_fill()

    ao.penup()
    ao.goto(40,105)
    ao.pendown()
    ao.begin_fill()
    ao.circle(10)
    ao.end_fill()

def mouth():
    ao.penup()
    ao.goto(-60,80)
    ao.pendown()
    ao.color("red")
    ao.begin_fill()
    ao.right(90)
    ao.circle(60,180)
    ao.end_fill()


orange()
eyes()
mouth()
