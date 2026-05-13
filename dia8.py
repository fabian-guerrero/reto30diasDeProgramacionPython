import random

tiempoCoche1 = 0
vueltasRapidasCoche1 = 0
tiempoCoche2 = 0
vueltasRapidasCoche2 = 0
tiempoCoche1
cocheMasRapido = ""
ganador = ""
vueltaMasRapidaGeneral = 40
recordVuelta = []
numeroDeVueltas = 5


coche1 = input("Ingrese el nombre del coche 1: ")
coche2 = input("Ingrese el nombre del coche 2: ")

for i in range(1,numeroDeVueltas+1,1):
    vueltaCoche1 = random.randint(20,40)
    vueltaCoche2 = random.randint(20,40)

    tiempoCoche1 += vueltaCoche1
    tiempoCoche2 += vueltaCoche2

    if(tiempoCoche1 == tiempoCoche2):
        cocheMasRapido = "Empate"
    elif vueltaCoche1 < vueltaCoche2:
        cocheMasRapido = coche1
        vueltasRapidasCoche1 +=1
        if vueltaCoche1 < vueltaMasRapidaGeneral:
            vueltaMasRapidaGeneral = vueltaCoche1
            recordVuelta = [vueltaCoche1,coche1]
    else:
        cocheMasRapido = coche2
        vueltasRapidasCoche2 +=1
        if vueltaCoche2 < vueltaMasRapidaGeneral:
            vueltaMasRapidaGeneral = vueltaCoche2
            recordVuelta = [vueltaCoche2,coche2]

    print(
    f"""----- VUELTA {i} -----

    {coche1} → {vueltaCoche1} segundos
    {coche2} → {vueltaCoche2} segundos

    {"HAN EMPATADO EL TIEMPO DE VUELTA" if cocheMasRapido == "Empate" else f"{cocheMasRapido} ha sido más rápido en esta vuelta."}
    """)

if (tiempoCoche1 == tiempoCoche2):
    ganador = "Empate"
elif (tiempoCoche1 < tiempoCoche2):
    ganador = coche1
else:
    ganador = coche2

print(
f"""----- RESULTADO FINAL -----

Tiempo total {coche1}: {tiempoCoche1} segundos
Tiempo total {coche2}: {tiempoCoche2} segundos

{"LA CARRERA TERMINO EN EMPATE" if ganador == "Empate" else f"GANADOR: {ganador}"}

{coche1} gano {vueltasRapidasCoche1} vueltas.
{coche2} gano {vueltasRapidasCoche2} vueltas.

Vuelta más rápida: {recordVuelta[0]} segundos {recordVuelta[1]}
""")