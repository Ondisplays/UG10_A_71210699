#Input

artikel = input("Masukan artikel yang ingin dipindai: ")
klub = input("Masukkan nama klub favorit anda: ")
skor = input("Masukkan skor yang ingin dicari: ")

#Mencari

klub1 = klub in artikel
skor1 = skor in artikel

#Hasil

if(klub1 and skor1):
    print("Hasil pencarian ditemukan")
elif(klub1 and not skor1):
    print("Hanya kata " + klub + " yang ditemukan pada artikel ini")
elif(not klub1 and skor1):
    print("Hanya skor "+ skor + " yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian " + klub + " dan " + skor + " tidak ditemukan")

