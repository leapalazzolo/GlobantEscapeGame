import sys
import threading
import csv
import multiprocessing
import time
import os
from multiprocessing.dummy import Pool
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

def obtener_conjuntos(limites):
    numeros = list()
    limite_superior = limites[1]
    #TODO no tomar el primero como valido
    primer_numero_valido = buscar_siguiente_numero_valido(limites[0], limite_superior)
    siguiente_numero_valido = buscar_siguiente_numero_valido(primer_numero_valido, limite_superior)
    while siguiente_numero_valido is not None:
        diferencia = siguiente_numero_valido - primer_numero_valido
        conjunto = [primer_numero_valido, siguiente_numero_valido, diferencia]
        #print("[{}]: {}".format(threading.current_thread().getName(), conjunto))
        numeros.append(conjunto)
        primer_numero_valido = siguiente_numero_valido
        siguiente_numero_valido = buscar_siguiente_numero_valido(primer_numero_valido, limite_superior)
    print("[{}]: Listo {}".format(threading.current_thread().getName(), limites))
    #print(numeros)
    #numeros.sort(key=itemgetter(2), reverse=True)
    return numeros

def obtener_primeros_de_conjuntos(limites):
    resultado = obtener_conjuntos(limites)
    resultado.sort(key=itemgetter(2), reverse=True)
    print("[{}]: Max. Diferencia: {}".format(threading.current_thread().getName(), resultado[0]))
    return resultado[0]


def obtener_primeros_de_conjuntos_en_paralelo(limites, threads):
    pool = Pool(threads)
    resultado = list()
    resultado += pool.map(obtener_primeros_de_conjuntos, limites)
    resultado.sort(key=itemgetter(2), reverse=True)
    pool.close()
    pool.join()
    return resultado

def obtener_maxima_diferencia(limites, threads):
    return obtener_primeros_de_conjuntos_en_paralelo(limites, threads)[0]

def main():
    inicio = time.clock()
    limite_inferior_original = int(sys.argv[1])
    limite_superior_original = int(sys.argv[2])
    num_threads = int(sys.argv[3])
    incremento = (limite_superior_original - limite_inferior_original) / num_threads
    lista_limites = []
    limite_inferior = limite_inferior_original
    for i in range(num_threads - 1):
        limite_superior = limite_inferior + int(incremento)
        lista_limites.append([limite_inferior, limite_superior])
        limite_inferior = limite_superior
    lista_limites.append([limite_inferior, limite_superior_original])
    resultado = obtener_maxima_diferencia(lista_limites, num_threads)
    print("--- Fin de ejecucion: %s segundos ---" % (time.clock() - inicio))
    print("La maxima diferencia fue de {}, entre {} y {}".format(resultado[2], resultado[0], resultado[1]))
    with open('resultado.csv', 'w') as archivo_resultado:
        writer = csv.writer(archivo_resultado, delimiter=';', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['Inicio', 'Fin', 'Diferencia'])
        writer.writerow(resultado)

if __name__ == "__main__":
    main()  
