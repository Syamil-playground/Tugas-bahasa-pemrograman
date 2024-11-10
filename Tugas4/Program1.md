# Program 1: Data Acak Kurang dari 0.5

Program ini menghasilkan sejumlah bilangan acak yang kurang dari 0.5 berdasarkan input pengguna.

### Cara Kerja

1. Pengguna diminta untuk memasukkan jumlah bilangan acak (`N`) yang ingin dihasilkan.
2. Program akan menghasilkan `N` bilangan acak yang nilainya kurang dari 0.5 menggunakan fungsi `random.random()`.
3. Setiap bilangan acak yang dihasilkan akan ditampilkan bersama nomor urutnya.
4. Setelah selesai, program menampilkan pesan "Selesai".

### Kode Program

```python
import random

# Meminta input jumlah data N dari pengguna
N = int(input("Masukkan nilai N: "))

# Loop untuk menghasilkan dan menampilkan N bilangan acak
for i in range(1, N + 1):
    angka = random.random()  # Menghasilkan bilangan acak antara 0 dan 1
    print(f"data ke-{i} => {angka}")

# Menampilkan pesan selesai setelah loop selesai
print("Selesai")
