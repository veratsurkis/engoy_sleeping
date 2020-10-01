import turtle as tr
tr.shape('circle')
tr.speed(0)
tr.penup()
tr.goto(-500,0)
tr.pendown()
x=-500
y=0
ay=-1
dt=0.05
for i in range(4):
    Vx=10-2*i
    Vy=20-2*i
    while y>=0:
        tr.goto(x,y)
        x += Vx*dt
        y += Vy*dt + ay*dt**2/2
        Vy += ay*dt
    y=0