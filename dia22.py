import random

filas = 3
columnas = 5
carton = []
numerosCarton = []
posicionNumero = 0
bingo=False
linea=False
linea1=0
linea2=0
linea3=0
extraidas = []
aciertos = 0

def ver_carton():
    print("----- CARTÓN -----")
    for i in range(0,filas):
        for j in range(0,columnas):
            print(f" {carton[i][j]}  ", end="")
        print("")

while len(numerosCarton) < 15:
    numeroCarton = random.randint(1,30)
    if numeroCarton not in numerosCarton:
        numerosCarton.append(numeroCarton)

for i in range(0,3):
    fila = []
    for j in range(0,5):
        fila.append(numerosCarton[posicionNumero])
        posicionNumero +=1
    carton.append(fila)

ver_carton()

while bingo == False:
    bolaExtraida = random.randint(1,30)

    while bolaExtraida in extraidas:
        bolaExtraida = random.randint(1,30)

    print("")
    print(f"Bola extraída: {bolaExtraida}")
    extraidas.append(bolaExtraida)

    if bolaExtraida in numerosCarton:
        print("¡Acierto!")
        print("")

    for i in range(filas):
        for j in range(columnas):
            if bolaExtraida == carton[i][j]:
                print(" X ", end="")
                carton[i][j]= " X "
                aciertos+=1
                if i == 0:
                    linea1+= 1
                elif i == 1:
                    linea2 += 1
                elif i == 2:
                    linea3 +=1
            else:
                print(f" {carton[i][j]}  ", end="")
        print("")

    if (linea1 == 5 or linea2 == 5 or linea3 == 5) and linea == False:
        print("¡LÍNEA!")
        linea=True

    if aciertos == 15:
        bingo = True
        print("¡BINGO!")

    input("Pulsa Enter para sacar una bola...")