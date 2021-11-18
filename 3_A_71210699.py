#input

skuy = input("Mendatar/Menurun?: ")

#hasil

if skuy == "Mendatar":
    skidi = int(input("Masukan kolom: "))
    print("#" * skidi)
elif skuy == "Menurun":
    pu = int(input("Masukan baris: "))
    print("*\n" * pu)
else:
    print("Pola tidak dikenali")

