import turtle
import tkinter as tk

# Create a Tkinter root window
root = tk.Tk()

# Set the background color of the root window
root.configure(bg='blue')

# Initialize Turtle
screen = turtle.Screen()
t = turtle.Turtle()
colors = ['red', 'orange']

# Your Turtle drawing code
for number in range(400):
    t.forward(number + 1)
    t.right(89)
    t.pencolor(colors[number % 2])

turtle.done()
