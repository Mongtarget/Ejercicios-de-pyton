sueldo = float(input("Ingrese el sueldo: "))
antiguedad = int(input("Ingrese los años de antiguedad: "))

if sueldo < 500 and antiguedad >= 10:
    aumento = sueldo * 0.20
    print("El aumento es:", aumento)
    print("El nuevo sueldo es:", sueldo + aumento)
else:
    if sueldo < 500 and antiguedad < 10:
        aumento = sueldo * 0.05
        print("El aumento es:", aumento)
        print("El nuevo sueldo es:", sueldo + aumento)
    else:
        print("No tiene aumento")