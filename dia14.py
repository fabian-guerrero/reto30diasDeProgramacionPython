filas =  int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))
comienzo = int(input("Presione 1 para comenzar las coordenadas desde 1 o 2 para comenzar desde 0: "))

filaEspecial = int(input("Introduce la fila especial: "))
columnaEspecial = int(input("Introduce la columna especial: "))

for i in range(filas):
    for j in range(columnas):
        if comienzo == 1:
            if i+1 == filaEspecial and j+1 == columnaEspecial:
                print("   X   ",end="")
            else:
                print(f"({i + 1}, {j + 1}) ",end="")
        else:
            if i == filaEspecial and j == columnaEspecial:
                print("   X   ",end="")
            else:
                print(f"({i}, {j}) ",end="")

        if columnas == j + 1:
                print("")
