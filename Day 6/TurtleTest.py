import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.shape('turtle')
turtle.Screen().bgcolor('black')
t.pensize(14)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
while True:
    t.color(random.choice(colors))
    t.forward(random.randint(1, 90))
    t.right(random.randint(10, 360))
turtle.done()

