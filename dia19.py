cantidadPilotos = int(input("¿Cuántos pilotos participan?: "))
puntosPilotos = []
sumaPuntos = 0

for i in range(cantidadPilotos):
    puntos = int(input(f"¿Cuántos puntos obtuvo el piloto {i+1}?: "))
    puntosPilotos.append(puntos)

print("")

for i in range(len(puntosPilotos)):
    print(f"Puntos del piloto {i+1}: {puntosPilotos[i]}")
    sumaPuntos+= puntosPilotos[i]

print("")

print(f"Puntuación máxima: {max(puntosPilotos)}")
print(f"Puntuación minima: {min(puntosPilotos)}")
print(f"Media de puntos: {sumaPuntos/len(puntosPilotos)}")