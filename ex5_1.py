import turtle as tr
tr.shape('turtle')
def square(a, n):
    for i in range(n):
        for j in range(4):
            tr.forward(a)
            tr.right(90)
        a+=10
        tr.penup()
        tr.left(135)
        tr.forward(5*(2**0.5))
        tr.pendown()
        tr.right(135)
p=50
square(p, 10)
