import turtle as tr
tr.shape('turtle')
def circle(n):
	turn = 360/n
	for i in range(n):
		tr.forward(3)
		tr.right(turn)
p = 100
circle(p)