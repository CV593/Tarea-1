
def horas_segundos (a):
    return a*3600

def minutos_segundos (a):
    return a*60

ingreso = input("INGRESE LA HORA ACTUAL DE FORMA HH:MM \t")
h,m = map(int, ingreso.split(":"))

if 0 <= h < 24 and 0 <= m < 60:
    print(f"Han pasado {horas_segundos(h)+minutos_segundos(m)} segundos del dia")
else:
    print("LOS VALORES INGRESADOS SON INCORRECTOS")