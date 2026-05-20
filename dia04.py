numero1=int(input("Introduce el primer número: "))
numero2=int(input("Introduce el segundo número: "))

mayor=0
menor = 0
iguales=False
num1Positivo=False
num2Positivo=False
num1Par=False
num2Par=False
num1esCero=False
num2esCero=False

suma = numero1 + numero2
diferecia = abs(numero1 - numero2)

if numero1 == numero2:
    iguales = True
elif numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1

if numero1 > 0:
    num1Positivo=True
elif numero1 < 0:
    num1Positivo=False
else:
    num1esCero=True

if numero2 > 0:
    num2Positivo=True
elif numero2 < 0:
    num2Positivo=False
else:
    num2esCero=True

if numero1 % 2 == 0:
    num1Par=True
else:
    num1Par=False

if numero2 % 2 == 0:
    num2Par=True
else:
    num2Par=False


if iguales:
    print(f"""
    ----- RESULTADOS -----

    Los numero son iguales

    Suma: {suma}
    Diferencia: La diferencia es cero

    Número 1 y 2:
    - {'El numero es 0, no es positivo ni negativo' if num1esCero else{'Positivo' if num1Positivo  else 'Negativo' }}
    - {'Par' if num1Par else 'Impar'}

    ----------------------
    """)

else:
    print(f"""
    ----- RESULTADOS -----

    Número mayor: {mayor}
    Número menor: {menor}

    Suma: {suma}
    Diferencia: {diferecia}

    Número 1:
    - {'El numero es 0, no es positivo ni negativo' if num1esCero else 'Positivo' if num1Positivo  else 'Negativo' }
    - {'Par' if num1Par else 'Impar'}

    Número 2:
    - {'El numero es 0, no es positivo ni negativo' if num2esCero else'Positivo' if num2Positivo  else 'Negativo' }
    - {'Par' if num2Par else 'Impar'}

    ----------------------
    """)