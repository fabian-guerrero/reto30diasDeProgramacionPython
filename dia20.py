cantidadCanciones = int(input("¿Cuántas canciones quieres añadir?: "))
listaCanciones = []
busquedaPosicion = 0
cancionBuscada = ""
cancionEncontrada = False

for i in range(cantidadCanciones):
    cancion = input(f"Ingrese el nombre de la cancion {i+1}: ")
    listaCanciones.append(cancion)

print("")

print("----- PLAYLIST -----")
for cancion in range(len(listaCanciones)):
    print(f"{cancion+1}: {listaCanciones[cancion]}")
print("")

busquedaPosicion = int(input("¿Qué posición quieres consultar?: "))
while busquedaPosicion > len(listaCanciones) or busquedaPosicion < 1:
    print("Debe ingresar una posicion valida")
    print("")
    busquedaPosicion = int(input("¿Qué posición quieres consultar?: "))

print(f"La canción en la posición {busquedaPosicion} es: {listaCanciones[busquedaPosicion-1]}")
print("")

cancionBuscada = input("¿Qué canción quieres buscar?: ")

for i in range(len(listaCanciones)):
    if cancionBuscada.lower() == listaCanciones[i].lower():
        print(f"""
La canción existe en la playlist.
Posición: {i+1}
""")
        cancionEncontrada = True
        break
    else:
        cancionEncontrada = False

if cancionEncontrada == False:
    print("Canción no encontrada.")