#!/usr/bin/env python
#-*- coding: utf-8 -*-
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

puntos = int(input("¿Cuántos puntos tienes?"))
listax=[]
listay=[]

for i in range(0,puntos):
    listax.append(int(input("X"+ str(i+1) +": ")))
    listay.append(int(input("Y"+str(i+1)+": ")))

xi=np.array(listax)
yi=np.array(listay)

n = len(xi)
x = sym.Symbol('x')

polinomio = 0
for i in range(0,n,1):

    termino = 1
    for j  in range(0,n,1):
        if (j!=i):
            termino = termino*(x-xi[j])/(xi[i]-xi[j])
    polinomio = polinomio + termino*yi[i]

px = polinomio.expand()

pxn = sym.lambdify(x,polinomio)


a = np.min(xi)
b = np.max(xi)
muestras = 101
xi_p = np.linspace(a,b,muestras)
yi_p = pxn(xi_p)

print('Polinomio de Lagrange, expresiones\n')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(px)

plt.title('Interpolación Lagrange')
plt.plot(xi,yi,'o', label = 'Puntos')
plt.plot(xi_p,yi_p, label = 'Polinomio')
plt.legend()
plt.show()
