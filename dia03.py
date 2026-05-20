nombre = input("Ingrese el nombre del alumno: ")
nota = float(input("Ingrese la nota del alumno: "))
resultado = ""
mensaje = ""

if (nota >=0 and nota<5):
    resultado = "Suspenso"
elif (nota >=5 and nota<7):
    resultado = "Aprobado"
elif (nota >=7 and nota<9):
    resultado = "Notable"
elif (nota >=9 and nota<=10):
    resultado = "Excelente"
else:
    resultado = "Nota no válida"

if resultado == "Suspenso":
    mensaje = "Hay que seguir trabajando"
elif resultado == "Nota no válida":
    mensaje = "Debe ingresar una nota entre 0 y 10"
else:
    mensaje = "Buen trabajo"


if nota <0 or nota >10:
    print(f"{resultado}")
    print(f"{mensaje}")
else:
    print(f"""
    Alumno: {nombre}
    Nota: {nota}
    Resultado: {resultado}

    {mensaje}
    """)