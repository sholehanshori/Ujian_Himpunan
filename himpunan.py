#  ------------------------ Selasa, 12 November 2019 -----------------------------------

A = []
B = []
C = []
D = []
E = []

# A = himpunan (set) bilangan genap antara 1 dan 20.
# B = himpunan (set) bilangan ganjil antara 1 dan 20.
# C = himpunan (set) bilangan negatif lebih dari -10.
# D = himpunan (set) bilangan prima antara 1 dan 20.
# E = himpunan (set) bilangan komposit antara 1 dan 20.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def genap(angka):
    for i in range(0, angka+1):
        if i%2 == 0:
            A.append(i)             # Tidak tau maksud dari eror, tapi program jalan
genap(20)
# print(A)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ganjil(angka):
    for j in range(1, angka):
        if j%2 != 0:
            B.append(j)             # Tidak tau maksud dari eror, tapi program jalan
ganjil(20)
# print(B)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def negatif(angka):
    for k in range(angka, 0):
        C.append(k)                 # Tidak tau maksud dari eror, tapi program jalan
negatif(-10)
# print(C)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

y = range(2, 20)
for l in range(2, 20):
    y = list(filter(lambda x: x%l != 0 or x/l == 1, y))
D = y
# print(D)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def komposit(angka):
    hasil = False
    if angka > 1:
        for i in range(2, angka):
            if angka % i == 0:
                hasil = True
                break
            else:
                hasil = False
    else:
        hasil = False
    return hasil

E = list(filter(komposit, range(21)))
# print(E)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''' Operasi Himpunan '''
A = set(A); B = set(B); C = set(C); D = set(D); E = set(E)

# a. A ∪ B ∪ C ∪ D ∪ E
operasi_1 = A | B | C | D | E
# print(sorted(operasi_1))

# b. (A ∩ B) ∪ (D ∩ E)
operasi_2 = (A&B) | (D&E)
# print(operasi_2)

# c. (A ∪ B) ∩ (D ∪ E)
operasi_3 = (A|B) & (D|E)
# print(operasi_3)

# d. (A ∪ B) - (D ∪ E)
operasi_4 = (A|B) - (D|E)
# print(operasi_4)

# e. (A ∪ B ∪ C) - (A ∩ E)
operasi_5 = (A|B|C) - (A&E)
# print(sorted(operasi_5))