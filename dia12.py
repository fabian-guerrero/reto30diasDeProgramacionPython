import random

saldo = 0
jugada = []

def validar_numero_positivo(mensaje):
    numero = int(input(mensaje))
    while numero <= 0:
        print("Debe introducir un numero positivo")
        numero = int(input(mensaje))
    return numero

def menu_opciones():
    print(f"""
----- TRAGAPERRAS -----

Saldo actual: {saldo} monedas

1. Jugar partida
2. Añadir saldo
3. Ver saldo
4. Salir

"""

    )

    opcion = int(input("Introduce una opcion: "))
    return opcion

opcion = menu_opciones()

while opcion != 4:

    if opcion == 1:
        if saldo <= 0:
            print("No tienes saldo suficiente para jugar.")
        else:
            jugada = []
            saldo -= 1
            for i in range(3):
                numAleatorio = random.randint(1,4)
                if numAleatorio == 1:
                    print("🍒", end="")
                    jugada.append(1)
                elif numAleatorio == 2:
                    print("🍋", end="")
                    jugada.append(2)
                elif numAleatorio == 3:
                    print("⭐️", end="")
                    jugada.append(3)
                elif numAleatorio == 4:
                    print("🔔", end="")
                    jugada.append(4)

            if jugada[0] == jugada[1] and jugada[0] == jugada[2]:
                print(f"""
¡PREMIO MAYOR!
Has ganado 10 monedas.
                """)
                saldo += 10
            elif jugada[0] == jugada[1] or jugada[0] == jugada[2] or jugada[1] == jugada[2]:
                print(f"""
¡PREMIO MENOR!
Has ganado 3 monedas.
                """)
                saldo += 3
            else:
                print("""
No tienes premio
                """)

    elif opcion == 2:
        aniadirSaldo = validar_numero_positivo("¿Cuántas monedas quieres añadir? ")
        saldo += aniadirSaldo
    elif opcion == 3:
        print(f"Saldo actual: {saldo} monedas")
    elif opcion <1 or opcion > 4:
        print("Debe introducir una opcion del menu (1 a 4)")

    opcion = menu_opciones()

if opcion == 4:
    print("Selecciono salir del programa")