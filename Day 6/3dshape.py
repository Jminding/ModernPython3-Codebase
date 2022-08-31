import turtle
import math

def draw_square(tur):
    for i in range(4):
        tur.forward(100)
        tur.left(90)

t = turtle.Turtle()

draw_square(t)
t.penup()
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.pendown()
draw_square(t)
t.right(135)
t.forward(50 * math.sqrt(2))
t.right(180 - 45)
t.forward(100)
t.right(45)
t.forward(50 * math.sqrt(2))
t.right(45)
t.forward(100)
t.right(180 - 45)
t.forward(50 * math.sqrt(2))
t.left(45)
t.forward(100)
t.left(180 - 45)
t.forward(50 * math.sqrt(2))
t.penup()
t.home()

turtle.done()