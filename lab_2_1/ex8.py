import turtle as tr
tr.shape('turtle')
def sq_spir(a,n):
    for i in range(n):
            tr.forward(a)
            tr.right(90)
            a+=10
p=20
sq_spir(10,p)