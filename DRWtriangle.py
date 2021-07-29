from turtle import *

def draw_triangle():
    """Draw an equilateral triangle with sides of length 40 units"""
    for sides in range(0,3):
        forward (100)
        left (120)

draw_triangle()
penup()
forward(100)
pendown()

draw_triangle()
penup()
left(180)
forward(100)
right(90)
forward(100)
right(90)
pendown()

draw_triangle()
