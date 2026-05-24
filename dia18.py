frase = input("Introduce una frase: ")
caracterMarco = input("¿Qué carácter quieres utilizar para el marco?")

caracteresFrase = list(frase);
caracteresFrase.insert(0," ")
caracteresFrase.insert(0,caracterMarco)
caracteresFrase.append(" ")
caracteresFrase.append(caracterMarco)

longitudFrase = len(caracteresFrase)

for i in range(3):
    for j in range(longitudFrase):
        if i == 1:
            print(caracteresFrase[j], end="")
        else:
            print(caracterMarco, end="")

    print("")