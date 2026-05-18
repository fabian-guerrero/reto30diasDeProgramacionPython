import random

oxigeno = 100
comida = 100
energia = 60
dia = 1

def menu_opciones(dia):
    print(f"""
----- DÍA {dia} -----

1. Buscar comida
2. Reparar sistema de oxígeno
3. Descansar

"""

    )

    opcion = int(input("Introduce una opcion: "))
    return opcion

while dia <= 7 and oxigeno > 0 and comida > 0 and energia > 0:
    opcion = menu_opciones(dia)
    if opcion >= 1 and opcion <= 3:
        if opcion == 1:
            comida += 20
            energia -= 15
            oxigeno -= 5

            print("Has encontrado suministros de comida.")
        elif opcion == 2:
            comida -= 5
            energia -= 20
            oxigeno += 10

            print("Has reparado parte del sistema de oxígeno.")
        elif opcion == 3:
            comida -= 10
            energia += 15
            oxigeno -= 5

            print("Has descansado y recuperado energía.")

        eventoAleatorio = random.randint(1,4)
        if eventoAleatorio == 1:
            oxigeno -= 15
            print("Ha habido una fuga de oxígeno.")
        elif eventoAleatorio == 2:
            energia += 10
            print("Los paneles solares han cargado energía.")
        elif eventoAleatorio == 3:
            comida += 15
            print("Has encontrado suministros extra.")
        elif eventoAleatorio == 4:
            print("No ha ocurrido ningún incidente.")

        comida -= 10
        energia -= 5
        oxigeno -= 10

        print(f"""
        Consumo diario aplicado.
        Valores actuales:
            comida: {comida}
            energia: {energia}
            oxigeno: {oxigeno}
        """)
        dia += 1
    else:
        print("Debe introducir una opcion del menu (1 a 3)")
        opcion = menu_opciones(dia)

if comida > 0 and energia > 0 and oxigeno > 0:
    print("¡Has sobrevivido hasta la llegada del rescate!")
else:
    print("No has sobrevivido. La nave se ha quedado sin recursos.")