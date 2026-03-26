print("=== CAJA REGISTRADORA SIMPLE ===\n")
total = 0.0
cantidad = 0
while True:
    precio = float(input("ingresas el precio del producto ( 0 para terminar)"))
    if precio == 0:
        break
    total += precio 
    cantidad += 1
# despues de salir del bluce
if cantidad> 0:
    promedio =total / cantidad 
    print("\n--- resumen de la compra---")
    print(f"total acomulado: $ {total:,.2f}")
    print(f"cantidad de producto:{cantidad}")
    print(f"promedio por producto: ${promedio:,.2f}")
else:
    print("\nNo se ingresaron producto.")
