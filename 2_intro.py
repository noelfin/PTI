# Perulangan -> Looping
# For Statement
# Index Data -> Dimulai 0

# Contoh 1
i = 1
for i in range (10) :
    print(i)

# Contoh 2
i = 0
for i in range (10) :
    i+= 1
    print(i)

# Contoh 3
i = 0
for baris in range(5):
    for kolom in range(5):
        print("*", end="")
    print()

# Contoh 4
i = 0 
for baris in range(5):
    for kolom in range(5):
        print("*")
    print()

# While Iteration -> Need Condition (Lakukan perulangan saat i < 10)

# Contoh 5 (Untuk menghentikan pakai ctrl + C)
baris2 = 0
while baris2 < 5 :
    kolom2 = 0
    while kolom2 < 5 :
        print("*", end="")
    print()

# Contoh 6 (Bisa berhenti)
baris2 = 0
while baris2 < 5 :
    baris2 +=1
    kolom2 = 0
    while kolom2 < 5 :
        kolom2 +=1
        print("*", end="")
    print()

# Contoh 7
baris2 = 0
tengah = 5
while baris2 < 5 :
    kolom2 = 0
    if(baris2 % 2 == 1):
        while kolom2 < 5 :
            if(kolom2 == int(round(tengah/2))):
                print("*", end="")
            else:
                print(" ", end="")
            kolom2 +=1
    else:
        while kolom2 < 5 :
            print("*", end="")
            kolom2 +=1
print()
baris2 +=1