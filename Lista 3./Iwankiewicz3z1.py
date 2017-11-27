# coding: utf8 

from math import sqrt
from functools import reduce

def pierwsze_skladana(n):
    nie_pierwsze= [j for i in range(2, int(sqrt(n)+1)) for\
                 j in range(i*2, n+1, i)]
    pierwsze = [i for i in range(2, n+1) if i not in nie_pierwsze]
    return pierwsze

def pierwsze_funkcyjna(n):
    nie_lista = lambda _list: lambda x: x not in _list

    lista1 = list(map(lambda i: list(range(i*2, n+1, i)),\
                 range(2, n+1)))
    lista2 = reduce(lambda x, y: x + list(filter(nie_lista(x), y)),\
               lista1)
    lista3 = filter(nie_lista(lista2), range(2, n+1))

    return list(lista3)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("pierwsze_skladana(50)",\
                        setup="from __main__ import pierwsze_skladana", number=1), "secs")
    print(timeit.timeit("pierwsze_funkcyjna(50)",\
                        setup="from __main__ import pierwsze_funkcyjna", number=1), "secs")
    print(pierwsze_skladana(50))
    print(pierwsze_funkcyjna(50))