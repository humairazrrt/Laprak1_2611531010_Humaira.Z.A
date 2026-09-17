# Program operator logika dalam python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_1010 = input("Input nilai boolean-1 (True/False):").strip().lower() == "true"
a2_1010 = input("Input nilai boolean-2 (True/False):").strip().lower() == "true"

print("\nA1 =", a1_1010)
print("A2 =", a2_1010)

# Konjungsi: bernilai True jika keduanya True
hasil_1010 = a1_1010 and a2_1010
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_1010)

#Disjungsi: bernilai True jika salah satunya True
hasil_1010 = a1_1010 or a2_1010
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_1010)

# Negasi A1: membalik nilai A1
hasil_1010 = not a1_1010
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_1010)

# Negasi A2: membalik nilai A2
hasil_1010 = not a2_1010
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_1010)

# XOR: bernilai True jika kedua nilai berbeda
hasil_1010 = a1_1010 != a2_1010
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_1010)