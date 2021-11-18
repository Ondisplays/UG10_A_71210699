#Judul
print("############################")
print("Kalkulator Advance Sederhana")
print("############################")

print("""1. Menghitung sisa hasil bagi
2. Membulatkan ke bawah hasil pembagian
3. Mencari akar kubik sebuah bilangan """)

#Input

menu_number = int(input("Masukan menu yang anda pilih: "))

#Hasil

if menu_number == 1:
    n1 = float(input("Masukan bilangan yang ingin dibagi: "))
    n2 = float(input("Masukan bilangan pembagi: "))

    a1 = n1 % n2

    print("Sisa hasil bagi " + str(n1) + " dibagi dengan " + str(n2) + " adalah " + str(a1))
elif menu_number == 2:
    n3 = float(input("Masukan bilangan yang ingin dibagi: "))
    n4 = float(input("Masukan bilangan pembagi: "))

    a2 = n3 // n4

    print("Hasil pembagian " + str(n3) + " dibagi dengan " + str(n4) + " dibulatkan kebawah adalah " + str(a2))
elif menu_number == 3:
    n5 = float(input("Masukan bilangan yang ingin dicari akar kubiknya: "))

    a3 = (n5 **(1/3))

    print("Akar kubik dari " + str(n5) + " Adalah " + str(a3))
else:
    print("Menu yang anda pilih tidak tersedia")
