from turtle import *
import colorsys

# setup
speed(0)
pensize(3)
bgcolor("black")
tracer(10) # setup for fast drawing

h = 0
penup()
goto(0, -100) # setup position
pendown()

for i in range(500):
    # color change logic
    col = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.005
    
    fillcolor(col)
    begin_fill()
    
    # design creation logic
    circle(i, 45)
    left(80)
    circle(i, 45)
    
    end_fill()
    left(145) # this angle rotates the design

done()