from typing import Final

# 1. Deklarasi Konstanta (Ganti 1234 dengan 4 digit terakhir NIM kamu)
BATAS_LULUS_1234: Final[float] = 75.0

# 2. Input Data (String & Type Casting Numerik)
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_1234 = input("Masukkan Nama Mahasiswa: ")
jk_1234 = input("Masukkan Jenis Kelamin (L/P): ")

print("Masukkan Alamat Domisili (Tekan Enter, lalu ketik baris berikutnya):")
alamat_1234 = f"""{input("  Baris 1: ")}
{input("  Baris 2: ")}"""

umur_1234 = int(input("Masukkan Umur: "))
skor_1234 = float(input("Masukkan Skor Tes Awal: "))

# Tipe Data Complex & Boolean Verification
token_1234 = 100 + 3j
status_lulus_1234 = skor_1234 >= BATAS_LULUS_1234

# 3. Output Data dan Pengecekan Tipe Data
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa  : {nama_1234} | Tipe: {type(nama_1234)}")
print(f"Jenis Kelamin   : {jk_1234} | Tipe: {type(jk_1234)}")
print(f"Alamat Domisili :\n{alamat_1234} | Tipe: {type(alamat_1234)}")
print(f"Umur            : {umur_1234} tahun | Tipe: {type(umur_1234)}")
print(f"Skor Tes Awal   : {skor_1234} | Tipe: {type(skor_1234)}")
print(f"ID Token Sinyal : {token_1234} | Tipe: {type(token_1234)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai  : {BATAS_LULUS_1234}")
print(f"Apakah Dinyatakan Lulus?: {status_lulus_1234} | Tipe: {type(status_lulus_1234)}")