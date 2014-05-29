#!/usr/bin/python
#! encoding: UTF-8

elem = int(raw_input("Numero de elementos del vector 1: "))
el = int(raw_input("Numero de elementos del vector 2: "))
v1 = []
v2 = []
suma = []

for i in range (elem):
  v1.append([0]*elem)
for i in range (el):
  v2.append([0]*el)
  
if (elem > el):
  suma.append([0]*elem)
else:
  suma.append([0]*el)
  

for i in range (elem):
  v1[i]=int(raw_input(("Cordenada (%d) del vector 1: ") % i))
for i in range (el):
  v2[i]=int(raw_input(("Cordenada (%d) del vector 2: ") % i))
  
if (elem > el):
  for i in range (elem):
    suma[i] = v1[i] + v2[i]

else :
  for i in range (el):
    suma[i] = v1[i] + v2[i]
    
print "Vector 1: " 
print v1
print "Vector 2: " 
print v2
print "Suma:"
print suma