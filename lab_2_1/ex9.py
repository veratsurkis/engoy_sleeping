import turtle as tr
import numpy as np
tr.shape('turtle')
def prav_n_ug(r_f,n):
    tr.penup()
    tr.forward(r_f)
    tr.pendown()
    tr.right(90*(n+2)/n)
    for i in range(n):
        tr.forward(r_f*2*np.sin(np.pi/n))
        tr.right(360/n)
    tr.right(90*(n-2)/n)
    tr.penup()
    tr.forward(r_f)
    tr.pendown()
r=20
for i in range (3,13):
    prav_n_ug(r,i)
    r+=10
