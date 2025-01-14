# Program Sederhana dengan Konsep Modular dan OOP

Proyek ini mendemonstrasikan aplikasi Python sederhana menggunakan konsep pemrograman modular dan berorientasi objek (OOP). Aplikasi ini mengelola daftar tugas, memungkinkan pengguna untuk melihat, menambah, dan menghapus tugas melalui menu berbasis teks.

## Struktur Direktori
```
UAS SEMESTER1
│
└───Ex
    │
    ├───data
    │   └───data.py 
    ├───process 
    │   └───process.py
    ├───view
    │   └───view.py
    ├───main.py
```

## Deskripsi Modul

### data/data.py
Modul ini menangani penyimpanan dan pengelolaan data tugas.
```python
class TugasData:
    def __init__(self):
        self.data = []

    def tambah(self, data):
        self.data.append(data)

    def hapus(self, hps):
        if 0 <= hps < len(self.data):
            self.data.pop(hps)

    def semua_data(self):
        return self.data
```

### view/view.py
Modul ini menyediakan antarmuka pengguna untuk aplikasi.
```python
class TugasView:
    def tampil_menu(self):
        print("Menu:")
        print("1. Daftar Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")

    def tampil_tugas(self, tugas):
        if tugas:
            print("\nDaftar Tugas:")
            for id, tugas in enumerate(tugas, 1):
                print(f"{id}. {tugas}")

    def input_baru(self):
        return input("Masukkan tugas baru: ")

    def hapus_tugas(self):
        return int(input("Nomor yang akan dihapus:"))-1

    def pesan(self, pesan):
        print(pesan)
```

### process/process.py
Modul ini mengintegrasikan modul data dan view serta mengontrol alur program.
```python
from data.data import TugasData
from view.view import TugasView

class TugasProses:
    def __init__(self):
        self.file = TugasData()
        self.view = TugasView()

    def run(self):
        while True:
            self.view.tampil_menu()
            pilih = input("Pilih antara (1-4):")

            if pilih == "1":
                self.view.tampil_tugas(self.file.semua_data())
            elif pilih == "2":
                tambah = self.view.input_baru()
                self.file.tambah(tambah)
                self.view.pesan("Tugas berhasil ditambahkan!")
            elif pilih == "3":
                self.view.tampil_tugas(self.file.semua_data())
                hapus = self.view.hapus_tugas()
                self.file.hapus(hapus)
                self.view.pesan("Tugas telah dihapus!")
            elif pilih == "4":
                self.view.pesan("Program selesai!")
                break
            else:
                print("Invalid Hanya angka (1-4)!")
```

### main.py
Titik masuk aplikasi.
```python
from process.process import TugasProses

if __name__ == "__main__":
    process = TugasProses()
    process.run()
```

## Cara Menjalankan
1. Pastikan Python terinstal di sistem Anda.
2. Navigasikan ke direktori yang berisi `main.py`.
3. Jalankan program dengan perintah:
   ```
   python main.py
   ```
4. Ikuti petunjuk di layar untuk berinteraksi dengan aplikasi.

## Fitur
- Melihat semua tugas.
- Menambah tugas baru.
- Menghapus tugas berdasarkan nomor dalam daftar.
- Keluar dari program.

## Flowchart
![TLBBQiCm4BphApOvHT0UskPaKqXk3QMGWtzW7MrYOKasUZJaxxloeoN5kKXYjBCpgz4kHFGnMIE6WoWEJWUDHWSC6gfqmN3qNQ1GYg92sslJeeClSgaKddh2WTAd24TjT8Ek5E6guwc1pGH8SS90i7cHejZRMXi8P1E2meWGiy1TQuLdDZ9VZDHNEOiCCDJeqqYgiSca__3KgwV0wxeQR](https://github.com/user-attachments/assets/20746d8f-d0c3-4202-a6b1-e997526133ee)

