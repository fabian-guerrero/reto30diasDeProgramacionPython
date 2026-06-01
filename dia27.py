personajes = [{ "nombre": "Aria", "vida": 100, "ataque": 25, "defensa": 10},{ "nombre": "Thorin", "vida": 120, "ataque": 20, "defensa": 15},{ "nombre": "Luna", "vida": 15, "ataque": 5, "defensa": 2 }]
personajeEncontrado = False

def menu_opciones():
    print("""
----- CREADOR DE PERSONAJES -----

1. Crear personaje
2. Ver personajes
3. Combatir
4. Ver clasificación
5. Salir

""")

    opcion = int(input("Introduce una opcion: "))
    return opcion

def personaje_existe(personaje):
    personajeEncontrado = False
    for i in range(0, len(personajes)):
        if personajes[i].get("nombre") == personaje:
            personajeEncontrado = True

    return personajeEncontrado

def valores_personaje(personaje, rol):
    for i in range(0, len(personajes)):
        if personajes[i].get("nombre") == personaje:
            if rol == "atacante":
                valorPersonaje = personajes[i].get("ataque")
            elif rol == "defensor":
                valorPersonaje = personajes[i].get("defensa")

    print(valorPersonaje)

    return valorPersonaje

def nivel_vida(personaje):
    for i in range(0, len(personajes)):
        if personajes[i].get("nombre") == personaje:
            nivelPersonaje = personajes[i].get("vida")

    return nivelPersonaje

def actualizar_vida(personaje, vidaActual):
    for i in range(0, len(personajes)):
        if personajes[i].get("nombre") == personaje:
            personajes[i]["vida"] = vidaActual

def personaje_mas_vida(personajes):
    masVida = personajes[0]
    for personaje in personajes:
        if personaje["vida"] > masVida["vida"]:
            masVida = personaje
    return masVida

def personaje_menos_vida(personajes):
    menosVida = personajes[0]
    for personaje in personajes:
        if personaje["vida"] < menosVida["vida"] and menosVida["vida"] > 0:
            menosVida = personaje
    return menosVida

opcion = menu_opciones()


while opcion != 5:
    if opcion == 1:
        nombre = input("Introduce el nombre del personaje: ")
        vida = int(input("Introduce el nivel de vida: "))
        ataque = int(input("Introduce el nivel de ataque: "))
        defensa = int(input("Introduce el nivel de defensa: "))

        personaje = { "nombre": nombre, "vida": vida, "ataque": ataque, "defensa": defensa}
        personajes.append(personaje)
        print("Personaje creado correctamente.")
    elif opcion == 2:
        if len(personajes) == 0:
            print("No hay personajes creados.")
        else:
            indice = 0
            print("")
            print("----- PERSONAJES -----")
            for personaje in personajes:
                indice += 1
                print(f"{indice}. ", end="")
                for clave, valor in personaje.items():
                    print(f"{clave}: {valor}")
                print("")
    elif opcion == 3:
        atacante = input("Ingrese el nombre del atacante: ")
        defensor = input("Ingrese el nombre del defensor: ")

        atacanteExiste = personaje_existe(atacante)
        defensorExiste = personaje_existe(defensor)

        if (atacante != defensor ):
            if (atacanteExiste and defensorExiste):
                valorAtaque = valores_personaje(atacante, "atacante")
                valorDefensa = valores_personaje(defensor, "defensor")

                if ((valorAtaque - valorDefensa) < 1):
                    danio = 1
                else:
                    danio = valorAtaque - valorDefensa

                print(f"{atacante} ataca a {defensor}")
                print(f"Daño realizado: {danio}")

                valorVida = nivel_vida(defensor)
                vidaActual = valorVida - danio

                actualizar_vida(defensor,vidaActual)

                if (vidaActual > 0):
                    print(f"""
{defensor}
Vida: {vidaActual}
""")
                else:
                    print(f"¡{defensor} ha sido derrotado!")

            else:
                print("Uno o ambos personajes no existen")
        else:
            print("Debe seleccionar personajes distintos")

    elif opcion == 4:
        cantidad = len(personajes)

        print("----- CLASIFICACIÓN -----")
        print(f"Personajes: {cantidad}")

        masVida = personaje_mas_vida(personajes)
        menosVida = personaje_menos_vida(personajes)

        print("Personaje con más vida:")
        print(f"{masVida['nombre']} ({masVida['vida']} PV)")

        print("Personaje con menos vida:")
        print(f"{menosVida['nombre']} ({menosVida['vida']} PV)")


    opcion = menu_opciones()

print("Fin de la Arena de Combate.")