import sys
import math
import numpy as np
#import time
#import matplotlib as mpl
#import matplotlib.pyplot as plt

import scipy.optimize

#np.info(scipy.optimize)

help(math.acos)

#l=[1,"alfa", 0.9, (1,2,3)]; 
#print [type(i) for i in l]

c=np.array([1,2,3,4])
d=np.array([[1,1,1,1],[2,2,2,2]])

print("d",d) 
print("c",c)
print("somma",d+c)

#def func_NumPy(x):
 # r=x.copy()
  #for i in range(np.size)

e=np.array([1,2,3,4])
list1=[1,2,3,4]
tupla=(5,6,7,8)
f=np.array(list1)
g=np.array(tupla)
h=np.array([list1,tupla])
print("h",h)
print(h.dtype)



b=np.array([5,6,7,8])
print("b", b)
c=np.arange(1,5)
print("c", c)
print("somma", b+c)
b+=1
print("b+=1", b)
print("sin(c)", np.sin(c))

v1=np.array([1,2,3])
v2=np.array([10,20,30])
print("prodotto componenti", v1*v2)
print("prodotto scalare", np.dot(v1,v2))

m1=np.matrix(v1)
m2=np.matrix(v2[:,np.newaxis])
print("m1", m1)
print("m2", m2)
print("prodotto scalare matrici", np.dot(m1,m2))

a=np.ones(4)
print("array1",a)
b=np.arange(1,5)
print("b",b)
print("somma", a+b)
print("prima componente b",b[0])
a[1:3]=a[1:3]*3 #modifica la seconda e la terza componente (delle 4 totali)
print("a_modificato",a)

a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("componente0",a[0,0])
print("riga3", a[2])
print("colonna 2",a[:,1])
print("sottomatrice2x2", a[2:,1:3])




a=np.arange(8)
print("a",a)
b=a[2:5]
print("b",b)
b[0]=15
b[2]=98
print("a",a, "b", b)

