# Program keanggotaan dan identitas dalam python

print("==================================")
print("1.OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma'
Input_data = input("Input beberapa data, pisahkan dengan koma:")

# Mengubah input menjadi list integer
data = [int(angka.strip()) for angka in Input_data.split(",")]

nilai_dicari = int(input("Masukkan angka yang ingin dicari:"))

# Operator in
hasil_1010 = nilai_dicari in data
print("\nOperator keanggotaan IN")
print(nilai_dicari, "in data =", hasil_1010)

#Operator not in
hasil_1010 = nilai_dicari not in data
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari, "not in", data, "=", hasil_1010)
print("==================================")
print("2.OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_1010 = data

# objek2 merujuk pada objek yang sama dengan objek1
objek2_1010 = objek1_1010

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_1010 = data.copy()

print("objek1 =", objek1_1010)
print("objek2 =", objek2_1010)
print("objek3 =", objek3_1010)

# Operator is
hasil_1010 = objek1_1010 is objek2_1010
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_1010)

# Operator is not
hasil_1010 = objek1_1010 is not objek3_1010
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_1010)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_1010 is objek3_1010)
print("objek1 == objek3 =", objek1_1010 == objek3_1010)
