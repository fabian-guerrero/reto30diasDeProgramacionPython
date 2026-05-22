import random

def validar_coordenada(mensaje):
    numero = int(input(mensaje))
    while numero < 1 or numero > 6:
        print("Debe introducir un numero dentro del rango")
        numero = int(input(mensaje))
    return numero

def posicionBarco(filaInicial, columnaInicial, orientacionBarco):
    # orientacionBarco == 1 -> orientacion Horizontal
    # orientacionBarco == 2 -> orientacion Vertical

    if orientacionBarco == 1:
        if columnaInicial - 2 > 0 and columnaInicial + 2 < 7:
            coordenadasBarco = [[filaInicial,columnaInicial], [filaInicial,columnaInicial+1], [filaInicial,columnaInicial+2]]
            return coordenadasBarco
        elif columnaInicial - 2 > 0 :
            coordenadasBarco = [[filaInicial,columnaInicial], [filaInicial,columnaInicial-1], [filaInicial,columnaInicial-2]]
            return coordenadasBarco
        elif columnaInicial + 2 < 7:
            coordenadasBarco = [[filaInicial,columnaInicial], [filaInicial,columnaInicial+1], [filaInicial,columnaInicial+2]]
            return coordenadasBarco

    elif orientacionBarco == 2:
        if (filaInicial - 2) > 0 and filaInicial + 2 < 7:
            coordenadasBarco = [[filaInicial,columnaInicial], [filaInicial+1,columnaInicial], [filaInicial+2,columnaInicial]]
            return coordenadasBarco
        elif filaInicial - 2 > 0:
            coordenadasBarco = [[filaInicial,columnaInicial], [filaInicial-1,columnaInicial], [filaInicial-2,columnaInicial]]
            return coordenadasBarco
        elif filaInicial + 2 < 7:
            coordenadasBarco = [[filaInicial,columnaInicial], [filaInicial+1,columnaInicial], [filaInicial+2,columnaInicial]]
            return coordenadasBarco


filas = 6
columnas = 6

posicionInicialBarco = [random.randint(1,6), random.randint(1,6)]
orientacionBarco = random.randint(1,2)

coordenadasBarco = posicionBarco(posicionInicialBarco[0],posicionInicialBarco[1],orientacionBarco)

disparosAgua = []
tocado = []
disparo = 0

aciertos = 0

while aciertos != 3:
    cordenadaFila = validar_coordenada("Ingrese coordenada de fila: ")
    cordenadaColumna = validar_coordenada("Ingrese coordenada de columna: ")
    disparo = [cordenadaFila, cordenadaColumna]

    if disparo in disparosAgua or disparo in tocado:
        print("Ya habías disparado ahí. Prueba otra coordenada.")
    elif disparo in coordenadasBarco:
        tocado.append(disparo)
        aciertos+=1
        print("¡Tocado!")
    else:
        disparosAgua.append(disparo)
        print("Agua")

    for i in range(1, filas + 1):
        for j in range(1, columnas + 1):
            if [i,j] in tocado:
                print(f" X ", end="")
            elif [i,j] in disparosAgua:
                print(" O ", end="")
            else:
                print(" ~ ", end="")
        print("")

print("¡Tocado y hundido!")
print("Has undido el barco")
print(f"Intentos realizados: {len(tocado)+len(disparosAgua)}")