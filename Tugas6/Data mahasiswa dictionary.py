# Dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

def tambah_data():
    print("\nTambah Data Mahasiswa")
    nim = input("Masukkan NIM: ")
    if nim in data_mahasiswa:
        print("Data dengan NIM ini sudah ada.")
        return
    nama = input("Masukkan Nama: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas, 'akhir': akhir}
    print("Data berhasil ditambahkan!")

def ubah_data():
    print("\nUbah Data Mahasiswa")
    nim = input("Masukkan NIM yang akan diubah: ")
    if nim not in data_mahasiswa:
        print("Data dengan NIM ini tidak ditemukan.")
        return
    print(f"Data ditemukan: {data_mahasiswa[nim]}")
    nama = input("Masukkan Nama baru: ")
    tugas = float(input("Masukkan Nilai Tugas baru: "))
    uts = float(input("Masukkan Nilai UTS baru: "))
    uas = float(input("Masukkan Nilai UAS baru: "))
    akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas, 'akhir': akhir}
    print("Data berhasil diubah!")

def hapus_data():
    print("\nHapus Data Mahasiswa")
    nim = input("Masukkan NIM yang akan dihapus: ")
    if nim not in data_mahasiswa:
        print("Data dengan NIM ini tidak ditemukan.")
        return
    del data_mahasiswa[nim]
    print("Data berhasil dihapus!")

def tampilkan_data():
    print("\nDaftar Nilai Mahasiswa")
    print("="*70)
    print("| NO |    NIM    |      NAMA       | TUGAS |  UTS  |  UAS  | AKHIR |")
    print("="*70)
    if not data_mahasiswa:
        print("|                        TIDAK ADA DATA                        |")
    else:
        for i, (nim, nilai) in enumerate(data_mahasiswa.items(), start=1):
            print(f"| {i:2} | {nim:9} | {nilai['nama']:15} | {nilai['tugas']:5.1f} | {nilai['uts']:5.1f} | {nilai['uas']:5.1f} | {nilai['akhir']:5.1f} |")
    print("="*70)

def cari_data():
    print("\nCari Data Mahasiswa")
    nim = input("Masukkan NIM yang akan dicari: ")
    if nim not in data_mahasiswa:
        print("Data dengan NIM ini tidak ditemukan.")
        return
    print("Data ditemukan:")
    print(f"NIM   : {nim}")
    print(f"Nama  : {data_mahasiswa[nim]['nama']}")
    print(f"Tugas : {data_mahasiswa[nim]['tugas']}")
    print(f"UTS   : {data_mahasiswa[nim]['uts']}")
    print(f"UAS   : {data_mahasiswa[nim]['uas']}")
    print(f"Akhir : {data_mahasiswa[nim]['akhir']}")

# Menu utama
while True:
    print("\nProgram Input Nilai")
    print("===================")
    print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    menu = input("Pilih menu: ").lower()

    if menu == 'l':
        tampilkan_data()
    elif menu == 't':
        tambah_data()
    elif menu == 'u':
        ubah_data()
    elif menu == 'h':
        hapus_data()
    elif menu == 'c':
        cari_data()
    elif menu == 'k':
        print("Keluar dari program. Terima kasih!")
        break
    else:
        print("Menu tidak valid. Silakan pilih lagi.")
