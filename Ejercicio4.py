from math import sqrt

def evaluacion (a,b,c):
    return b ** 2 - 4 * a * c
def x (a,b,c):
    if evaluacion(a,b,c) > 0:
        x1 = (-b + sqrt(evaluacion(a,b,c)))/(2*a)
        x2 = (-b - sqrt(evaluacion(a,b,c)))/(2*a)
        return x1,x2
    else:
        return None
    
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

soluciones = x(a, b, c)

if soluciones is not None:
    print(f"Las soluciones son: x1 = {soluciones[0]}, x2 = {soluciones[1]}")
else:
    print("No hay soluciones reales.")  