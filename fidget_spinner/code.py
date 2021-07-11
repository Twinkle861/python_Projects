import turtle
from turtle import *
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, '#e36bae')
    back(100)
    right(120)
    forward(100)
    dot(120, '#72147e')
    back(100)
    right(120)
    forward(100)
    dot(120, '#55ae95')
    back(100)
    right(120)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=20

setup(500, 500, 370, 0)
hideturtle()
turtle.Screen().bgcolor('#f5f7b2')

tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()