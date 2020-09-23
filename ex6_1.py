import turtle as tr
tr.shape('turtle')
def spider(n):
    for i in range (n):
        tr.forward(50)
        tr.stamp()
        tr.backward(50)
        tr.right(360/n)
p=12
spider(p)