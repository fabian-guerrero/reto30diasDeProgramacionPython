nombre = input("Introduce tu nombre: ")
anioNacimiento = int(input("Introduce tu año de nacimiento: "))
ciudad = input("Introduce tu ciudad: ")

anioActual = 2026
edadAproximada = anioActual - anioNacimiento
esAdulto = edadAproximada >= 30

print("\n----- FICHA DE USUARIO -----")
print(f"Nombre: {nombre.capitalize()}")
print(f"Ciudad: {ciudad}")
print(f"Edad aproximada: {edadAproximada} años")
print("---------------------------\n")

if esAdulto:
    print("Eres adulto")
else:
    print("Eres joven")