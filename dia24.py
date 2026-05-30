mapas = {
    "Nuketown": 0,
    "Raid": 0,
    "Hijacked": 0,
    "Standoff": 0
}

print("""Mapas disponibles:
- Nuketown
- Raid
- Hijacked
- Standoff

""")

cantidadJugadores = int(input("¿Cuántos jugadores van a votar?: "))
masVotado = 0
claveMasVotado = str

for i in range(1, cantidadJugadores + 1):
    mapaSeleccionado = input(f"Jugador {i}, elige mapa: ")
    while mapaSeleccionado not in mapas:
        mapaSeleccionado = input(f"Jugador {i}, debe seleccionar un mapa de la lista: ")
    mapas[mapaSeleccionado] += 1

for mapa, votos in mapas.items():
    if votos > masVotado:
        masVotado = votos
        claveMasVotado = mapa

print(f"""
----- RESULTADOS -----

Nuketown → {mapas["Nuketown"]} votos
Raid → {mapas["Raid"]} votos
Hijacked → {mapas["Hijacked"]} votos
Standoff → {mapas["Standoff"]} votos

Mapa elegido: {claveMasVotado}
""")