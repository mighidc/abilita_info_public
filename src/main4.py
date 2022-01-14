import sys
import math
import numpy as np
import time

def divide(x, y):
 try:
  result = x / y
 except ZeroDivisionError:
  print("division by zero!")     
 else:       
  print("result is", result)    
 finally:         
  print("executing finally clause")

print(divide(4,0))





for i in range (-1,-10,-1):
  print(i)

for i in range (1,10,5):
  print(i)


m=range(3,10,4)
for n in m:
  print("range")
  print(n)


a=("Pierpaolo", "Gianmarco", "Luca")
b=("Michela", "Marta", "Monica")
x=zip(a,b)
print(tuple(x))



coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)
result_list = list(result)
print(result_list)
c, v =  zip(*result_list)
print('c =', c)
print('v =', v)


