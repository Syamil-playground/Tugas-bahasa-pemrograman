# Program Pengelolaan Data Mahasiswa

Program ini adalah aplikasi sederhana berbasis teks yang digunakan untuk mengelola data mahasiswa. Setiap mahasiswa memiliki beberapa data, yaitu nama, NIM, nilai tugas, nilai UTS, dan nilai UAS. Berdasarkan nilai-nilai ini, program akan menghitung nilai akhir untuk masing-masing mahasiswa dan menampilkan data yang telah dimasukkan.

## Fitur

- Input data mahasiswa (nama, NIM, nilai tugas, UTS, dan UAS).
- Validasi input agar nilai tugas, UTS, dan UAS harus berupa angka.
- Menghitung nilai akhir berdasarkan bobot:
  - Nilai Tugas: 30%
  - Nilai UTS: 35%
  - Nilai UAS: 35%
- Menampilkan data mahasiswa dalam bentuk tabel di akhir.

## Struktur Data

Data mahasiswa disimpan dalam bentuk list yang berisi elemen-elemen berikut:
- `nama`: Nama mahasiswa
- `nim`: NIM mahasiswa
- `tugas`: Nilai tugas (30% dari nilai akhir)
- `uts`: Nilai UTS (35% dari nilai akhir)
- `uas`: Nilai UAS (35% dari nilai akhir)
- `nilai_akhir`: Nilai akhir yang dihitung

## Cara Kerja

1. Program meminta pengguna untuk memasukkan data mahasiswa (nama dan NIM).
2. Pengguna memasukkan nilai tugas, UTS, dan UAS dengan validasi tipe data.
3. Nilai akhir dihitung menggunakan rumus berikut:
   nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
4. Data mahasiswa (nama, NIM, nilai tugas, UTS, UAS, dan nilai akhir) ditambahkan ke dalam list `data_mahasiswa`.
5. Program akan menanyakan apakah pengguna ingin menambah data mahasiswa lagi.
6. Setelah selesai, program akan mencetak semua data mahasiswa dalam bentuk tabel yang rapi.

## Contoh Tampilan Program
Nama : Muhammad syamil asy syabab -> NIM : 312410244 -> Nilai Tugas : 50 -> Nilai UTS : 35 -> Nilai UAS : 80 -> Tambah data (y/t)? -> y -> Nama : Budi -> NIM : 319910888 -> Nilai Tugas : 10 -> Nilai UTS : 100 -> Nilai UAS : 100 -> Tambah data (y/t)? -> t
t
### Output
![Screenshot 2024-11-12 090929](https://github.com/user-attachments/assets/82edb821-c0b8-47d0-9a04-1eca68366ef9)

### Flowchart:
![pP8nQyCm48Lt_OeZaprrTmY9jwQGBdM7JkMCbVZmIJNHgIR_leTjN0KCfLiqoERkyUvzXmv1y2hHiHb_Z2cEdW8XKy10e1-11WK_7RPQ20DkZRdQtg8OqAFoFWgyejD6MZYUL0Xw4d7Q9qQ2AbumR9SUdI6RscC3lf6fsUSWhVMGVM1k83b1llgbO3bOo2fgiBjN5HMwdhX33xqDUdTwi](https://github.com/user-attachments/assets/26332293-1130-4b38-8164-3341eb154a5a)

### Kode python:
![ray-so-export (1)](https://github.com/user-attachments/assets/d731dd72-8782-4810-996a-7b40d18e20f7)






