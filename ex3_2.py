import turtle as tr
tr.shape('turtle')
tr.penup()


def draw_num(A):
    tr.pendown()
    for i in range(len(A)):
        a,x,flag = A[i]
        if flag==1:
            tr.penup()
            tr.right(a)
            tr.forward(x)
            tr.pendown()
        else:
            tr.right(a)
            tr.forward(x)
    tr.penup()
    tr.forward(30)
    tr.right(90)
    tr.forward(50)
    tr.left(90)


S=10*[0]
NUM=10*[0]
sleep = open("ex3_tmp.txt", 'r')
for i in range(10):
    S[i]=sleep.readline()
    S[i]=S[i].rstrip()
    NUM[i]=eval(S[i])

for i in range(1, 4, 1, 7, 0, 0):
    draw_num(NUM[i])