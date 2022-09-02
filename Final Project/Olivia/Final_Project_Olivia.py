from asyncio.windows_events import NULL
from contextlib import nullcontext
from turtle import *
import turtle
turtle.Screen().bgcolor("light blue")
turtle.pensize(7)
turtle.shape("turtle") 
turtle.color("green")

c = 'green'
def changeColor():
    global c
    c = turtle.textinput("Choose a color","Colors: red, orange, yellow, green, cyan, blue, purple, pink, brown, black")
    turtle.color(c)
    turtle.listen()

def u():
    turtle.forward(20)

def d():
    turtle.forward(-20)


def r():
    turtle.right(20)

def l():
    turtle.left(20)

pen_down = True
def toggle():
    global pen_down
    if pen_down:
        turtle.penup()
        pen_down = False
        turtle.color('light green')
    else:
        turtle.pendown()
        pen_down = True
        turtle.color(c)

s = turtle.Screen()
s.setup(900,600)

#change_color

s.onkeypress(u, "Up")
s.onkeypress(d, "Down")
s.onkeypress(r, "Right")
s.onkeypress(l, "Left")
s.onkey(toggle, "space")
s.onkey(changeColor, "c")
s.listen()


turtle.done()