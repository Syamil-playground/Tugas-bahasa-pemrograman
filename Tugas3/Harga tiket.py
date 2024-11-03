def hitung_harga_tiket():
    # Harga tiket
    harga_reguler = 50000
    harga_vip = 100000

    # Meminta input dari pengguna
    tipe_tiket = input("Masukkan tipe tiket (reguler/VIP): ").lower()
    status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

    # Menentukan harga tiket dengan operator ternary
    harga_tiket = harga_reguler if tipe_tiket == "reguler" else harga_vip if tipe_tiket == "vip" else None

    if harga_tiket is None:
        print("Tipe tiket tidak valid.")
        return

    # Menghitung total harga dengan diskon menggunakan operator ternary
    total_harga = harga_tiket * (0.8 if status_member == "ya" else 1)

    # Menampilkan total harga yang harus dibayar
    print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")

# Memanggil fungsi
hitung_harga_tiket()
