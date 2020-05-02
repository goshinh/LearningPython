import turtle
from turtle import Turtle 

bob = turtle.Turtle()

bob.color('red','yellow')
bob.begin_fill()
while True:
    bob.forward(200)
    bob.left(170)
    if abs (bob.pos()) < 1:
        break
bob.end_fill()
turtle.done()
