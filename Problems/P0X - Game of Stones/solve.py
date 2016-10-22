#!/bin/python
# -*- coding: utf-8 -*-


def turno(pilas):
    for pila in pilas:
        if pila == 1:
            continue
        elif pila%3==0 and not pila%2==0:
            return [pila//3,pila//3,pila//3], pila
        else:
            only_ones = False
            pila1 = pila//3
            resto = pila-pila1

            if (resto/2)%2==0 and resto!=0:
                return [pila1,resto/2+1,resto/2-1],pila
            elif resto!=0 and resto>0:
                return [pila1,resto/2,resto/2],pila

    return None,None



def main():
    tests = int(raw_input())
    i = 0


    while i<tests:
        pilas = []

        games = int(raw_input())

        k = 0
        jugador = True

        while k<games:
            numpilas = int(raw_input())
            pilas +=  [int(x) for x in raw_input().split(' ')]
            k+=1

        perder = False

        while not perder:
            add,remove = turno(pilas)
            if add == None and remove == None:
                perder = True
            else:
                pilas+=add
                pilas.remove(remove)
            jugador = not jugador

        if jugador:
            print("Alice")
        else:
            print("Bob")

        i+=1




if __name__ == '__main__':
    main()
