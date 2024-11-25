# Inisialisasi data mahasiswa sebagai list kosong
data_mahasiswa = []

# Fungsi untuk menambah data mahasiswa
def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    data_mahasiswa.append({'nama': nama, 'nilai': nilai})
    print(f"Data mahasiswa {nama} berhasil ditambahkan.\n")

# Fungsi untuk menampilkan data mahasiswa
def lihat():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa.\n")
        return
    print("Daftar Nilai Mahasiswa:")
    for i, mahasiswa in enumerate(data_mahasiswa, start=1):
        print(f"{i}. Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")
    print()

# Fungsi untuk menghapus data mahasiswa berdasarkan nama
def hapus(nama):
    global data_mahasiswa
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'].lower() == nama.lower():
            data_mahasiswa.remove(mahasiswa)
            print(f"Data mahasiswa {nama} berhasil dihapus.\n")
            return
    print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.\n")

# Fungsi untuk mengubah data mahasiswa berdasarkan nama
def ubah(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'].lower() == nama.lower():
            nilai_baru = float(input(f"Masukkan nilai baru untuk {nama}: "))
            mahasiswa['nilai'] = nilai_baru
            print(f"Data mahasiswa {nama} berhasil diubah.\n")
            return
    print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.\n")

# Program utama
while True:
    print("Tambah(T)")
    print("Lihat(L) ")
    print("Hapus(H) ")
    print("Ubah(U) ")
    print("Keluar(K)")
    pilihan = input("Pilih(T/L/H/U/K): ")

    if pilihan == "T":
        tambah()
    elif pilihan == "L":
        lihat()
    elif pilihan == "H":
        nama_hapus = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        hapus(nama_hapus)
    elif pilihan == "U":
        nama_ubah = input("Masukkan nama mahasiswa yang ingin diubah: ")
        ubah(nama_ubah)
    elif pilihan == "K":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
