# List untuk menyimpan data mahasiswa
data_mahasiswa = []

while True:
    # Input data mahasiswa
    nama = input("Nama : ")
    nim = input("NIM : ")
    
    # Input nilai tugas dengan pengecekan kesalahan
    while True:
        try:
            tugas = int(input("Nilai Tugas : "))
            break
        except ValueError:
            print("Nilai Tugas harus berupa angka. Silakan masukkan kembali.")

    # Input nilai UTS dengan pengecekan kesalahan
    while True:
        try:
            uts = int(input("Nilai UTS : "))
            break
        except ValueError:
            print("Nilai UTS harus berupa angka. Silakan masukkan kembali.")

    # Input nilai UAS dengan pengecekan kesalahan
    while True:
        try:
            uas = int(input("Nilai UAS : "))
            break
        except ValueError:
            print("Nilai UAS harus berupa angka. Silakan masukkan kembali.")

    # Hitung nilai akhir
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

    # Tambahkan data ke dalam list
    data_mahasiswa.append([nama, nim, tugas, uts, uas, nilai_akhir])

    # Tanya apakah ingin menambah data lagi
    tambah = input("Tambah data (y/t)? ")
    if tambah.lower() == 't':
        break

# Tampilkan daftar data mahasiswa
print("\n===================================================================")
print("| No |     Nama     |    NIM    | Tugas | UTS | UAS |  Akhir |")
print("===================================================================")

for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"| {i:2} | {mahasiswa[0]:11} | {mahasiswa[1]:7} | {mahasiswa[2]:5} | {mahasiswa[3]:3} | {mahasiswa[4]:3} | {mahasiswa[5]:6.2f} |")

print("===================================================================")

