def invertir_frase(frase):
    fraseInvertida = ""
    frase.reverse()
    for caracter in frase:
        fraseInvertida += caracter

    return fraseInvertida

def verificar_palindromo(frase):
    fraseSinEspaciosLista = []
    fraseSinEspaciosListaInvertida = []
    fraseEnLowercase = frase.lower()
    fraseEnLista = list(fraseEnLowercase)
    for caracter in fraseEnLista:
        if caracter != " ":
            fraseSinEspaciosLista.append(caracter)

    fraseSinEspaciosListaInvertida = fraseSinEspaciosLista.copy()
    fraseSinEspaciosListaInvertida.reverse()

    if fraseSinEspaciosLista == fraseSinEspaciosListaInvertida:
        return True


caracteres = 0
espacios = 0
vocales = 0
consonantes = 0
mayusculas = 0
minusculas = 0
aVeces = 0
eVeces = 0
iVeces = 0
oVeces = 0
uVeces = 0
palindromo = False

fraseString = input("Introduce una frase: ")
fraseList = list(fraseString)

for caracter in fraseList:
    if caracter == " ":
        espacios += 1
    elif caracter in "aeiou":
        vocales += 1
        minusculas += 1
    elif caracter in "AEIOU":
        vocales += 1
        mayusculas += 1
    elif caracter in "bcdfghjklmnñpqrstvwxyz":
        consonantes += 1
        minusculas += 1
    elif caracter in "BCDFGHHJKLMNÑOPQRSTVWXYZ":
        consonantes += 1
        mayusculas += 1

print(f"""
    Caracteres: {len(fraseList)}
    Espacios: {espacios}
    Vocales: {vocales}
    consonanetes: {consonantes}

    Mayusculas: {mayusculas} caracteres son mayusculas
    Minusculas: {minusculas} caracteres son minusculas
""")

if verificar_palindromo(fraseString):
    print("La frase es un palindromo")

print(f"La frase invertida es: {invertir_frase(fraseList)}")