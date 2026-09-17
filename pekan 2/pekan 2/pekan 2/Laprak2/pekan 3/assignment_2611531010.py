# Program assignment dalam python

angka1_1010 = int(input("Input angka-1:"))
angka2_1010 = int(input("Input angka-2:"))

print("\nNilai awal angka1 =", angka1_1010)
print("Nilai awal angka2 =", angka2_1010)

# Assignement biasa
hasil_1010 = angka1_1010
print("\nAssignment Biasa (=)")
print("Hasil =", hasil_1010)

# Assignment penambahan
hasil_1010 = angka1_1010
hasil_1010 += angka2_1010   
print("\nAssignment Penambahan (+=)")
print("Hasil =", hasil_1010)

# Assignment pengurangan
hasil_1010 = angka1_1010
hasil_1010 -= angka2_1010
print("\nAssignment Pengurangan (-=)")
print("Hasil =", hasil_1010)

# Assignment perkalian
hasil_1010 = angka1_1010
hasil_1010 *= angka2_1010
print("\nAssignment Perkalian (*=)")
print("Hasil =", hasil_1010)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_1010 != 0:
    hasil_1010 = angka1_1010
    hasil_1010 /= angka2_1010
    print("\nAssignment Pembagian (/=)")
    print("Hasil =", hasil_1010)
    # Operator tambahan
    hasil_1010 = angka1_1010
    hasil_1010 //= angka2_1010  
    print("\nAssignment Pembagian Bulat (//=)")
    print("Hasil =", hasil_1010)
    hasil_1010 = angka1_1010
    hasil_1010 %= angka2_1010
    print("\nAssignment Sisa Bagi (%=)")
    print("Hasil =", hasil_1010)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0.")
    
# Operator tambahan: assignment perpangkatan
hasil_1010 = angka1_1010
hasil_1010 **= angka2_1010
print("\nAssignment Perpangkatan (**=)")
print("Hasil =", hasil_1010)