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