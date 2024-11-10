# Inisialisasi saldo awal
saldo = 1000000

# Loop utama ATM
while True:
    # Menampilkan saldo dan menu
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    
    # Meminta pilihan menu dari pengguna
    pilihan = input("Pilih menu (1/2): ")
    
    # Mengecek pilihan pengguna
    if pilihan == "1":
        # Meminta jumlah penarikan
        jumlah_tarik = int(input("Masukkan jumlah penarikan: "))
        
        # Mengecek apakah saldo cukup
        if jumlah_tarik <= saldo:
            saldo -= jumlah_tarik
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak mencukupi!")
    
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM!")
        break  # Keluar dari loop dan mengakhiri program
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
