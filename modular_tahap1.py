"""
Menghitung luas bangun datar
"""
print('Hitung Luas Segitiga')
alas = 10
tinggi = 6
luas_segitiga= alas * tinggi / 2
print(f"segitiga dengan alas {alas} dan tinggi {tinggi} memiliki luasi {luas_segitiga}")

print('\nHitung Luas Segitiga copas aja')
alas = 10
tinggi = 6
luas_segitiga= alas * tinggi / 2
print(f"segitiga dengan alas {alas} dan tinggi {tinggi} memiliki luasi {luas_segitiga}")

print('\nHitung Luas Segitiga dg definisi')

def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga=alas*tinggi/2
    return luas_segitiga

print(f"hitung dengan fungsi {hitung_luas_segitiga(4,5)}")
print(f"hitung dengan fungsi lagi {hitung_luas_segitiga(43,5)}")

alas=10
tinggi=22
print(f"hitung dengan fungsi lagi dah {hitung_luas_segitiga(alas,tinggi)}")
