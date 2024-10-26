urunler = [
    {"name:": "iphone 8", "price": "4000"},
    {"name:": "iphone 8 Plus", "price": "5000"},
    {"name:": "iphone X", "price": "6000"},
    {"name:": "iphone XR", "price": "7000"},
    {"name:": "iphone 11", "price": "8000"},
    {"name:": "samsung s10", "price": "6000"}
]

#1- tüm ürünlerin bilgilerini listeleyiniz.
for urun in urunler:
    print(urun.values())

#2- Ürünlerin Fiyatları Toplamı nedir?
toplam = 0
for urun in urunler:
    toplam = toplam + int(urun["price"])

print(toplam)

#3- Urunlerden fiyatı en fazla 600 olan ürünleri gösteriniz.
for urun in urunler:
    if int(urun["price"]) <= 6000:
        print(urun)

#4- Kullanıcıdan alınan anahtar kelimeyi içeren ürünlwri bulunuz.

kelime = input("lütfen aramak istediğiniz kelimeyi giriniz")

for urun in urunler:
    if kelime.lower() in urun["name:"].lower() :
        print(urun)


#Hocanın kodu
# kelime = input("anahtar kelimeleri giriniz")
#
# for urun in urunler:
#     if (urun["name"].find(kelime.lower()) > -1):
#         print(urun["name"])
