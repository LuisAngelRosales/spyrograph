from turtle import Turtle, Screen
from random import Random

turtle=Turtle()
screen=Screen()
random=Random()

screen.colormode(255)
turtle.speed(0)

def random_colour():
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    return (r,g,b)
radius=100
while True:
    turtle.color(random_colour())
    turtle.circle(radius)
    turtle.left(1)
    radius+=0.1