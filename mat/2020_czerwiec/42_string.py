file = open("pary.txt", 'r')
linie = file.readlines()
fragmenty = []
for line in linie:
    fragmenty.append(str(line).strip().split(' '))

print("\nMax ilosc znakow w string: ")
print(fragmenty)
for fragment in fragmenty:
    maks = [0, None]
    for znak in fragment[1]:
        if fragment[1].count(znak) > maks[0]:
            maks[0] = fragment[1].count(znak)
            maks[1] = znak
    print(maks)


# tablica tylko z tekstami
tekst = []
for fragment in fragmenty:
    tekst.append(fragment[1])
fragmenty = tekst


print(" max ciag liter we fragmencie: ")
print(fragmenty)
for fragment in fragmenty:
    max_znak = fragment[0]
    max_znak_count = 1
    znak_count = 1
    znak = None

    for i in range(len(fragment) - 1):
        if fragment[i] == fragment[i+1]:
            znak = fragment[i]
            znak_count += 1
        else:
            znak_count = 1
        if znak_count > max_znak_count:
            max_znak = znak
            max_znak_count = znak_count
    print("znak: ", max_znak, " ilosc: ", max_znak_count)
