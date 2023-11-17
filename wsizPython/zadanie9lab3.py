import random
tab = []
def generujDane():
    for i in range(10):
        tab2 = []
        for j in range(10):
            tab2.append(random.randint(1, 10))
        tab.append(tab2)
def wyswietlWynik():
    for tab2 in tab:
        for val in tab2:
            print(val, end='\t')
        print()
def przetworzDane():
    suma = 0
    for i in range(10):
        suma += tab[i][i]
        print(" ",end='\t')
        print(tab[i][i],end='\t')
    return suma

generujDane()
wyswietlWynik()
print("suma = ",przetworzDane())
