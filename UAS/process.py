from data.data import TugasData
from view.view import TugasView

class TugasProses:
    def __init__(self):
        self.file= TugasData()
        self.view= TugasView()
        
    def run(self):
        while True:
            self.view.tampil_menu()
            pilih = input("Pilih antara (1-4):")

            if pilih == "1":
                self.view.tampil_tugas(self.file.semua_data())
            elif pilih== "2":
                tambah= self.view.input_baru()
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