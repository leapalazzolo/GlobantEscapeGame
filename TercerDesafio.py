import os
import time
import threading
from multiprocessing import Pool
from operator import itemgetter

def buscar_siguiente_numero_valido(numero, maximo):
    numero += 1
    while sin_numeros_repetidos(numero) is False and numero <= maximo:
        #numero += 1
        numero = aumentar_numero(numero)

    if numero <= maximo:
        return numero
    return None

def sin_numeros_repetidos(numero):
    caracteres = '0123456789'
    cadena = str(numero)
    for c in caracteres:
        if cadena.count(c) > 1:
            return False
    return True

def posicion_substring(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

def aumentar_numero(numero):
    caracteres = '0123456789'
    cadena_original = str(numero)
    cadena = str(numero)
    for c in caracteres:
        if c*2 in cadena[-2:]:
            return numero + 1
        if '99' in c*2:
            i = cadena.find('99') - 1#posicion_substring(cadena, c*2)
            if i > 0:
                cadena = cadena[:i] + str(int(cadena[i]) + 1) + '01' + cadena[i + 3:]
                #lista_de_chars[i] = int(cadena[i]) + 1
                #cadena = cadena2 #"".join(lista_de_chars)
                #cadena.replace('99','01')
        else:
            reemplazo = c + str(int(c) + 1)[-1:]
            cadena = cadena.replace(c*2, reemplazo)
    if cadena in cadena_original:
        return numero + 1
    #print("Se avanzo desde {} hasta {}".format(numero, int(cadena)))
    return int(cadena)

def calcular_conjuntos(limite_inferior, limite_superior)
    numeros = list()
    primer_numero_valido = limite_inferior
    siguiente_numero_valido = buscar_siguiente_numero_valido(primer_numero_valido, limite_superior)
    while siguiente_numero_valido is not None:
        diferencia = siguiente_numero_valido - primer_numero_valido
        conjunto = (primer_numero_valido, siguiente_numero_valido, diferencia)
        print(conjunto)
        numeros.append(conjunto)
        primer_numero_valido = siguiente_numero_valido
        siguiente_numero_valido = buscar_siguiente_numero_valido(primer_numero_valido, limite_superior)
    return numeros
    # print(sorted(numeros,key=itemgetter(1)))

def main():
    num_threads = sys.argv[1]
    limite_inferior_original = 123456789
    limite_superior_original = 987654321
    incremento = (limite_superior - limite_inferior) / num_threads
    lista_limites = []
    limite_inferior = limite_inferior_original
    for i in range(num_threads - 1):
        limite_superior = limite_inferior + int(incremento)
        lista_limites.append(tuple(limite_inferior, limite_superior))
        #limite_inferior[i] = limite_inferior
        limite_inferior = limite_superior
    #limite_superior[-1] = limite_superior   #Porque se perdio precision al redondear el incremento
    lista_limites.append(tuple(limite_inferior, limite_superior_original))
    resultado = []
    with Pool(num_threads) as pool:
        for i in range(num_threads):
            resultado.append(pool.starmap(calcular_conjuntos, product(names, repeat=2)))
        print(results)    

if __name__ == "__main__":
    main()  
