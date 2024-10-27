angka1=int(input("Masukkan angka pertama: "))
angka2=int(input("Masukkan angka kedua: "))
angka3=int(input("Masukkan angka ketiga: "))
pernyataan= "Angka terbesar adalah: "
if angka1>angka2 and angka1>angka3:
    print(pernyataan, angka1)
elif angka2>angka1 and angka2>angka3:
    print(pernyataan, angka2)
else:
    print(pernyataan, angka3)