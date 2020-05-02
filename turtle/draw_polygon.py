import tkinter
import turtle
from turtle import * 


# turtle.tracer(False) # display the result,don't tracer the progess
t = turtle.Turtle()
def draw(sides,side_length):
  for i in range(sides) :
    t.fd(side_length)
    t.lt(360/sides)

turtle.bgcolor('orange')
draw(6,50)
# save the screen as eps file
turtle.getcanvas().postscript(file = 'polygon.eps',colormode = 'color')

# keep windows on
turtle.done()
