from turtle import *

shape("turtle")
bgcolor("Black")
back(-100)
left(90)
back(100)
color("red","yellow")

for i in range(50):
        begin_fill()
        for i in range(5):
                forward(200-(i*5))
                left(50)
        end_fill()

done()