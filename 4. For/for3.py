mul3 = 0
mul5 = 0

for f in range (10):
    valor = int(input("Digite um valor: "))
    if valor % 3 == 0:
        mul3 += 1
    if valor % 5 == 0:
        mul5 += 1
print("multiplos de 3: ", mul3)
print("multiplos de 5: ", mul5)
