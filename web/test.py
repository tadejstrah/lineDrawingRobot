import random
import time
import turtle
import math
tabela=[]
a=0
turtle.pu()
turtle.goto(0, 0)
while a <= 10000:
    x=random.randint(-100, 100) #ker je naš uporabnik pač moderni umetnik
    y=random.randint(-100, 100)
    a = a + math.sqrt((x*x) + (y*y))
    tabela.append({"x":x, "y":y})
turtle.pd()
print(tabela)
for koordinata in  tabela:
    turtle.goto(koordinata["x"], koordinata["y"])
