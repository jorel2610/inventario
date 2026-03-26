# año de edad multiplo de 5
nacimiento = int(input("ingresa tu año de nacimiento"))
anio_inicio = int(input("ingrese año inicial del rango"))
anio_fin = int(input("ingrese año fianl del rango"))
print(f"\nAños en los que tendrás edad múltiplo de 5 entre {anio_inicio} y {anio_fin}:\n")

for anio in range(anio_inicio, anio_fin + 1):
    edad = anio - nacimiento
    if edad % 5 == 0 and edad >= 0:
        print(f"Año {anio} → tenías/ tendrás {edad} años")