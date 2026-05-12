nombreProducto = ""
precioProducto = 0.00
acumuladoCompra = 0
totalCompra = 0
opcionMenu = 0

while opcionMenu != 4:
    print("""
        
    ----- SUPERMERCADO -----
    1. Añadir producto
    2. Ver total actual
    3. Aplicar descuento
    4. Finalizar compra
        
    """)

    opcionMenu = int(input("Seleccione una opcion del menu: "))

    if opcionMenu == 1:
        nombreProducto = input("Ingrese el nombre del producto: ")
        precioProducto = float(input("Ingrese el precio del producto: "))
        while precioProducto <= 0:
            print("El precio del producto debe ser mayor a cero")
            precioProducto = float(input("Ingrese el precio del producto: "))
        print(f"""
        Producto: {nombreProducto}
        Precio: {precioProducto}€

        Producto añadido correctamente.
        """)
        acumuladoCompra += precioProducto
        print(f"Total acumulado: {acumuladoCompra}€")
    elif opcionMenu == 2:
        print(f"Total actual: {acumuladoCompra}€")
    elif opcionMenu == 3:
        if acumuladoCompra > 100:
            print("Tiene un descuento del 20%")
        elif acumuladoCompra > 50:
            print("Tiene un descuento del 10%")
        else:
            print("No hay descuento disponible.")
    elif opcionMenu == 4:
        print(f"Total: {acumuladoCompra}€")
        if acumuladoCompra > 100:
            print(f"Descuento por compra mayor de 100: {acumuladoCompra * 0.2}€")
            print(f"Precio Final: {acumuladoCompra - (acumuladoCompra * 0.2)}€")
        elif acumuladoCompra > 50:
            print(f"Descuento por compra mayor de 50: {acumuladoCompra * 0.1}€")
            print(f"Precio Final: {acumuladoCompra - (acumuladoCompra * 0.1)}€")
        print("Gracias por su compra")
    else:
        print("Opcion no valida. Ingrese una opcion del menu")

