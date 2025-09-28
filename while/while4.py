cantidad = 0
x = 1
n = int(input("cuantas piezas cargara:"))
while x <= n:
    largo = float(input("ingrese el largo de la pieza:"))
    if largo > 1.2 and largo <= 1.3:
        cantidad = cantidad + 1
    x = x + 1
print("la cantidad de piezas aptas son:", cantidad)