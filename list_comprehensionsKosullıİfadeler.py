
#Dongu ile
sayilar = [1,5,8,9,15,44]
sonuc = []

for  sayi in sayilar:
    if sayi%2==0:
        sonuc.append(sayi)

print(sonuc)

sonuc2 = [sayi for sayi in sayilar if sayi %3 == 0]
sonuc = [sayi if sayi %2 == 0 else "tek sayi" for sayi in sayilar]
#sadece if varken önce for yazılırdı else de varsa if-else + for
print(sonuc2)

fiyatlar = [1000,3000,5000,0,4000]
vergiler= []

for fiyat in fiyatlar:
    if(fiyat > 0):
        vergiler.append(fiyat*1.18)


vergiler = [fiyat*1.18 for fiyat in  fiyatlar if fiyat > 0]
vergiler = [fiyat*1.18 if fiyat > 0 else "vergi alinmaz" for fiyat in fiyatlar]
print(vergiler)

ekleme = []
for x in range(1,4):
    for z in range(1,3):
        ekleme.append((x,z)) #appendi iki adet parantezin içine almayımnca, tek parantezde hata verdi
print(ekleme)

#iç içe comprehension
sonuc = [(x,y) for x in range(3) for y in range(3)]