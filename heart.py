import math
from turtle import *
 
def heart(t):
    return 16*math.sin(t)**3
 
def heart1(t):
    return 13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t)
 
speed(10)
bgcolor('black')
for i in range(1000):
    goto(heart(i)*20, heart1(i)*20)
    for j in range(5):
        color("light blue")
 
done()
  