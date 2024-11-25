## Python
![Subrutin_fungsi](https://github.com/user-attachments/assets/40cda49f-08a9-4b3f-ab52-c8541a1d74d0)
## Flowchart
![pladitor_diagram (1)](https://github.com/user-attachments/assets/b69f732b-157a-4172-b84d-59b8fc944097)

# Program Pengelolaan Data Nilai Mahasiswa

Program ini adalah aplikasi sederhana berbasis Python yang memungkinkan pengguna untuk mengelola data nilai mahasiswa. Fitur yang tersedia meliputi:
- Menambahkan data mahasiswa.
- Menampilkan daftar nilai mahasiswa.
- Menghapus data mahasiswa berdasarkan nama.
- Mengubah nilai mahasiswa berdasarkan nama.

## Fitur dan Penjelasan

### 1. **Menambahkan Data (`tambah`)**
   - Fungsi ini digunakan untuk menambah data mahasiswa.
   - **Langkah-langkah kerja:**
     1. Program meminta pengguna memasukkan nama mahasiswa.
     2. Program meminta pengguna memasukkan nilai mahasiswa (dalam format angka).
     3. Data nama dan nilai akan disimpan ke dalam list `data_mahasiswa` sebagai dictionary.
   - **Output:** Pesan konfirmasi bahwa data telah berhasil ditambahkan.

### 2. **Menampilkan Data (`tampilkan`)**
   - Fungsi ini digunakan untuk menampilkan seluruh data mahasiswa yang telah ditambahkan.
   - **Langkah-langkah kerja:**
     1. Program memeriksa apakah terdapat data di list `data_mahasiswa`.
     2. Jika data tersedia, program akan mencetak daftar mahasiswa dengan format:
        ```
        <No>. Nama: <nama>, Nilai: <nilai>
        ```
     3. Jika tidak ada data, program akan menampilkan pesan bahwa data kosong.
   - **Output:** Daftar nilai mahasiswa atau pesan bahwa data kosong.

### 3. **Menghapus Data (`hapus`)**
   - Fungsi ini digunakan untuk menghapus data mahasiswa berdasarkan nama.
   - **Langkah-langkah kerja:**
     1. Program meminta pengguna memasukkan nama mahasiswa yang ingin dihapus.
     2. Program mencari nama tersebut di dalam list `data_mahasiswa`.
     3. Jika ditemukan, data mahasiswa akan dihapus dari list.
     4. Jika tidak ditemukan, program akan menampilkan pesan bahwa nama tidak ditemukan.
   - **Output:** Pesan konfirmasi atau pesan kesalahan jika nama tidak ditemukan.

### 4. **Mengubah Data (`ubah`)**
   - Fungsi ini digunakan untuk mengubah nilai mahasiswa berdasarkan nama.
   - **Langkah-langkah kerja:**
     1. Program meminta pengguna memasukkan nama mahasiswa yang ingin diubah.
     2. Program mencari nama tersebut di dalam list `data_mahasiswa`.
     3. Jika ditemukan, program meminta pengguna memasukkan nilai baru untuk mahasiswa tersebut, lalu memperbarui nilai di dalam list.
     4. Jika tidak ditemukan, program akan menampilkan pesan bahwa nama tidak ditemukan.
   - **Output:** Pesan konfirmasi atau pesan kesalahan jika nama tidak ditemukan.
## Output
![Output (1)](https://github.com/user-attachments/assets/576846ea-be90-4ef7-9509-193acaf06d72)
