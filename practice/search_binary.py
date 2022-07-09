import sys
import random

rng = random.SystemRandom()
liczby = []
for i in range(5000000):
    liczby.append(rng.randint(0, 100000000))
liczby.sort()
lista = liczby
print("lista:\n", lista, "\n")


def search(szukana, start=0, end=len(lista), last_start=2, last_end=1):
    target = int((start + end) / 2)
    if lista[target] == szukana:
        print("------ ", szukana, " jest w liscie ------ ")
        return True
    if start == last_start and end == last_end:
        print("------ ", szukana, " nie ma na liscie ------ ")
        return False
    if lista[target] > szukana:
        search(szukana, start, target, start, end)
    elif lista[target] < szukana:
        search(szukana, target, end, start, end)


# test number
liczba = random.randint(2, 122)
print("przykladowa liczba: ", lista[liczba])
print("next przykladowa liczba: ", lista[liczba + 1])
# search
while 1 == 1:
    x = int(input("Wyszukaj liczbe: "))
    search(x)
