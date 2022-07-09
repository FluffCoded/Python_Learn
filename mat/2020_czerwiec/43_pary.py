file = open("pary.txt", "r")
tekst = file.readlines()
pary = []
for para in tekst:
    para = para.lower()
    fragment = para.strip().split()
    if int(fragment[0]) == len(fragment[1]):
        pary.append(fragment)
print(pary)
najmniejsza_para = pary[0]
for i in range(len(pary)):
    if pary[i][0] < najmniejsza_para[0]:
        najmniejsza_para = pary[i]
    elif pary[i][0] == najmniejsza_para[0]:
        for a in range(len(pary[i][1])):
            if pary[i][1][a] < najmniejsza_para[1][a]:
                najmniejsza_para = pary[i]
                break
            elif pary[i][1][a] > najmniejsza_para[1][a]:
                break
print("\nnajmniejsza para", najmniejsza_para)
