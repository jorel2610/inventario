# Ejercicio 2 - Adivina el número secreto
secreto = 42
intentos = 0

print("¡Adivina el número secreto!")
print("(Está entre 1 y 100)")

while True:
    intento = int(input("Ingresa tu número: "))
    intentos += 1
    
    if intento < secreto:
        print("El número secreto es mayor ↑")
    elif intento > secreto:
        print("El número secreto es menor ↓")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
