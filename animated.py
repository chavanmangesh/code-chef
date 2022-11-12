
#Animated video through python program

from turtle import *

speed(0.5)
bgcolor("black")
c=["orange","white","green"]
pensize(2)

for i in range(450):
    color(c[i%3])
    fd(i)
    lt(80)
done()