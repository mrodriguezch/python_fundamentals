
a=float(input("Ingrese a:"))
b=float(input("Ingrese b:"))
c=float(input("Ingrese c:"))

#actividad básica
print("="*50,"\nBásica\n","="*50)
from math import sqrt
def FGeneral(a,b,c):
    if((b**2)-4*a*c)<0:
        print("Solución Basica: La solución es compleja")
    else:
        x1=(-b+sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-sqrt(b**2-4*a*c))/(2*a)
        print("Solución Basica: Los valores son x1={0} y x2={1}".format(x1,x2))

FGeneral(a,b,c)

#actividad avanzada
print("="*50,"\nAvanzada\n","="*50)

import cmath
def FGeneralC(a,b,c):
    if((b**2)-4*a*c)<0:
        x1=(-b+cmath.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-cmath.sqrt(b**2-4*a*c))/(2*a)
    else:
        x1=(-b+sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-sqrt(b**2-4*a*c))/(2*a)
    print("Solución Avanzada: Los valores son x1={0} y x2={1}".format(x1,x2))

FGeneralC(a,b,c)
