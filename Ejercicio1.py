def celsius_fahrenheit(a):
    return float((cel * (9/5)) + 32)

cel = float(input("INGRESE SU DATO EN GRADOS CELSIUS:\t\t"))

print(f"{cel} Grados Celsius son {celsius_fahrenheit(cel)} Grados Fahrenheit")