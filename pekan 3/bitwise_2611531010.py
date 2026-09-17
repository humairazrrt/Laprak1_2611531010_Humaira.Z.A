# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("\n========================================")
print("3. OPERATOR BITWISE")
print("==========================================")

angka1_1010 = int(input("Masukkan angka bitwise-1: "))
angka2_1010 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_1010, "| biner =", bin(angka1_1010))
print("angka2 =", angka2_1010, "| biner =", bin(angka2_1010))

# Bitwise AND
hasil_1010 = angka1_1010 & angka2_1010
print("\nBitwise AND (&)")
print(angka1_1010, "&", angka2_1010, "=", hasil_1010)
print("Biner hasil =", bin(hasil_1010))
print("Biner hasil (8 bit) =", format(hasil_1010, "08b"))

# Bitwise OR
hasil_1010 = angka1_1010 | angka2_1010
print("\nBitwise OR (|)")
print(angka1_1010, "|", angka2_1010, "=", hasil_1010)
print("Biner hasil =", bin(hasil_1010))
print("Biner hasil (8 bit) =", format(hasil_1010, "08b"))

# Bitwise XOR
hasil_1010 = angka1_1010 ^ angka2_1010
print("\nBitwise XOR (^)")
print(angka1_1010, "^", angka2_1010, "=", hasil_1010)
print("Biner hasil =", bin(hasil_1010))
print("Biner hasil (8 bit) =", format(hasil_1010, "08b"))

# Bitwise NOT
hasil_1010 = ~angka1_1010
print("\nBitwise NOT (~)")
print("~", angka1_1010, "=", hasil_1010)
print("Biner hasil =", bin(hasil_1010))
print("Biner hasil (8 bit) =", format(hasil_1010, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_1010 = angka1_1010 << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angka1_1010, "<<", jumlah_geser, "=", hasil_1010)
print("Biner hasil =", bin(hasil_1010))
print("Biner hasil (8 bit) =", format(hasil_1010, "08b"))

# Bitwise geser kanan
hasil_1010 = angka1_1010 >> jumlah_geser
print("\nBitwise geser kanan (>>)")
print(angka1_1010, ">>", jumlah_geser, "=", hasil_1010)
print("Biner hasil =", bin(hasil_1010))
print("Biner hasil (8 bit) =", format(hasil_1010, "08b"))