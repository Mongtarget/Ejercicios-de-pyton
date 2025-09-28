numero1=int(input("Ingrese primer numero:"))
numero2=int(input("Ingrese segundo numero:"))
numero3=int(input("Ingrese tercer numero:"))

if numero1>numero2:
    if numero1>numero3:
        print("El numero mayor es:",numero1)
    else:
        print("El numero mayor es:",numero3)
else:
    if numero2>numero3:
        print("El numero mayor es:",numero2)
    else:
        print("El numero mayor es:",numero3)
