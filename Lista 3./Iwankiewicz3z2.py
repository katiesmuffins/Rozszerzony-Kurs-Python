# coding: utf8 

from functools import reduce

def doskonale_skladana(n):
    dzielniki = lambda x: [i for i in range(1, x) if x % i == 0]

    doskonale = [j for j in range(1, n+1)\
                       if sum(dzielniki(j)) == j]
    return doskonale

def czy_doskonala(x):
    dzielniki = filter(lambda i: x % i == 0, range(1, x))
    return reduce(lambda x, y: x + y, dzielniki) == x

def doskonale_funkcyjna(n):
    return list(filter(lambda x: czy_doskonala(x), range(2, n+1)))



if __name__ == '__main__':
    import timeit
    print(timeit.timeit("doskonale_skladana(1000)",\
                        setup="from __main__ import doskonale_skladana", number=1), "secs")
    print(timeit.timeit("doskonale_funkcyjna(1000)",\
                        setup="from __main__ import doskonale_funkcyjna", number=1), "secs")

print(doskonale_skladana(1000))
print(doskonale_funkcyjna(1000))