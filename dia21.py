import random

def menu_opciones():
    print(f"""
----- MOCHILA DEL AVENTURERO -----

1. Encontrar objeto
2. Usar objeto
3. Ver mochila
4. Buscar objeto
5. Salir

"""
    )

    opcion = int(input("Introduce una opcion: "))
    return opcion

listaObjetos =["poción","espada","escudo","llave","moneda","mapa","antorcha" ]
mochila =[]
opcion = 1

while opcion != 5:
    opcion = menu_opciones()
    if opcion == 1:
        encontrado = random.randint(0,len(listaObjetos)-1)
        encontrado = listaObjetos[encontrado]
        if(len(mochila) < 5):
            mochila.append(encontrado)
            print(f"Has encontrado: {encontrado}")
            print("Objeto añadido a la mochila.")
        else:
            print(f"Has encontrado: {encontrado}")
            print("La mochila está llena. No puedes guardarlo.")
    elif opcion == 2:
        usarObjeto = input("¿Que objeto quieres usar? ")
        for i in range(len(listaObjetos)):
            if usarObjeto == listaObjetos[i]:
                encontrado = True
                mochila.remove(listaObjetos[i])
                break
            else:
                encontrado = False

        print(f"Has usado: {usarObjeto}") if encontrado else print("No tienes ese objeto en la mochila.")
    elif opcion == 3:
        if len(mochila) == 0:
            print("La mochila está vacía.")
        else:
            print("----- MOCHILA -----")
            for objeto in range(len(mochila)):
                print(f"{objeto+1}. {mochila[objeto]}")
    elif opcion == 4:
        buscarObjeto = input("¿Que objeto quieres buscar? ")
        for i in range(len(listaObjetos)):
            if buscarObjeto == listaObjetos[i]:
                encontrado = True
                break
            else:
                encontrado = False

        print("Sí tienes ese objeto.") if encontrado else print("No tienes ese objeto.")
    else:
        print("Has seleccionado una opcion no valida")

print("Fin de la aventura.")