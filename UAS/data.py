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