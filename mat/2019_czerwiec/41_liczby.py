file = open("liczby_przyklad.txt", "r")
linie = file.readlines()
liczbytxt = [2]
for line in linie:
    a = line.lower().strip()
    a = int(a)
    if a >= 100 and a <= 5000:
        liczbytxt.append(a)
print("liczby", liczbytxt)


def prime(x):
    if x < 2:
        return False
    licznik = 0
    for i in range(2, x):
        if x % i == 0:
            licznik += 1
    if licznik == 0:
        print(x)


for liczba in liczbytxt:
    prime(liczba)
