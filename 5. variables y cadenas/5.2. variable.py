opcion = "s"
suma = 0
while opcion == "s":
    numero = int(input("Ingrese un número: "))
    suma += numero
    opcion = input("¿Desea ingresar otro número? (s/n): ").lower()
print("La suma total es:", suma)