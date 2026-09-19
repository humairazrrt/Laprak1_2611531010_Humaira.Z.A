# ==============================================================================
# STUDI KASUS: SISTEM SIMULASI TRANSAKSI DAN VALIDASI AKSES TOKO
# Nama File : tugas3_1010.py
# ==============================================================================

print("=== SISTEM TRANSAKSI TOKO ===")

# ------------------------------------------------------------------------------
# 1. INPUT DATA PELANGGAN DAN TRANSAKSI
# ------------------------------------------------------------------------------
nama_1010 = input("Masukkan Nama Pelanggan : ")
status_pelanggan_1010 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
total_belanja_1010 = float(input("Masukkan Total Belanja : "))
jumlah_barang_1010 = int(input("Masukkan Jumlah Barang : "))
kode_promo_1010 = input("Masukkan Kode Promo : ").strip().upper()

# Daftar promo yang valid
daftar_promo_1010 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# ------------------------------------------------------------------------------
# 2. OPERATOR PERBANDINGAN & LOGIKA (VALIDASI)
# ------------------------------------------------------------------------------
# Operator Perbandingan
min_belanja_1010 = total_belanja_1010 >= 200000
min_barang_1010 = jumlah_barang_1010 >= 3
is_member_1010 = status_pelanggan_1010 == "member"

# Operator Keanggotaan (Membership)
promo_valid_1010 = kode_promo_1010 in daftar_promo_1010
promo_invalid_1010 = kode_promo_1010 not in daftar_promo_1010

# Operator Logika (and, or, not)
dapat_diskon_1010 = is_member_1010 and min_belanja_1010
dapat_promo_1010 = promo_valid_1010 or (min_barang_1010 and min_belanja_1010)
bukan_member_1010 = not is_member_1010

# ------------------------------------------------------------------------------
# 3. OPERATOR ARITMATIKA & PENUGASAN (CALCULATION)
# ------------------------------------------------------------------------------
# Operator Aritmatika dasar
persen_diskon_1010 = 0.10 if dapat_diskon_1010 else 0.0
besarnya_diskon_1010 = total_belanja_1010 * persen_diskon_1010
total_pembayaran_1010 = total_belanja_1010 - besarnya_diskon_1010

# Operator Aritmatika / (Pembagian) & % (Modulus)
rata_rata_harga_1010 = total_belanja_1010 / jumlah_barang_1010 if jumlah_barang_1010 > 0 else 0
sisa_barang_1010 = jumlah_barang_1010 % 3  # Sisa pembagian per paket isi 3

