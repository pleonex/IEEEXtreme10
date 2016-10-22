#!/bin/python
# -*- coding: utf-8 -*-


def sumar(base, letras, a, b):
    if not a in letras:
        sumando1 = 0
    else:
        sumando1 = letras.index(a)

    if not b in letras:
        sumando2 = 0
    else:
        sumando2 = letras.index(b)

    resultado = sumando1+sumando2

    resultado_base = resultado%base
    llevada = resultado//base

    return letras[llevada], letras[resultado_base]



def main():

    lenCadenas = 0
    base, letras = raw_input().split(" ")

    print(base+" "+letras)

    sumando1 = raw_input()
    lenCadenas = len(sumando1)
    print(sumando1)
    sumando1.replace(" ","")

    sumando2 = raw_input()
    print(sumando2)
    sumando2.replace(" ","").replace("+","")
    print(raw_input())

    result = raw_input()

    base = int(base)

    i = len(sumando1)-1
    resultado = []
    llevada = letras[0]
    while i>0:
        llevada, resultado_suma = sumar(base,letras,sumando1[i],llevada)
        llevada, resultado_suma = sumar(base,letras,resultado_suma, llevada[0])
        llevada, resultado_suma = sumar(base,letras,resultado_suma,sumando2[i])

        resultado = [resultado_suma] + resultado

        i-=1

    salida_final = ''.join(str(e) for e in resultado)
    salida_final = int((lenCadenas-len(salida_final)))*' '+str(salida_final)
    print(salida_final)


if __name__ == '__main__':
    main()
