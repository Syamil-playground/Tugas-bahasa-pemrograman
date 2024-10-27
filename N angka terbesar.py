n = int(input("Masukkan jumlah angka: "))

angka_terbesar = float('-inf')  # Inisialisasi dengan nilai terkecil

for i in range(n):
    angka = float(input("Masukkan angka ke-{}: ".format(i+1)))
    if angka > angka_terbesar:
        angka_terbesar = angka

print("Angka terbesar adalah:", angka_terbesar)