# Operator Penugasan (Augmented Assignment)
poin_1010 = 0
poin_1010 += int(total_pembayaran_1010 // 10000)  # Tambah 1 poin tiap Rp10.000

if dapat_promo_1010 and kode_promo_1010 == "HEMAT10":
    total_pembayaran_1010 -= 10000  # Potongan tambahan Rp10.000

# ------------------------------------------------------------------------------
# 4. OPERATOR IDENTITAS (IDENTITY)
# ------------------------------------------------------------------------------
# Menunjukkan perbedaan antara 'is' (identitas objek) dan '==' (kesamaan nilai)
list_promo_A_1010 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
list_promo_B_1010 = list_promo_A_1010
list_promo_C_1010 = list_promo_A_1010.copy()

is_objek_sama_1010 = list_promo_A_1010 is list_promo_B_1010       # True
is_objek_beda_1010 = list_promo_A_1010 is not list_promo_C_1010   # True
is_nilai_sama_1010 = list_promo_A_1010 == list_promo_C_1010       # True

# ------------------------------------------------------------------------------
# 5. OPERATOR BITWISE (HAK AKSES & KODE STATUS)
# ------------------------------------------------------------------------------
# Definisi Bit Flag
BIT_MEMBER_1010 = 0b0001  # 1
BIT_BELANJA_1010 = 0b0010  # 2
BIT_BARANG_1010  = 0b0100  # 4
BIT_PROMO_1010   = 0b1000  # 8

# Pembentukan Kode Status Transaksi Menggunakan Operator Bitwise OR (|)
kode_status_1010 = 0b0000
if is_member_1010:
    kode_status_1010 |= BIT_MEMBER_1010
if min_belanja_1010:
    kode_status_1010 |= BIT_BELANJA_1010
if min_barang_1010:
    kode_status_1010 |= BIT_BARANG_1010
if promo_valid_1010:
    kode_status_1010 |= BIT_PROMO_1010

# Pemeriksaan Akses Menggunakan Operator Bitwise AND (&)
cek_member_1010 = (kode_status_1010 & BIT_MEMBER_1010) != 0
cek_promo_1010  = (kode_status_1010 & BIT_PROMO_1010) != 0

# Perbandingan Status Menggunakan Operator Bitwise XOR (^)
kode_referensi_1010 = 0b1011  # Referensi standar (Member + Belanja + Promo)
perbedaan_status_1010 = kode_status_1010 ^ kode_referensi_1010

# Bitwise Shift (<<)
shifted_status_1010 = kode_status_1010 << 1

# ------------------------------------------------------------------------------
# 6. OUTPUT HASIL TRANSAKSI DAN OPERATOR
# ------------------------------------------------------------------------------
print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan        : {nama_1010}")
print(f"Status Pelanggan      : {status_pelanggan_1010}")
print(f"Total Belanja         : Rp{int(total_belanja_1010)}")
print(f"Jumlah Barang         : {jumlah_barang_1010}")
print(f"Kode Promo            : {kode_promo_1010}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000   : {min_belanja_1010}")
print(f"Jumlah Barang >= 3    : {min_barang_1010}")
print(f"Status Member         : {is_member_1010}")
print(f"Kode Promo Tersedia   : {promo_valid_1010}")
print(f"Mendapatkan Diskon    : {dapat_diskon_1010}")
print(f"Mendapatkan Promo     : {dapat_promo_1010}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                : Rp{int(besarnya_diskon_1010)}")
print(f"Total Pembayaran      : Rp{int(total_pembayaran_1010)}")
print(f"Rata-rata Harga Barang: Rp{int(rata_rata_harga_1010)}")
print(f"Poin Diperoleh        : {poin_1010}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Status Transaksi : {format(kode_status_1010, '04b')}")
print(f"Member Access         : {cek_member_1010}")
print(f"Promo Access          : {cek_promo_1010}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print(f"Kode Biner   : {format(kode_status_1010, '04b')}")
print(f"Kode Desimal : {kode_status_1010}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(kode_status_1010, '04b')} & 0001")
print(f"Hasil Biner   : {format(kode_status_1010 & BIT_MEMBER_1010, '04b')}")
print(f"Hasil Desimal : {kode_status_1010 & BIT_MEMBER_1010}")

print("\nCek Promo")
print(f"{format(kode_status_1010, '04b')} & 1000")
print(f"Hasil Biner   : {format(kode_status_1010 & BIT_PROMO_1010, '04b')}")
print(f"Hasil Desimal : {kode_status_1010 & BIT_PROMO_1010}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {format(kode_status_1010, '04b')}")
print(f"Kode Referensi : {format(kode_referensi_1010, '04b')}")
print(f"{format(kode_status_1010, '04b')} ^ {format(kode_referensi_1010, '04b')}")
print(f"Hasil Biner   : {format(perbedaan_status_1010, '04b')}")
print(f"Hasil Desimal : {perbedaan_status_1010}")

print("\n=== Shift ===")
print(f"{format(kode_status_1010, '04b')} << 1")
print(f"Hasil Biner   : {format(shifted_status_1010, '05b')}")
print(f"Hasil Desimal : {shifted_status_1010}")

print("\n=== OPERATOR IDENTITAS ===")
print(f"list_promo_A is list_promo_B : {is_objek_sama_1010}")
print(f"list_promo_A is not list_promo_C : {is_objek_beda_1010}")
print(f"list_promo_A == list_promo_C : {is_nilai_sama_1010}")

print("\n=== SELESAI ===")