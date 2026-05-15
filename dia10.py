nota = float(input("Introduce una nota (-1 para terminar): "))
totalNotas = 0
notaMasAlta = nota
notaMasBaja = nota
acumuladorNotas = 0.00
media = 0.00
aprobados = 0
suspensos = 0
porcentjeAprobados = 0.00
clasificacionFinal = ""

while nota != -1:

    if nota >= 0 and nota <= 10:
        acumuladorNotas += nota
        totalNotas += 1
        media = acumuladorNotas / totalNotas

        if nota < 5:
            suspensos += 1
        else:
            aprobados += 1

        porcentjeAprobados = (aprobados * 100) / totalNotas

        if nota > notaMasAlta:
            notaMasAlta = nota
        elif nota < notaMasBaja:
            notaMasBaja = nota
    
    else:
        print("Introdujo una nota en un rango no valido. Las notas deben estar entre 0 y 10")

    nota = float(input("Introduce una nota (-1 para terminar): "))

if media >= 9:
    clasificacionFinal = "Grupo excelente"
elif media > 5:
    clasificacionFinal = "Grupo aceptable"
elif media > 0:
    clasificacionFinal = "Grupo mejorable"

print(f"""
----- RESULTADOS -----

Media: {round(media,2)}
Nota más alta: {notaMasAlta}
Nota más baja: {notaMasBaja}
Total de notas: {totalNotas}

Aprobados: {aprobados}
Suspensos: {suspensos}

Porcentaje de aprobados: {round(porcentjeAprobados,2)}%

{clasificacionFinal}
""")

