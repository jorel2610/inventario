# --- Validación de entrada ---
while True:
    num_limite = int(input("Ingresa un número entero positivo: "))
    if num_limite >= 2:
        break
    print(" Por favor, ingresa un número mayor o igual a 2.")

print(f"\n🔎 Analizando números primos hasta el {num_limite}:")
print("-" * 40)

# Bucle exterior: recorre cada número del 2 al límite
for n in range(2, num_limite + 1):
    es_primo = True
    
    # Bucle interior: busca divisores desde 2 hasta la raíz cuadrada de n (optimizado)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            es_primo = False
            break  # Si encontramos un divisor, ya no es primo
            
    if es_primo:
        if n == num_limite:
            print(f"⭐ {n} es el número que ingresaste y ¡ES PRIMO!")
        else:
            print(f"Primo encontrado: {n}")

print("-" * 40)
