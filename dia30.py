import random

parque = {
    "dinero": 100,
    "visitantes": 20,
    "satisfaccion": 70,
    "dia": 1
}

atracciones = [
    {"nombre": "Montaña rusa", "precio": 40, "ingresos": 20},
    {"nombre": "Casa del terror", "precio": 25, "ingresos": 12},
    {"nombre": "Noria", "precio": 30, "ingresos": 15}
]

atraccionesConstruidas = []

dinero = 100
visitantes = 20
satisfaccion = 70
dia = 1

def menu_opciones(dia, dinero, visitantes, satisfaccion):
    print(f"""
----- DÍA {dia} -----

Dinero: {dinero}€
Visitantes: {visitantes}
Satisfacción: {satisfaccion}

1. Construir atracción
2. Mejorar satisfacción
3. Hacer publicidad
4. Pasar al siguiente día

"""

    )

    opcion = int(input("Introduce una opcion: "))
    return opcion

while dia < 7 and satisfaccion > 0:
    opcion = menu_opciones(dia, dinero, visitantes, satisfaccion)
    if opcion == 1:
        for i in range(0, len(atracciones)):
            print(f"{i+1}. {atracciones[i]["nombre"]}")

        atraccion = int(input("Seleccione la atraccion que desea construir: "))        
        seleccionada = atracciones[atraccion - 1]

        if dinero >= seleccionada["precio"]:
            dinero -= seleccionada["precio"]
            atraccionesConstruidas.append(seleccionada)
            print(f"Has construido {seleccionada["nombre"]}")
        else:
            print("No tienes dinero suficiente")
        
    elif opcion == 2:
        print("2. Mejorar satisfacción")
        if dinero >= 30:
            dinero -= 30
            satisfaccion += 20
            if satisfaccion > 100:
                satisfaccion = 100
            print("¡Satisfacción aumentada!")
        else:
            print("No tienes dinero suficiente.")

    elif opcion == 3:
        print("3. Hacer publicidad")
        if dinero >= 20:
            dinero -= 20
            visitantes += 10
            print("Has pagado publicidad")
        else:
            print("No tienes dinero suficiente.")
        
    elif opcion == 4:
        print("4. Pasar al siguiente día")

        ingresosTotales = 0
        for atraccion in atraccionesConstruidas:
            ingresosTotales += atraccion["ingresos"]
        
        ingresosTotales += visitantes
        dinero += ingresosTotales

        print(f"Ingresos del día {dia}: +{ingresosTotales}€")

        eventoAleatorio = random.randint(1, 4)
        if eventoAleatorio == 1:
            print("Lluvia → visitantes -5")
            visitantes -= 5
            if visitantes < 0:
                visitantes = 0
        elif eventoAleatorio == 2:
            print("Influencer recomienda el parque → visitantes +15")
            visitantes += 15
        elif eventoAleatorio == 3:
            print("Avería en una atracción → satisfacción -15")
            satisfaccion -= 15
        elif eventoAleatorio == 4:
            print("Día tranquilo → sin cambios")

        satisfaccion -= 5
        dia += 1

    else:
        print("Debe introducir una opcion del menu (1 a 4)")
        opcion = menu_opciones(dia)

if satisfaccion > 0:
    print("Fin de la semana.")
    print(f"Dinero final: {dinero}€")