# Buat file dengan nama Konstanta_2611531010.py
# Program ini menggunakan konstanta untul menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1010

from typing import Final
PI: Final = 3.14
print("pi: %f" %(PI))
jari_1234 = float(input('Masukkan nilai jari-jari: '))
luas_1234 = PI * jari_1234 * jari_1234
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" %(jari_1234, luas_1234))