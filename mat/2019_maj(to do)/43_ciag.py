file = open("przyklad.txt", "r")
liczby = file.read().splitlines()
liczby = list(map(int, liczby))
print(liczby)


def wspolnydzielnik(lista):
    mini = lista[0]
    for i in range(len(lista)):
        if lista[i] < mini:
            mini = lista[i]
    if mini == 2:
        koniec = 3
    else:
        koniec = mini
    najwiekszy_dzielnik = 0
    for dzielnik in range(2, koniec):
        licznik = 0
        for i in range(len(lista) - 1):
            if lista[i] % dzielnik == 0:
                licznik += 1
        if licznik == len(lista):
            if dzielnik > najwiekszy_dzielnik:
                najwiekszy_dzielnik = dzielnik
    return najwiekszy_dzielnik

cos = [4, 6, 10, 2]

print(wspolnydzielnik(cos))
max_ciag = 6
ciag = 6
