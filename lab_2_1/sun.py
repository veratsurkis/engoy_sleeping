import turtle as tr
tr.shape('turtle')
tr.color('orange', 'yellow' )
def sun(k, n): 
    for i in range(k):
        for j in range(n//k):
            tr.forward(3)
            tr.right(360/n)
        tr.left(90)
        tr.forward(50)
        tr.backward(50)
        tr.right(90)
tr.hideturtle()
tr.begin_fill()
sun(10,100)
tr.end_fill()

