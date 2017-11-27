def slownie(n):
    jednosci = ['', 'jeden', 'dwa','trzy','cztery','pięć','sześć', 'siedem', 'osiem', 'dziewięć']
    tys = ['', '', 'dwa','trzy','cztery','pięć','sześć', 'siedem', 'osiem', 'dziewięć']
    nastki = ['','jedenaście','dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście','siedemnaście', 'osiemnaście', 'dziewiętnaście']
    dziesiatki = ['','dziesięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt']
    setki = ['', 'sto', 'dwieście','trzysta', 'czterysta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset']
    tysiac = ['', 'tysiąc', 'milion'] 
    tysiace = ['', 'tysiące', 'miliony']
    tysiecy = ['', 'tysięcy', 'milionów']
    miliony = [2, 3, 4]
    milionow = [5, 6, 7, 8, 9, 0]
    wynik = []
    if n == 0: 
        wynik.append('zero')
    if n == 1000:
        wynik.append('tysiąc')
        return  ' '.join(wynik)
    if n == 100:
        wynik.append('sto')
        return ' '.join(wynik)
    if n == 1000000:
        wynik.append('milion')
        return ' '.join(wynik)

    else:  
        liczba = '%d' %n
        dlLiczby = len(liczba)
        grupy = (dlLiczby+2)//3
        liczba = liczba.zfill(grupy*3)
        for i in range(0,grupy*3, 3):
            s,d,j = int(liczba[i]), int(liczba[i+1]), int(liczba[i+2])
            g = grupy-((i//3)+1)
            if s>1:
                wynik.append(setki[s])
            if d>1:
                wynik.append(dziesiatki[d])
                if j>=1: wynik.append(jednosci[j])
            elif d == 1:
                if j >=1: wynik.append(nastki[j]) 
                else: wynik.append(dziesiatki[d])
            else: 
                if j>=1: wynik.append(jednosci[j])
            if (g>=1) and ((s+d+j)>0): 
                if j == 1: 
                    wynik.append(tysiac[g])
                elif j in miliony: 
                    wynik.append(tysiace[g])
                elif j in milionow:
                    wynik.append(tysiecy[g])  
    return ' '.join(wynik)

print(slownie(4245))
print(slownie(5))
print(slownie(652917))
print(slownie(10982))
print(slownie(2345))
print(slownie(23450731))
print(slownie(4000000))
print(slownie(1000))
print(slownie(1000000))
print(slownie(10000))
print(slownie(100))