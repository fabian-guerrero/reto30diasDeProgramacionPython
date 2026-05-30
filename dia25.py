import random

def menu_opciones():
    print(f"""
----- APERTURA DE SOBRES -----

1. Abrir sobre
2. Ver colección
3. Consultar carta
4. Ver estadísticas
5. Salir

""")

    opcion = int(input("Introduce una opcion: "))
    return opcion


cartas = ["Caballero","Arquera","Mago","Gigante","Dragón","Bruja","Príncipe"]
coleccion = {}
cartasDiferentes = 0
cantidadCartas = 0
masObtenida = 0
menosObtenida = 1

opcion = menu_opciones()

while opcion != 5:
    if opcion == 1:
        print("Has obtenido:")
        print("")
        for i in range(1,6):
            cartaSobre = random.randint(0,len(cartas)-1)
            cartaSobre = cartas[cartaSobre]
            if cartaSobre not in coleccion:
                coleccion[cartaSobre] = 1
                print(f"{cartaSobre}")
            else:
                coleccion[cartaSobre] += 1
                print(f"{cartaSobre}")
        print(coleccion)
        print(len(coleccion))
    elif opcion == 2:
        if len(coleccion) == 0:
            print("No tienes cartas en la coleccion")
        else:
            for carta, cantidad in coleccion.items():
                print(f"{carta} → {cantidad}")
    elif opcion == 3:
        consulta = input("¿Qué carta quieres consultar? ")
        if consulta in coleccion:
            print(f"Tienes {coleccion[consulta]} {consulta}")
        else:
            print("No has conseguido esa carta todavía.")
    elif opcion == 4:
        cartasDiferentes = len(coleccion);
        for valor in coleccion.values():
            cantidadCartas += valor

        for carta, cantidad in coleccion.items():
            if cantidad > masObtenida:
                masObtenida = cantidad
                claveMasObtenida = carta
            elif cantidad <= menosObtenida:
                menosObtenida = cantidad
                claveMenosObtenida = carta

        print(f"Carta más obtenida: {claveMasObtenida} ({masObtenida})")
        print(f"Carta menos obtenida: {claveMenosObtenida} ({menosObtenida})")

        print(f"Cartas diferentes: {cartasDiferentes}")
        print(f"Total de cartas: {cantidadCartas}")
    else:
        print("Has seleccionado una opcion no valida")

    opcion = menu_opciones()

print("Has salido del programa")