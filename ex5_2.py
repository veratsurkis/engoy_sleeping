from random import randint
import turtle as tr


number_of_turtles = 20
steps_of_time_number = 200

A = []

pool = [tr.Turtle(shape='circle') for i in range(number_of_turtles)]
i=0
for unit in pool:
    unit.penup()
    unit.goto(randint(-300, 300), randint(-300, 300))
    A.append(randint(0, 360))
    unit.right(A[i])
    unit.speed(0)
    i+=1


for i in range(steps_of_time_number):
    j=0
    for unit in pool:
        unit.forward(2)
        if (unit.ycor()>=300 or unit.ycor()<=-300):
          unit.left(2*A[j]) 
        if (unit.xcor()>=300 or unit.xcor()<=-300):
          unit.right(2*A[j])
        j+=1