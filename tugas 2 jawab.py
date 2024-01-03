def jarak_gerak_lurus(kecepatan, waktu):
    jarak = kecepatan * waktu
    return jarak

kecepatan_mobil = 20  # m/s
waktu_tempuh = 30  # detik

jarak_tempuh = jarak_gerak_lurus(kecepatan_mobil, waktu_tempuh)
print(f"Jarak yang ditempuh mobil adalah {jarak_tempuh} meter.")
