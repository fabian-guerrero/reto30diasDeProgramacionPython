contrasenia = "python2026"
intentos = 1

contraseniaIngresada = str(input("Introduce la contraseña: "))

while contrasenia != contraseniaIngresada:

    print("Contraseña Incorrecta")
    if intentos == 1:
        print("Intentalo de nuevo")
    elif intentos == 2:
        print("Ultimo intento")
    else:
        print("Acceso bloqueado")
        break
    
    intentos +=1
    contraseniaIngresada = str(input("Introduce la contraseña: "))

if contrasenia == contraseniaIngresada:
    print(f"""
    Acceso concedido.
    Bienvenido al sistema
    Has necesitado {intentos} {"intento" if intentos == 1 else "intentos"}
    """)