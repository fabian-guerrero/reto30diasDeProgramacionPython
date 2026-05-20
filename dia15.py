import random

jugadores = int(input("¿Cuántos jugadores participan? "))
listaJugadores = []
totalPartidos = 0

for i in range(jugadores):
    listaJugadores.append(i+1)

for i in range(1, jugadores + 1):
    for j in range(i+1, jugadores + 1):
        puntos1 = random.randint(0,5)
        puntos2 = random.randint(0,5)
        print(f"Jugador {i} vs Jugador {j}")
        print(f"Jugador {i} {puntos1} - Jugador {j} {puntos2}")
        print("")
        totalPartidos += 1

print(f"Total de partidos jugados: {totalPartidos}")