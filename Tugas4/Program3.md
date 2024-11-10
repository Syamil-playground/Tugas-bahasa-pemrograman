# Program 3: Simulasi ATM Sederhana

Program ini merupakan simulasi ATM sederhana yang ditulis dalam bahasa Python. Program ini memungkinkan pengguna untuk:
- Melihat saldo saat ini.
- Menarik uang jika saldo mencukupi.
- Keluar dari program.

Program ini berjalan di terminal dan akan terus menampilkan menu hingga pengguna memilih untuk keluar.

## Fitur Program

1. **Menampilkan Saldo Awal**  
   Program dimulai dengan saldo awal sebesar Rp 1,000,000.

2. **Penarikan Uang**  
   Pengguna dapat menarik uang dalam jumlah tertentu, dan program akan mengecek apakah saldo mencukupi.

3. **Penghentian Program**  
   Pengguna dapat memilih untuk keluar dari program kapan saja.

## Cara Kerja Program

1. **Inisialisasi Saldo Awal**  
   Pada awal program, saldo pengguna diinisialisasi dengan nilai Rp 1,000,000.

2. **Loop Utama ATM**  
   Program berjalan dalam loop tak terbatas sehingga terus menampilkan saldo dan menu hingga pengguna memilih untuk keluar.

3. **Menu dan Pilihan Pengguna**  
   Pada setiap iterasi, program menampilkan menu dengan dua pilihan:
   - **1. Tarik Uang**: Memungkinkan pengguna untuk menarik uang dari saldo mereka.
   - **2. Keluar**: Mengakhiri program.

4. **Proses Penarikan Uang**  
   - Jika pengguna memilih opsi 1, mereka diminta untuk memasukkan jumlah uang yang ingin ditarik.
   - Program kemudian memeriksa apakah saldo mencukupi untuk melakukan penarikan:
     - Jika saldo mencukupi, program mengurangi saldo sesuai jumlah yang diminta dan menampilkan pesan bahwa penarikan berhasil.
     - Jika saldo tidak mencukupi, program menampilkan pesan bahwa saldo tidak cukup untuk penarikan.

5. **Mengakhiri Program**  
   - Jika pengguna memilih opsi 2, program menampilkan pesan terima kasih dan keluar dari loop, sehingga program berakhir.
   - Jika pengguna memasukkan pilihan yang tidak valid, program akan memberikan pesan kesalahan dan meminta pengguna untuk mencoba lagi.

## Contoh Penggunaan

Berikut adalah contoh interaksi dengan program:

``` Output
Saldo saat ini: Rp 1000000
1. Tarik Uang
2. Keluar
Pilih menu (1/2): 1
Masukkan jumlah penarikan: 500000
Penarikan berhasil!

Saldo saat ini: Rp 500000
1. Tarik Uang
2. Keluar
Pilih menu (1/2): 2
Terima kasih telah menggunakan ATM!
