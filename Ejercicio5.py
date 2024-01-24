a = input("INGRESE UN DATO: ")

if '.' in a:
    print("EL DATO INGRESADO ES UN DECIMAL")
elif a.isdigit():
    print("EL DATO INGRESADO ES UN NUMERO")
else:
    print("EL DATO INGRESADO ES UN TEXTO")