# Meminta pengguna memasukkan modal awal
modal_awal = float(input("Masukkan modal awal (dalam juta): ")) * 1000000  # Konversi juta ke satuan rupiah
total_laba = 0

# Loop untuk menghitung laba setiap bulan
for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba = 0
    elif bulan == 3 or bulan == 4:
        laba = 0.01 * modal_awal  # 1% dari modal
    elif bulan == 5 or bulan == 6 or bulan == 7:
        laba = 0.05 * modal_awal  # 5% dari modal
    elif bulan == 8:
        laba = 0.03 * modal_awal  # 3% dari modal
    
    # Tampilkan laba per bulan
    print(f"Laba bulan ke-{bulan} sebesar: {laba}")
    
    # Tambahkan laba bulan ini ke total laba
    total_laba += laba

# Tampilkan total laba
print(f"Total laba adalah: {total_laba}")
