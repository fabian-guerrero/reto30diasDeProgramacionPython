from decimal import *

producto = input("Indique el nombre del producto: ")
precioUnitario = int(input("Indique el precio unitario del producto: "))
cantidad = int(input("Indique la cantidad de la compra: "))
IVA = 21

subtotal = precioUnitario * cantidad
ivaCompra = subtotal * (IVA/100)
totalCompra = Decimal(subtotal + ivaCompra).quantize(Decimal('0.00'))
compraGrande = totalCompra >= 20

print(f"""
------ TICKET ------
Producto: {producto}
Cantidad: {cantidad}
Precio unitario: {precioUnitario}€
Subtotal: {subtotal}€
IVA ({IVA}%): {ivaCompra}€
TOTAL: {totalCompra}€
--------------------
""")

if compraGrande:
    print("Compra grande")
else:
    print("Compra pequeña")

