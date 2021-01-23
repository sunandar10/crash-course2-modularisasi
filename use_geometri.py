from geometri.persegipanjang import hitung_luas_persegi_panjang, info as info_persegipanjang

from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga

print(info_segitiga())
print(f'hitung luas segitiga dari alas 10 dan tinggi 3 adalah {hitung_luas_segitiga(10,3)}')

print('\n')
print(info_persegipanjang())
print(f'hitung_luas_persegi_panjang dari panjang 10 dan lebar 3 adalah {hitung_luas_persegi_panjang(10,3)}')




print('\natau cara 2')
import geometri.segitiga
print(f'luas segitiga dari alas 10 dan tinggi 3 adalah {geometri.segitiga.hitung_luas_segitiga(10,3)}')

print('\natau cara 3')
import geometri.segitiga as gs
print(f'luas segitiga dari alas 10 dan tinggi 3 adalah {gs.hitung_luas_segitiga(10,3)}')
