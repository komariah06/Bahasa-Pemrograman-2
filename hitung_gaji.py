nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Pegawai Tetap/Honor): ").lower()
golongan = input("Masukkan Golongan (A/B/C): ").upper()

gaji = 0
bonus = 0

if status == "pegawai tetap":
    gaji = 1000000
    if golongan == "A":
        bonus = 200000
    elif golongan == "B":
        bonus = 400000
    elif golongan == "C":
        bonus = 550000
elif status == "pegawai honor":
    gaji = 750000
    if golongan == "A":
        bonus = 150000
    elif golongan == "B":
        bonus = 275000
    elif golongan == "C":
        bonus = 480000

gaji_total = gaji + bonus

print("\n=== HASIL PERHITUNGAN GAJI ===")
print("Nama       : " + nama)
print("NIK        : " + nik)
print("Status     : " + status)
print("Golongan   : " + golongan)
print("Gaji       : " + str(gaji))
print("Bonus      : " + str(bonus))
print("Gaji Total : " + str(gaji_total))