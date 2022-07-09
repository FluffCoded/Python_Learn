file = open("przyklad.txt", "r")
lines = file.readlines()
liczby = []
for line in lines:
    a = line.strip()

    liczby.append(a)
print(liczby)