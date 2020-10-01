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
