import turtle as tr
import numpy as np
tr.shape('turtle')
tr.speed(0)
def circle(n):
	turn = 360/n
	for i in range(n):
		tr.forward(1)
		tr.right(turn)
def half_circle(n):
	turn = 360/n
	for i in range(n//2):
		tr.forward(1)
		tr.right(turn)


tr.left(90)
tr.color('black', 'yellow')
tr.begin_fill()
circle(500)
tr.end_fill()
tr.penup()
diam=1/np.sin(np.pi/500)
tr.goto(diam/6,diam/4)
tr.color('black', 'blue')
tr.pendown()
tr.begin_fill()
circle(80)
tr.end_fill()
tr.penup()
diam_gl=1/np.sin(np.pi/80)
tr.goto(5*diam/6-diam_gl,diam/4)
tr.pendown()
tr.begin_fill()
circle(80)
tr.end_fill()
tr.penup()
tr.goto(diam/2,diam/4)
tr.pendown()
tr.width(10)
tr.goto(diam/2,-diam/4)
tr.penup()
tr.goto(5*diam/6,0)
n_lips=int(np.pi/np.arcsin(3/(2*diam)))
tr.left(180)
tr.color('red')
tr.pendown()
half_circle(n_lips)

