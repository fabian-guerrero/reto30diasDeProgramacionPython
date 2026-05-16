def validar_numero_positivo(mensaje):
    numero = int(input(mensaje))
    while numero <= 0:
        print("Debe introducir un numero positivo")
        numero = int(input(mensaje))
    return numero

def dibujar_rectangulo(filas, columnas, caracter):
    print("")
    for i in range(filas):
        for j in range(columnas):
            print(f"{caracter}", end="")
        print("")

def dibujar_triangulo(altura, caracter):
    print("")
    for i in range(altura):
        for j in range(i+1):
            print(f"{caracter}", end="")
        print("")

def dibujar_triangulo_invertido(altura, caracter):
    print("")
    for i in range(altura):
        for j in range(altura-i, 0, -1):
            print(f"{caracter}", end="")
        print("")

def menu_opciones():
    print("""
----- GENERADOR DE PATRONES -----

1. Rectángulo
2. Triángulo normal
3. Triángulo invertido
4. Salir

"""

    )

    opcion = int(input("Introduce una opcion: "))
    return opcion

opcion = menu_opciones()

while opcion != 4:
    caracter = input("¿Qué carácter quieres utilizar?")

    if opcion == 1:
        filas = validar_numero_positivo("Introduce el número de filas: ")
        columnas = validar_numero_positivo("Introduce el número de columnas: ")
        dibujar_rectangulo(filas, columnas, caracter)
    elif opcion == 2:
        altura = validar_numero_positivo("Introduce la altura: ")
        dibujar_triangulo(altura, caracter)
    elif opcion == 3:
        altura = validar_numero_positivo("Introduce la altura: ")
        dibujar_triangulo_invertido(altura, caracter)
    elif opcion <1 or opcion > 4:
        print("Debe introducir una opcion del menu (1 a 4)")

    opcion = menu_opciones()

if opcion == 4:
    print("Selecciono salir del programa")
