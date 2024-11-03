# Program Pemesanan Tiket Bioskop dan Kalkulator Sederhana
# Pemesanan Tiket Bioskop
Script ini digunakan untuk menghitung total harga tiket berdasarkan jenis tiket (reguler atau VIP) dan status keanggotaan (member atau non-member). Pengguna akan diminta untuk memilih tipe tiket dan menentukan apakah mereka memiliki kartu member, yang akan memberikan diskon pada harga tiket.

## Flowchart
![WhatsApp Image 2024-11-03 at 21 52 13](https://github.com/user-attachments/assets/b5112a13-42f3-4100-824c-667e876f3950)

## Kode Python
![Harga-tiket-bioskop](https://github.com/user-attachments/assets/52b8bfab-1c12-4d01-8952-05665adcd297)

## Fungsi

### `hitung_harga_tiket()`

Fungsi ini menghitung harga tiket berdasarkan input dari pengguna, dengan langkah-langkah sebagai berikut:

1. **Harga Tiket Dasar**: 
   - Tiket reguler: Rp50.000
   - Tiket VIP: Rp100.000

2. **Input Pengguna**:
   - `tipe_tiket`: Pengguna diminta untuk memasukkan tipe tiket (`reguler` atau `VIP`). Input ini diubah menjadi huruf kecil untuk memudahkan pemrosesan.
   - `status_member`: Pengguna diminta untuk memasukkan status member (`ya` untuk member, `tidak` untuk non-member).

3. **Penentuan Harga Tiket**:
   - Menggunakan operator ternary untuk menentukan harga tiket berdasarkan `tipe_tiket`.
   - Jika input tipe tiket tidak valid (bukan `reguler` atau `VIP`), program akan menampilkan pesan error dan berhenti.

4. **Menghitung Total Harga dengan Diskon**:
   - Jika pengguna adalah member (`status_member` = `ya`), mereka akan mendapatkan diskon 20% (total harga dikalikan 0.8).
   - Jika bukan member, harga tiket tetap (tanpa diskon).

5. **Menampilkan Total Harga**:
   - Menampilkan total harga tiket yang harus dibayar dalam format Rp (Rupiah) dengan dua angka desimal.



# Kalkulator Sederhana

Script ini adalah kalkulator sederhana yang memungkinkan pengguna untuk melakukan operasi dasar matematika, yaitu penjumlahan, pengurangan, perkalian, dan pembagian. Pengguna akan diminta memasukkan dua angka dan memilih operator yang diinginkan.

## Fungsi

### `kalkulator()`

Fungsi ini menerima input dari pengguna dan menghitung hasil berdasarkan operator yang dipilih oleh pengguna. Berikut adalah langkah-langkah yang dilakukan fungsi ini:

## Flowchart 
![WhatsApp Image 2024-11-03 at 21 52 12](https://github.com/user-attachments/assets/49260acc-b700-4686-b4c1-04fa8bf1ac14)

## Kode python
![Kalkulator-sederhana (2)](https://github.com/user-attachments/assets/dac8ab27-8a78-4fa1-85a5-5a70e1935bc6)

1. **Input Pengguna**:
   - `angka1`: Pengguna memasukkan angka pertama (float).
   - `operator`: Pengguna memasukkan operator (`+`, `-`, `x`, `:`) untuk operasi matematika yang ingin dilakukan.
   - `angka2`: Pengguna memasukkan angka kedua (float).

2. **Menghitung Hasil**:
   - Berdasarkan operator yang dipilih, fungsi akan melakukan salah satu operasi berikut:
     - `+` untuk penjumlahan
     - `-` untuk pengurangan
     - `x` untuk perkalian
     - `:` untuk pembagian (jika angka kedua tidak nol)
   - Jika operator tidak valid, fungsi akan menampilkan pesan error: "Error: Operator tidak valid."
   - Jika pembagian dengan nol terjadi, fungsi akan menampilkan pesan error: "Error: Pembagian dengan nol tidak diperbolehkan."

3. **Menampilkan Hasil**:
   - Jika operasi berhasil, fungsi akan mengembalikan hasil dalam format `Hasil: <nilai>`.

### Input & Output
```bash
Masukkan tipe tiket (reguler/VIP): reguler
Apakah Anda memiliki kartu member? (ya/tidak): ya
Total harga yang harus dibayar: Rp40000.00

Input angka pertama: 10
Pilih operator (+/-/x/:): x
Input angka kedua: 5
Hasil: 50.0



