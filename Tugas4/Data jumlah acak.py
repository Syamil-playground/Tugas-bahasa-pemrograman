import random

# Meminta input jumlah data N dari pengguna
N = int(input("Masukkan nilai N: "))

# Loop untuk menghasilkan dan menampilkan N bilangan acak
for i in range(1, N + 1):
    angka = random.random()  # Menghasilkan bilangan acak antara 0 dan 1
    print(f"data ke-{i} => {angka}")

# Menampilkan pesan selesai setelah loop selesai
print("Selesai")

