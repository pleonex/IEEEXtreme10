#!/bin/python
# -*- coding: utf-8 -*-


def convertir(base, letras, value):
    salida = 0


    value = value.replace(" ","")
    value = value.replace("+","")

    i = len(value)-1

    for dig in value:
        if not dig=='' and not dig=='+' and not dig==' ':
            salida+=letras.index(dig)*base**i
            i-=1
    return salida


def int2base(x, base,digs):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)


def main():

    lenCadenas = 0
    base, letras = raw_input().split(" ")

    print(base+" "+letras)

    sumando1 = raw_input()
    lenCadenas = len(sumando1)
    print(sumando1)

    sumando2 = raw_input()
    print(sumando2)
    print(raw_input())

    result = raw_input()

    base = int(base)

    sumando1 = convertir(base,letras,sumando1)
    sumando2 = convertir(base,letras,sumando2)

    resultado = sumando1+sumando2

    final = int2base(resultado, base, letras)
    espacios = lenCadenas-len(final)

    final = ' '*espacios+final

    print(final)

if __name__ == '__main__':
    main()
