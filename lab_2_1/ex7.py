import turtle as tr
import numpy as np
tr.shape('turtle')
def spir(n):
    f=0
    d_f=1
    b_0=1
    for i in range(n):
        tr.right(1)
        f+=d_f
        b=b_0*(d_f*np.pi/180)*(1+(f*np.pi/180)**2)**0.5
        tr.forward(b)
p=10000
tr.speed(0)
spir(p)
