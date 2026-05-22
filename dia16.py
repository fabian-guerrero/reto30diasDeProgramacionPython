import random

filaTesoro = random.randint(1,8)
columnaTesoro = random.randint(1,8)
coordenadaFila = 0
coordenadaColumna = 0
intentos = 0


print(f"Fila tesoro: {filaTesoro}, Columna tesoro: {columnaTesoro}")

for i in range(1, 9):
    for j in range(1, 9):
        print(" * ", end="")
    print("")

print("")



while (filaTesoro != coordenadaFila) or (columnaTesoro != coordenadaColumna):
    intentos +=1
    coordenadaFila = int(input("Ingrese la fila: "))
    coordenadaColumna = int(input("Ingrese la columna: "))

    if filaTesoro == coordenadaFila and columnaTesoro == coordenadaColumna:
        print("¡Has encontrado el tesoro!")
        print(f"Intentos realizados: {intentos}")
    else:
        print("No has encontrado el tesoro.")
        if coordenadaFila > filaTesoro:
            print(f"El tesoro está más arriba.")
        elif coordenadaFila < filaTesoro:
            print(f"El tesoro está más abajo.")

        if coordenadaColumna > columnaTesoro:
            print(f"El tesoro está más a la izquierda.")
        elif coordenadaColumna < columnaTesoro:
            print(f"El tesoro está más a la derecha")
    
    print("")

for i in range(1, 9):
    for j in range(1, 9):
        if i == filaTesoro and j == columnaTesoro:
            print(" X ", end="")
        else:
            print(" * ", end="")
    print("")

