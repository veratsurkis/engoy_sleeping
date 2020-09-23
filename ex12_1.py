import turtle as tr
tr.shape('turtle')
tr.speed(0)
def half_circle(n):
	turn = 360/n
	for i in range(n//2):
		tr.forward(1)
		tr.right(turn)
r_1=300
r_2=50
p=5
tr.left(90)
for i in range(p):
    half_circle(r_1)
    half_circle(r_2)