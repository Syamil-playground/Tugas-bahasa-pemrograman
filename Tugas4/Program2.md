# Program 2
Program ini digunakan untuk menghitung total laba berdasarkan laba yang diperoleh setiap bulan selama 8 bulan. Berikut adalah penjelasan tentang cara kerja kode ini:

## Deskripsi Program

1. **Inisialisasi Variabel:**
   - Variabel `total_laba` diinisialisasi dengan nilai 0 untuk menyimpan total laba yang akan dihitung.

2. **Looping Bulanan:**
   - Program menggunakan perulangan `for` untuk menghitung laba dari bulan 1 hingga bulan 8.
   - Setiap bulan memiliki laba yang berbeda sesuai dengan periode berikut:
     - **Bulan 1 & 2**: Laba = 0
     - **Bulan 3 & 4**: Laba = 1.000.000
     - **Bulan 5 & 6**: Laba = 5.000.000
     - **Bulan 7 & 8**: Laba = 20.000.000
     
3. **Menampilkan Laba per Bulan:**
   - Laba setiap bulan ditampilkan dengan format "laba bulan ke-X sebesar: Y".

4. **Perhitungan Total Laba:**
   - Setiap laba yang diperoleh per bulan ditambahkan ke dalam variabel `total_laba` menggunakan operasi `+=`.

5. **Menampilkan Total Laba:**
   - Setelah loop selesai, program menampilkan total laba yang dihitung selama 8 bulan.

## Contoh Output Program:

Jika kode ini dijalankan, outputnya akan terlihat seperti berikut:
- laba bulan ke- 1 sebesar: 0 
- laba bulan ke- 2 sebesar: 0 
- laba bulan ke- 3 sebesar: 1000000.0 
- laba bulan ke- 4 sebesar: 1000000.0 
- laba bulan ke- 5 sebesar: 5000000.0 
- laba bulan ke- 6 sebesar: 5000000.0 
- laba bulan ke- 7 sebesar: 20000000.0 
- laba bulan ke- 8 sebesar: 20000000.0 
- Total laba adalah: 40000000.0
