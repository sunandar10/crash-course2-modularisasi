"""
program menghitung luas segitiga
luas_ segitiga = alas x tinggi / 2
"""
print('\nmenghitung luas segitiga')
alas = 10
tinggi = 6
luas_segitiga = (alas * tinggi / 2)
print(f'luas sebuah segitiga dengan alas = {alas} dan tinggi = {tinggi} adalah {luas_segitiga}')

print('\nmenghitung luas segitiga dengan copy paste')
alas = 20
tinggi = 2
luas_segitiga = (alas * tinggi / 2)
print(f'luas sebuah segitiga dengan alas = {alas} dan tinggi = {tinggi} adalah {luas_segitiga}')
print(luas_segitiga)

def hitung_luas_segitiga (alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga
print (f'hitung luas segitiga dengan fungsi, hasilnya {hitung_luas_segitiga(20, 2)}')

