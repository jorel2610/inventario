# pedir al usuario un numero pisitivo 
numero = int(input("ingrresa un numero entero positivo"))
# valida que el numero sea positivo
while numero <= 0:
    print("¡erro! el numero debe ser positivo")
    numero = int(input("ingresa un numero entero positivo:" ))
# mostrar la tebla de multiplicasion del 1 al 10 
print(f"\nTabla de multiplicar del {numero}:\n")
for i in range(1, 11):
      print(f"{numero} x {i:2d} = {numero * i:3d}")
