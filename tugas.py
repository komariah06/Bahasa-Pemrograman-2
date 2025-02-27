import math

# luas segitiga
print("Menghitung Luas Segitiga ")
alas = float(input("Masukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

luas_segitiga = 0.5 * alas * tinggi
print("Luas Segitiga:", luas_segitiga)
print()

# luas persegi panjang
print("Menghitung Luas Persegi Panjang ")
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

luas_persegi_panjang = panjang * lebar
print("Luas Persegi Panjang:", luas_persegi_panjang)
print()

# luas lingkaran
print("Menghitung Luas Lingkaran ")
jari_jari_lingkaran = float(input("Masukkan jari-jari lingkaran: "))

luas_lingkaran = math.pi * (jari_jari_lingkaran ** 2)
print("Luas Lingkaran:", luas_lingkaran)
print()

# volume tabung
print("Menghitung Volume Tabung ")
jari_jari_tabung = float(input("Masukkan jari-jari tabung: "))
tinggi_tabung = float(input("Masukkan tinggi tabung: "))

volume_tabung = math.pi * (jari_jari_tabung ** 2) * tinggi_tabung
print("Volume Tabung:", volume_tabung)
print()