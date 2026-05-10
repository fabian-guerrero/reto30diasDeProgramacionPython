precioCompra = 0.00
dineroEntregado = 0.00
precioEnCentimos = 0
entregadoEnCentimos = 0
cambioCompra = 0.00
cambioEnCentimos = 0
billetesUtilizados = 0
monedasUtilizadas = 0

precioCompra = float(input("Introduce el precio de la compra: "))
while precioCompra <= 0:
    print("El precio de la compra debe ser mayor que cero")
    precioCompra = float(input("Introduce el precio de la compra: "))

dineroEntregado = float(input("Introduce el dinero entregado: "))
while dineroEntregado <= 0:
    print("El precio de la compra debe ser mayor que cero")
    dineroEntregado = float(input("Introduce el dinero entregado: "))

if dineroEntregado < precioCompra:
    print("El dinero enregado es insuficiente")
else:
    print(f"dineroEntregado {dineroEntregado}")
    print(f"precioCompra {precioCompra}")

    precioEnCentimos = int(precioCompra * 100)
    entregadoEnCentimos = int(dineroEntregado * 100)

    cambioCompra = round((dineroEntregado - precioCompra),2)
    cambioEnCentimos = int(cambioCompra * 100)

    print(f"""
    Precio de la compra: {precioCompra}
    Dinero entregado: {dineroEntregado}

    Cambio total: {round(cambioCompra,2)}€

    """)

    if cambioEnCentimos >= (500 * 100):
        billetes500 = cambioEnCentimos // (500 * 100)
        cambioEnCentimos = cambioEnCentimos % (500 * 100)
        print(f"Billetes de 500€: {billetes500}")
        billetesUtilizados += billetes500

    if cambioEnCentimos >= (200 * 100):
        billetes200 = cambioEnCentimos // (200 * 100)
        cambioEnCentimos = cambioEnCentimos % (200 * 100)
        print(f"Billetes de 200€: {billetes200}")
        billetesUtilizados += billetes200

    if cambioEnCentimos >= (100 * 100):
        billetes100 = cambioEnCentimos // (100 * 100)
        cambioEnCentimos = cambioEnCentimos % (100 * 100)
        print(f"Billetes de 100€: {billetes100}")
        billetesUtilizados += billetes100

    if cambioEnCentimos >= (50 * 100):
        billetes50 = cambioEnCentimos // (50 * 100)
        cambioEnCentimos = cambioEnCentimos % (50 * 100)
        print(f"Billetes de 50€: {billetes50}")
        billetesUtilizados += billetes50

    if cambioEnCentimos >= (20 * 100):
        billetes20 = cambioEnCentimos // (20 * 100)
        cambioEnCentimos = cambioEnCentimos % (20 * 100)
        print(f"Billetes de 20€: {billetes20}")
        billetesUtilizados += billetes20

    if cambioEnCentimos >= (10 * 100):
        billetes10 = cambioEnCentimos // (10 * 100)
        cambioEnCentimos = cambioEnCentimos % (10 * 100)
        print(f"Billetes de 10€: {billetes10}")
        billetesUtilizados += billetes10

    if cambioEnCentimos >= (5 * 100):
        billetes5 = cambioEnCentimos // (5 * 100)
        cambioEnCentimos = cambioEnCentimos % (5 * 100)
        print(f"Billetes de 5€: {billetes5}")
        billetesUtilizados += billetes5

    if cambioEnCentimos >= (2 * 100):
        monedas2 = cambioEnCentimos // (2 * 100)
        cambioEnCentimos = cambioEnCentimos % (2 * 100)
        print(f"Monedas de 2€: {monedas2}")
        monedasUtilizadas += monedas2

    if cambioEnCentimos >= (1 * 100):
        monedas1 = cambioEnCentimos // (1 * 100)
        cambioEnCentimos = cambioEnCentimos % (1 * 100)
        print(f"Monedas de 1€: {monedas1}")
        monedasUtilizadas += monedas1

    if cambioEnCentimos >= (0.5 * 100):
        monedas050 = int(cambioEnCentimos // (0.5 * 100))
        cambioEnCentimos = cambioEnCentimos % (0.5 * 100)
        print(f"Monedas de 50 céntimos: {monedas050}")
        monedasUtilizadas += monedas050

    if cambioEnCentimos >= (0.2 * 100):
        monedas020 = int(cambioEnCentimos // (0.2 * 100))
        cambioEnCentimos = cambioEnCentimos % (0.2 * 100)
        print(f"Monedas de 20 céntimos: {monedas020}")
        monedasUtilizadas += monedas020


    if cambioEnCentimos >= (0.1 * 100):
        monedas010 = int(cambioEnCentimos // (0.1 * 100))
        cambioEnCentimos = cambioEnCentimos % (0.1 * 100)
        print(f"Monedas de 10 céntimos: {monedas010}")
        monedasUtilizadas += monedas010


    if cambioEnCentimos >= (0.05 * 100):
        monedas005 = int(cambioEnCentimos // (0.05 * 100))
        cambioEnCentimos = cambioEnCentimos % (0.05 * 100)
        print(f"Monedas de 5 céntimos€: {monedas005}")
        monedasUtilizadas += monedas005

    if cambioEnCentimos >= (0.02 * 100):
        monedas002 = int(cambioEnCentimos // (0.02 * 100))
        cambioEnCentimos = cambioEnCentimos % (0.02 * 100)
        print(f"Monedas de 2 céntimos: {monedas002}")
        monedasUtilizadas += monedas002

    if cambioEnCentimos >= (0.01 * 100):
        monedas001 = int(cambioEnCentimos // (0.01 * 100))
        cambioEnCentimos = cambioEnCentimos % (0.01 * 100)
        print(f"Monedas de 1 céntimo: {monedas001}")
        monedasUtilizadas += monedas001

    print(f"""
    Total de billetes utilizados: {billetesUtilizados}
    Total de monedas utilizadas: {monedasUtilizadas}
    """)