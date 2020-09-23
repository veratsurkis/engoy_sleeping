import turtle as tr
import numpy as np
tr.shape('turtle')
def star(n):
    for i in range(n):
        tr.forward(100)
        tr.right(180-180/n)

star(5)
tr.penup()
tr.forward(200)
tr.pendown()
star(11) 