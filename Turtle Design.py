# Design using Turtle:
import turtle

t = turtle.Turtle()
colors = ['red', 'orange']

#Turtle drawing code:
for number in range(400):
    t.forward(number + 1)
    t.right(89)
    t.pencolor(colors[number % 2])

turtle.done()
