personajes = [
    { "nombre": "Aria", "vida": 100, "ataque": 25, "defensa": 10,"monedas": 50},
    { "nombre": "Thorin", "vida": 120, "ataque": 20, "defensa": 15,"monedas": 50},
    { "nombre": "Luna", "vida": 15, "ataque": 5, "defensa": 2,"monedas": 5 }
]

tienda = [
    {"nombre": "Espada de hierro", "precio": 30, "ataque": 10, "defensa": 0, "vida": 0},
    {"nombre": "Escudo de madera", "precio": 25, "ataque": 0, "defensa": 8, "vida": 0},
    {"nombre": "Poción vital", "precio": 20, "ataque": 0, "defensa": 0, "vida": 20},
    {"nombre": "Armadura ligera", "precio": 40, "ataque": 0, "defensa": 12, "vida": 10}
]

personajeEncontrado = False
objetoEncontrado = False
comprador = ""
objeto = 0

def menu_opciones():
    print("""
----- TIENDA DE EQUIPAMIENTO -----

1. Crear personaje
2. Ver personajes
3. Ver tienda
4. Comprar objeto
5. Salir

""")

    opcion = int(input("Introduce una opcion: "))
    return opcion

def personaje_existe(personaje):
    personajeEncontrado = False
    for i in range(0, len(personajes)):
        if personajes[i].get("nombre") == personaje:
            personajeEncontrado = True

    while personajeEncontrado == False:
        print("Ingrese un personaje que exista")
        personaje = input("Nombre del personaje: ")
        for i in range(0, len(personajes)):
            if personajes[i].get("nombre") == personaje:
                personajeEncontrado = True

    return personaje

def objeto_existe(objeto):
    objetoEncontrado = False
    while objeto == 0:
        objeto=int(input("Debe ingresar un numero mayor a cero: "))

    for i in range(0, len(tienda)):
        if i == objeto - 1:
            objetoEncontrado = True
            objeto = objeto -1

    while objetoEncontrado == False:
        print("Ingrese un objeto que exista")
        objeto = int(input("Número del objeto: "))
        for i in range(0, len(tienda)):
            if i == objeto - 1:
                objetoEncontrado = True
                objeto = objeto -1
    return objeto

def actualizar_comprador(comprador, objeto):

    for i in range(0, len(personajes)):
        if personajes[i].get("nombre") == comprador:
            vida = personajes[i]["vida"]
            ataque = personajes[i]["ataque"]
            defensa = personajes[i]["defensa"]
            monedas = personajes[i]["monedas"]
            personajes[i]["vida"] = vida + tienda[objeto]["vida"]
            personajes[i]["ataque"] = ataque + tienda[objeto]["ataque"]
            personajes[i]["defensa"] = defensa + tienda[objeto]["defensa"]
            personajes[i]["monedas"] = monedas - tienda[objeto]["precio"]
            if not (vida == personajes[i]["vida"]):
                print(f"Vida {vida} → {personajes[i]["vida"]}")
            if not (ataque == personajes[i]["ataque"]):
                print(f"Ataque {ataque} → {personajes[i]["ataque"]}")
            if not (defensa == personajes[i]["defensa"]):
                print(f"Defensa {defensa} → {personajes[i]["defensa"]}")
            print(f"Monedas {monedas} → {personajes[i]["monedas"]}")

    print(f"{comprador} ha comprado {tienda[objeto]['nombre']}")

opcion = menu_opciones()


while opcion != 5:
    if opcion == 1:
        nombre = input("Introduce el nombre del personaje: ")
        vida = int(input("Introduce el nivel de vida: "))
        ataque = int(input("Introduce el nivel de ataque: "))
        defensa = int(input("Introduce el nivel de defensa: "))
        monedas = 50

        personaje = { "nombre": nombre, "vida": vida, "ataque": ataque, "defensa": defensa, "monedas": monedas}
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
        if len(tienda) == 0:
            print("No hay objetos en la tienda")
        else:
            indice = 0
            print("")
            for objeto in tienda:
                indice += 1
                print(f"{indice}. ", end="")
                for clave, valor in objeto.items():
                    if clave == "nombre":
                        print(f"{valor}")
                    elif clave == "precio":
                        print(f"{clave}: {valor}")
                    else:
                        print(f"{clave}: +{valor}")
                print("")

    elif opcion == 4:
        comprador = ""
        objeto = -1

        comprador = personaje_existe(input("Nombre del personaje: "))
        objeto = objeto_existe(int(input("Número del objeto: ")))

        for i in range(0, len(personajes)):
            if personajes[i].get("nombre") == comprador:
                if personajes[i]["monedas"] < tienda[objeto]["precio"]:
                    print("No tienes monedas suficientes.")
                else:
                    actualizar_comprador(comprador, objeto)

    opcion = menu_opciones()

print("Fin de la Tienda de equipamiento.")