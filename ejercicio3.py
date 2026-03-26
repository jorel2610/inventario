# numeros divisibles por 3 o 5 pero no por ambos
n = int(input("ingrese un numero entero positivo"))
contador = 0
print(f"numero del 1 al{n} divisible por 3 o 5 pero no por ambos:")
for i in range(1, n + 1):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0):
        print(i, end="")
        contador += 1
        print(f"\n\nTotal de numeros que cumple  la condicion: {contador}")  
