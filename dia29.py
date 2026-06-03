pruebas = [
    {
        "nombre": "Puerta antigua",
        "pregunta": "¿Cuánto es 7 x 8?",
        "respuesta": "56",
        "puntos": 10,
        "resuelta": False
    },
    {
        "nombre": "Caja fuerte",
        "pregunta": "¿Qué lenguaje estamos aprendiendo?",
        "respuesta": "python",
        "puntos": 15,
        "resuelta": False
    },
    {
        "nombre": "Panel secreto",
        "pregunta": "¿Cuántos días tiene una semana?",
        "respuesta": "7",
        "puntos": 10,
        "resuelta": False
    }
]

def menu_opciones():
    print("""
----- ESCAPE ROOM DIGITAL -----

1. Ver pruebas
2. Resolver prueba
3. Ver puntuación
4. Ver progreso
5. Salir

""")

    opcion = int(input("Introduce una opcion: "))
    return opcion

opcion = menu_opciones()
indice = 0
puntuacion = 0
pruebasResueltas = 0
pruebasTotales = len(pruebas)

while opcion != 5:
    if opcion == 1:
        indice = 0
        for prueba in pruebas:
            for clave,valor in prueba.items():
                if clave == "nombre":
                    indice += 1
                    nombrePrueba = valor

                if clave == "resuelta":
                    estadoPrueba = valor

            print(f"{indice}. {nombrePrueba} → ",end="")
            print("Resuelta" if estadoPrueba else "Pendiente")
    elif opcion == 2:
        indice = 0
        for prueba in pruebas:
            for clave,valor in prueba.items():
                if clave == "nombre":
                    indice += 1
                    nombrePrueba = valor
                    print(f"{indice}. {nombrePrueba}")

        seleccion = int(input("Elige una prueba: "))

        if pruebas[seleccion-1]["resuelta"]:
            print("Esa prueba ya estaba resuelta.")
        else:
            respuesta = pruebas[seleccion-1]["respuesta"]
            pregunta = input(f"{pruebas[seleccion-1]["pregunta"]} ")
            if pregunta == respuesta:
                puntos = pruebas[seleccion - 1]["puntos"]
                puntuacion += puntos
                pruebas[seleccion - 1]["resuelta"] = True
                pruebasResueltas += 1
                print("Respuesta correcta.")
                print(f"Has ganado {puntos} puntos.")
            else:
                print("Respuesta incorrecta.")

    elif opcion == 3:
        print(f"Puntuación actual: {puntuacion} puntos")
    elif opcion == 4:
        if pruebasResueltas == pruebasTotales:
            print("¡Has escapado del escape room!")
        else:
            print(f"Pruebas resueltas: {pruebasResueltas}/{pruebasTotales}")
            print(f"Pruebas pendientes: {pruebasTotales - pruebasResueltas}")
    else:
        print("Has seleccionado una opcion no valida")

    opcion = menu_opciones()

print("Has abandonado el escape room.")