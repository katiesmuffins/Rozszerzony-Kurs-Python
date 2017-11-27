def tabliczka(x1,x2,y1,y2):
    print(end='\t')
    for i in range(x1, x2+1):
        print(i, end='\t')
    print('\n')
    for rzad in range (y1, y2+1):
        print(rzad, end='\t')
        for kolumna in range (x1,x2+1):
            print(rzad * kolumna, end='\t')
        print('\n')

print(tabliczka(3,6,5,10))
print(tabliczka(2,9,1,7))
