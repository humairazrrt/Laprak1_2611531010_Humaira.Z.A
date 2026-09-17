# Buat program untuk operator aritmatika dalam Pyhton

angka1_1010 = int(input("Input angka-1:"))
angka2_1010 = int(input("Input angka-2:"))

# Penjumalahan
hasil_1010 = angka1_1010 + angka2_1010
print("\nOperator Penjumalhan")
print("Hasil =", hasil_1010)

# Pengurangan
hasil_1010 = angka1_1010 - angka2_1010
print("\nOperator Pengurangan")
print("Hasil =", hasil_1010)

# Perkalian
hasil_1010 = angka1_1010 * angka2_1010
print("\nOperator Perkalian")
print("Hasil =", hasil_1010)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_1010 != 0:
    hasil_1010 = angka1_1010 / angka2_1010
    print("\nOperator Pembagian")
    print("Hasil =", hasil_1010)

    hasil_1010 = angka1_1010 // angka2_1010
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_1010)

    hasil_1010 = angka1_1010 % angka2_1010
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_1010)
else:
    print("Angka kedua tidak boleh bernilai 0.")
    
# Pangkat
hasil_1010 = angka1_1010 ** angka2_1010
print("\nOperator Pangkat")
print("Hasil =", hasil_1010)