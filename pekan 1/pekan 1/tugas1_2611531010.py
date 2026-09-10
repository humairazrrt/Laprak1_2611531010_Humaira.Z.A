# Menampilkan bentuk hati dengan pola matematika
for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print("\033[91m*\033[0m", end=" ") # \033[91m memberi warna merah
        else:
            print(" ", end=" ")
    print()

print("\n\033[92m  FOR YOU! <3 \033[0m")
