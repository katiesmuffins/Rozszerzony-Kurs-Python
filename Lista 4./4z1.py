#!/usr/bin/env python3
# coding: utf8 

from math import sqrt
from functools import reduce

class Pierwsze:
    def __init__(self,n):
        self.i = 2
        self.n = n

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            while(self.i < self.n):
                if all(i % j != 0 for j in range(2, i)):
                    return i
                else:
                    i = self.i
                    self.i += 1
            raise StopIteration()
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self

def pierwsze_iteracyjnie(n):
    return(list(Pierwsze(n)))

def pierwsze_skladana(n):
    nie_pierwsze= [j for i in range(2, int(sqrt(n)+1)) for\
                 j in range(i*2, n+1, i)]
    pierwsze = [i for i in range(2, n+1) if i not in nie_pierwsze]
    return pierwsze

def pierwsze_funkcyjna(n):
    nie_lista = lambda lista: lambda x: x not in lista

    lista1 = list(map(lambda i: list(range(i*2, n+1, i)),\
                 range(2, n+1)))
    lista2 = reduce(lambda x, y: x + list(filter(nie_lista(x), y)),\
               lista1)
    lista3 = filter(nie_lista(lista2), range(2, n+1))

    return list(lista3)


if __name__ == '__main__':
    import timeit
    print("dla n=10:")
    print("Lista składana: ",timeit.timeit("pierwsze_skladana(10)",\
                        setup="from __main__ import pierwsze_skladana", number=1), "secs")
    print("Funkcyjna: ", timeit.timeit("pierwsze_funkcyjna(10)",\
                        setup="from __main__ import pierwsze_funkcyjna", number=1), "secs")
    print("Iteracyjnie: ", timeit.timeit("pierwsze_iteracyjnie(10)",\
                        setup="from __main__ import pierwsze_iteracyjnie", number=1), "secs", "\n")
    print("dla n=100:")
    print("Lista składana: ",timeit.timeit("pierwsze_skladana(100)",\
                        setup="from __main__ import pierwsze_skladana", number=1), "secs")
    print("Funkcyjna: ", timeit.timeit("pierwsze_funkcyjna(100)",\
                        setup="from __main__ import pierwsze_funkcyjna", number=1), "secs")
    print("Iteracyjnie: ", timeit.timeit("pierwsze_iteracyjnie(100)",\
                        setup="from __main__ import pierwsze_iteracyjnie", number=1), "secs", "\n")
    print("dla n=1000:")
    print("Lista składana: ",timeit.timeit("pierwsze_skladana(1000)",\
                        setup="from __main__ import pierwsze_skladana", number=1), "secs")
    print("Funkcyjna: ", timeit.timeit("pierwsze_funkcyjna(1000)",\
                        setup="from __main__ import pierwsze_funkcyjna", number=1), "secs")
    print("Iteracyjnie: ", timeit.timeit("pierwsze_iteracyjnie(1000)",\
                        setup="from __main__ import pierwsze_iteracyjnie", number=1), "secs")
