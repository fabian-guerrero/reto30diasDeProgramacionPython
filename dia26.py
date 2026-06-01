personajes = []
indice = 0
personajeEncontrado = False

def menu_opciones():
    print("""
----- CREADOR DE PERSONAJES -----

1. Crear personaje
2. Ver personajes
3. Buscar personaje
4. Salir

""")

    opcion = int(input("Introduce una opcion: "))
    return opcion

opcion = menu_opciones()

while opcion != 4:
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
        personajeEncontrado = False
        personajeBuscado = input("Introduce el personaje que quieres buscar: ")
        for i in range(0, len(personajes)):
            if personajes[i].get("nombre") == personajeBuscado:
                personajeEncontrado = True
                for clave, valor in personajes[i].items():
                    print(f"{clave}: {valor}")

        if personajeEncontrado == False:
            print("Personaje no encontrado.")
    else:
        print("Has seleccionado una opcion no valida")

    opcion = menu_opciones()

print("Has salido del programa")