import turtle as t
import math
import numpy as np

t.speed(10)
intital_rotation = 90
size = 6

def fibonnacci(n):
    if n < 2:
        return [1,1]
    else:
        output = [1,1]
        for i in range(n-2):
            output.append(output[i]+output[i+1])
        return output


#the spiral is defined as a parametric function
#the function below is distance traveled per t, which is the derivative of the arc length fomula
def speed_relative_to_t(x):
    phi = (1 + np.sqrt(5)) / 2  # golden ratio
    term1 = (2 / np.pi) * (phi ** (2 * x / np.pi)) * np.log(phi) * np.sin(x)
    term2 = (phi ** (2 * x / np.pi)) * np.cos(x)
    term3 = (2 / np.pi) * (phi ** (2 * x / np.pi)) * np.log(phi) * np.cos(x)
    term4 = -(phi ** (2 * x / np.pi)) * np.sin(x)
    
    result = np.sqrt((term1 + term2)**2 + (term3 + term4)**2)
    return result

def draw_square(r):
    for i in range(6):
        t.forward(r)
        if(i != 5):
            t.left(90)


#Creates borders
t.setheading(intital_rotation)
for index, fib_num in enumerate(fibonnacci(10)):
    draw_square(fib_num*size)

#initiate spiral drawing
t.up()
t.home()
t.down()
t.seth(intital_rotation)

for i in fibonnacci(10):
    t.circle(i*size,90)


#initiate spiral drawing
t.pencolor("red")
t.up()
t.home()
t.down()
t.seth(intital_rotation)

precision = 15 #this number is 
distance = 20 #how far the turtle should go
for i in range(int(distance*precision)):
    t.forward(0.5333*size*speed_relative_to_t(i/precision)/precision)
    t.left(180/(math.pi*precision)) #this number is degree change of the spiral per t, which is the derivate of arctan(slope)pi/180 with respect to t



t.exitonclick()

