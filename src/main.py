import sys
import math
import numpy as np

r = 12+5j
print(type(r))
print(type(r.real))

a=4.0872
print(type(a))

#c = not(3 and 6)
#print(c)

f=math.sin(np.pi/6)
print(f)
m=math.cos(30)
print(m)

a2= 'hola' + ' amigos'
print(a2)

a3= 'hola\tamigos'
print(a3)

n=a3.replace("a", "aa", 2)
print(n)

name = 'Mighi'
mystring="hola %s" %name
print(mystring)

mystring2="hola %s! Come va? %s" %(name, "Bene, grazie!! Tu?")
print(mystring2)

g="What\'s the day today?"
print(g)

o = "oggi è %s %d %s" %("venerdì", 10, "dicembre")
print(o)


