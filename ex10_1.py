import turtle as tr
tr.shape('turtle')
tr.speed(0)
def circle(n):
	turn = 360/n
	for i in range(n):
		tr.forward(1)
		tr.right(turn)
p=400
for i in range(6):
    circle(p)
    tr.right(60)
