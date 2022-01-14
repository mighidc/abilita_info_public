import sys
import math
import numpy as np
import time

infile='src/mydata.txt'
outfile='src/myout.txt'

def f(y):
 if y >= 0.0:
   return y**5*math.exp(-y)
 else:
   return 0.0

   
indata = open( infile, 'r')
linee=indata.readlines()
indata.close()
processati=[ ]
x=[ ]
for el in linee:
 valori = el.split()
 print(valori)
 x.append(float(valori[0])); y = float(valori[1])
 processati.append(f(y))
 print(processati)


outdata = open(outfile, 'w')
i=0
for el in processati:
 outdata.write('%g %12.5e\n' % (x[i],el))
 i+=1
outdata.close()




a=3
b=[[3,6,9],
 [1,2,3],
 [2,4,8]]

def matrix_per_scalar(matrix, scalar):
 result=[]
 for i in range(len(matrix)):
  tmp=[]
  for j in range(len(matrix[i])):
   tmp.append(matrix[i][j]*scalar)
  result.append(tmp)
 return result


def print_matrix(matrix):
 for i in range(len(matrix)):
  for j in range(len(matrix[i])):
   print(str((matrix[i][j]))+"\t", end='')
  print("\n")


print("Input:")
print("Scalar=" + str(a))
print("Matrix=")
print_matrix(b)
print("Matrix x scalar multiplication result:")
print_matrix(matrix_per_scalar(b,a))



# Program to multiply two matrices
# using nested loops
# 3x3 matrix
A = [[12,7,3],
 [4 ,5,6],
 [7 ,8,9]]
# 3x4 matrix
B = [[5,8,1,2],
 [6,7,3,0],
 [4,5,9,1]]
def print_matrix(matrix):
 for i in range(len(matrix)):
  for j in range(len(matrix[i])):
   print(str((matrix[i][j]))+"\t", end='')
  print("\n")
def matrix_x_matrix(X, Y):
# iterate through rows of X
# result is 3x4
 result = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
 for i in range(len(X)):
# iterate through columns of Y
  for j in range(len(Y[0])):
# iterate through rows of Y
   for k in range(len(Y)):
    result[i][j] += X[i][k] * Y[k][j]
 return result

print("Input")
print("A = ")
print_matrix(A)
print("B = ")
print_matrix(B)
print("Output AxB")
print_matrix(matrix_x_matrix(A, B))



class Person:
 def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Michela", 22)
print(p1.name)
print(p1.age)


