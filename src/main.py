import sys
import math
import numpy as np
import time 


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

k=['ciao','amici','belli']
print(k[0],k[1],k[2])
print(k)
print(k[0],k[1],k[2]*3)

g=[1,2,3,4,5,6,7,8]
h=[9,10,11,12]
print(g)
print(g[0:4])
print(g[0:4:2])
print(g[0::2])
print(g[7::-2])
print('la lunghezza è', len(g)) 
print(g+h)

s=range(1,9,1)
print(s[2],s[6],s[1])
t=[el*2 for el in s]
print("s", s)
print("t", t)

l=[1,2]
l2=["a","b"]
l3=[4,5,6]
f=[]

for e1 in l:
  for e2 in l2:
    for e3 in l3:
     f.append((e1,e2,e3))
     print(f)




l=list(range(1000000))
v=list(range(10000))
t1=time.perf_counter()
s=l+v
t2=time.perf_counter()
print("+execution time: :", t2-t1, "s")
t3=time.perf_counter()
l.extend(v)
t4=time.perf_counter()
print("extend execution time:", t4-t3, "s")


stack=[1,2,3,4]
print("initial stack:", stack)
for i in range (5,7):
  stack.append(i)
print("append:", stack)
stack.pop()
print("pop:", stack)


tup1=()
print(tup1)

tup2=(20,)
print(tup2[0])

tup3= 1,2,3,4
print(tup3)
print(tup3[2])
#del(tup3)
#print("dopo aver cancellato:", tup3)

print(len(tup3))
tup4=tup3+tup2
print(tup4)
print("il massimo è",max(tup4))


#dictionary
#dictionary with integer keys
my_d1={1:"apple", 7:"flower"}
my_d2=dict({1:"apple", "fiore":"flower"})
print(my_d1[1], my_d1[7])
print(my_d1.get(7))
print(my_d2[1], my_d2["fiore"])
print(my_d2.get("fiore"))

my_d2["fiore"]="tulip"
print(my_d2.get("fiore"))

my_d2["landscape"]="sea"
print(my_d2.get("landscape"))
print(my_d2)
print(my_d2.pop(1))
print(my_d2)
print(len(my_d2))
print(type(my_d2))



number=23
guess=int(input("enter an integer:"))

if guess == number:
 print("congrats, you've guessed it!")
elif guess < number:
  print("no, it's a little higher than that")
else:
  print("no, it's a little lower than that")
print("done")

number=18
running = True

while running:
  guess=int(input("enter an integer:"))

  if guess == number:
    print("congrats, you've guessed it!")
    running = False
  elif guess < number:
    print("no, it's a little higher than that")
  else:
    print("no, it's a little lower than that")
else:
  print("The while lop is over")
print("done")





for i in range (0,10):
  print(i)
else:
  print("the for loop is over")



a = "hola"
for el in a:
  print(el)





























