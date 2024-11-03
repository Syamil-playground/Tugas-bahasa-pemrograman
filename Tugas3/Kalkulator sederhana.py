def kalkulator():
    # Meminta input dari pengguna
    angka1 = float(input())
    operator = input("+/-/x/: =")
    angka2 = float(input())

    # Menghitung hasil berdasarkan operator yang dipilih
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "x":
        hasil = angka1 * angka2
    elif operator == ":":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            return "Error: Pembagian dengan nol tidak diperbolehkan."
    else:
        return "Error: Operator tidak valid."

    # Menampilkan hasil
    return f"Hasil: {hasil}"

# Memanggil fungsi kalkulator dan mencetak hasilnya
print(kalkulator())
