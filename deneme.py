" This file is for blah blah blah "
NAME = "Mustafa2"
SURNAME = "Yildiz"
surnames = ["Yildiz","Aksoy","Demir"]

if SURNAME in surnames:
    print(True)
else:
    print(False)


for soyad in surnames:
    #print(soyad)
    if soyad == SURNAME:
        print(True)
    else:
        print(False)

A = 0

while 1:
    print("Elma")
    print(A)
    A+=1
    if A > 4:
        break
