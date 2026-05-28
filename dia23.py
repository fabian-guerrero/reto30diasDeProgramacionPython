inventario = {
    "pocion": 3,
    "espada": 1,
    "escudo": 2
}

opcion = 0

def menu():
    print("""----- INVENTARIO DEL MERCADER -----

1. Ver inventario
2. Consultar producto
3. Añadir unidades
4. Vender producto
5. Salir""")

    opcion = int(input("Introduce una opcion: "))
    return opcion

while opcion != 5:
    opcion = menu()

    if opcion == 1 and len(inventario) == 0:
        print("El inventario esta vacio")
    elif opcion == 1:
        for clave, valor in inventario.items():
            print(f"{clave} → {valor} unidades")
    elif opcion == 2:
        consultaProducto = input("¿Que producto desea consultar? ")
        if consultaProducto in inventario:
            cantidad = inventario.get(consultaProducto)
            print(f"{consultaProducto}: {cantidad} unidades")
        else:
            print("Ese producto no existe en el inventario.")
    elif opcion == 3:
        producto = input("¿Que producto desea añadir? ")
        cantidadAniadir = int(input("¿Que cantidad de producto desea añadir? "))
        if producto in inventario:
            cantidadActual = inventario.get(producto)
            cantidadNueva = cantidadActual + cantidadAniadir
            inventario[producto] = cantidadNueva
            print(f"{producto} tenía {cantidadActual} unidades.")
            print(f"Ahora tiene {cantidadNueva} unidades.")
        else:
            inventario[producto]= cantidadAniadir
            print("Producto nuevo añadido al inventario.")
    elif opcion == 4:
        venderProducto = input("¿Que producto desea vender? ")
        venderCantidad = int(input("¿Que cantidad de producto desea vender? "))
        if venderProducto not in inventario:
            print("Ese producto no existe.")
        elif inventario.get(venderProducto) > venderCantidad:
            inventario[venderProducto] = inventario.get(venderProducto) - venderCantidad
            print("Venta realizada correctamente.")
        elif inventario.get(venderProducto) < venderCantidad:
            print("No hay suficientes unidades.")
        elif inventario.get(venderProducto) == venderCantidad:
            del inventario[venderProducto]
            print("Venta realizada correctamente.")

print("Inventario cerrado.")