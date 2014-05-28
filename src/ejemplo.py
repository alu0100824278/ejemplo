#!/usr/bin/python
#! encoding: UTF-8

import time
#Pedimos número de filas y columnas.

m = int(raw_input("Introduzca el numero de filas de las matrices: "))
n = int(raw_input("Introduzca el numero de columnas de las matrices: ")) 

M = []
N = []
C = []

for i in range (m):
  M.append([0]*n)
  N.append([0]*n)
  C.append([0]*n)
  
for i in range (m):
  for j in range (n):
    M[i][j] = int(raw_input("Introduzca la coordenada (%d,%d) de la matriz M: " % (i, j)))

print ("Matriz M:")
print M
  
for i in range (m):
  for j in range (n):
    N[i][j] = int(raw_input("Introduzca la coordenada (%d,%d) de la matriz N: " % (i, j)))

print ("Matriz N:")
print N

inicio = time.time()

for i in range (m):
  for j in range (n):
    C[i][j] = M[i][j] + N[i][j]

print ("La suma de las dos matrices:")
print C
  
final = time.time()
total = final - inicio
print ("Tiempo tardado en realizar la suma de matrices = %f segundos") % total

f = open("Resultados.tex", "w")
f.write("\nSuma: \n")
f.write(str(C))
f.write("\nTiempo tardado = %f" % total)
f.close()

f=open("Resultados.tex","r")
print(f.read())
f.close()