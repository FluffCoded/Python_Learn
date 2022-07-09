import secrets
import time

'#array z liczbami'
ilosc = int(input("podaj ilosc liczb: "))
i = 0
liczby = [None] * ilosc
while i < ilosc:
    liczby[i] = secrets.randbelow(10)
    i += 1
print(liczby)

liczbys = liczby
start_time = time.time()
liczbys.sort()
end_times = time.time() - start_time
print("sort", liczbys)
print(".sort finished in ", int(end_times), " seconds")

'#linear'
start_time = time.time()
a = 0
liczbyl = liczby
while a < ilosc:
    temp = liczbyl[a]
    i = a
    while i < ilosc:
        if liczbyl[i] < temp:
            temp2 = liczbyl[i]
            liczbyl[i] = temp
            temp = temp2
        i += 1
    liczbyl[a] = temp
    a += 1
current_time = time.time()
end_timel = current_time - start_time

'#Bubble'
start_time = time.time()
liczbyb = liczby
liczbyb.append(int(liczbyb[ilosc - 1]) + 1)
i = 0
a = 0
while a < ilosc:
    while i < ilosc - a:
        if liczbyb[i] > liczbyb[i + 1]:
            temp = liczbyb[i]
            liczbyb[i] = liczbyb[i + 1]
            liczbyb[i + 1] = temp
        i += 1
    i = 0
    a += 1
liczbyb.pop(ilosc)
current_time = time.time()
end_timeb = current_time - start_time

print("linear sorted", liczbyl)
print("linear finished in ", int(end_timel), " seconds")
print("bubble", liczbyb)
print("Bubble finished in ", int(end_timeb), " seconds")