#input

rata = float(input("Masukan nilai rata-rata UG anda: "))
tts = float(input("Masukan nilai TTS anda: "))
tas = float(input("Masukan nilai TAS anda: "))
print("=========================")

#perhitungan

hasil = ((rata*0.7)+(tts*0.15)+(tas*0.15))

print("hasil " + str(hasil))

#standar nilai
if hasil >= 85:
    print("Nilai huruf anda: A")
elif hasil >= 80:
    print("Nilai huruf anda: A-")
elif hasil >= 75:
    print("Nilai huruf anda: B+")
elif hasil >= 70:
    print("Nilai huruf anda: B")
elif hasil >= 65:
    print("Nilai huruf anda: B-")
elif hasil >= 60:
    print("Nilai huruf anda: C+")
elif hasil >= 55:
    print("Nilai huruf anda: C")
elif hasil >= 45:
    print("Nilai huruf anda: D")
else:
    print("Nilai huruf anda: E")


