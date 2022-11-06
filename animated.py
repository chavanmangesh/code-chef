from turtle import *

speed(0)
bgcolor("black")
c=["orange","white","green"]
pensize(2)

for i in range(450):
    color(c[i%3])
    fd(i)
    lt(91)
done()

