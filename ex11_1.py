import turtle as tr
tr.shape('turtle')
tr.speed(0)
def circle(n):
	turn = 360/n
	for i in range(n):
		tr.forward(1)
		tr.right(turn)
p=100
for i in range(10):
    circle(p)
    tr.right(180)
    circle(p)
    tr.right(180)
    p+=50
