print("=== CAJERO AUTOMÁTICO ===")

saldo = 1000000
while True:
    print(f"Saldo actual: ${saldo}")
    print("""
1. Consignar
2. Retirar
3. Salir
""")
    opcion = input("\nElegir una opcion (1-3): ").strip()
    if opcion =="1": # CONSIGNAR 
        monto = float(input("ingrese a cantidad a consignar : $"))
        if monto > 0:
            saldo += monto
            print(f"consignacion exitpsa. Nuevo saldo $ {saldo:,.2f}")
        else:
            print("Error: la cantidad debe ser mayo a 0.")
   
    elif opcion == "2": # RETIRAR
        monto = float(input("ingrese la cantidad a retirar:$"))
        if monto> 0: 
            if monto <= saldo:
                saldo -= monto
                print(f"ritora exitoso. Nuevo saldo: $ {saldo:,.2f}")
            else:
                print("Error: no tines suficiente saldo para realizar el retiro.")
        else:
            print("Error: la cantidad debe ser mayo a.")
    
    elif opcion =="3": # SALIR
        print("\n¡Gracias por usar el cajero automatico1!")
        break
    