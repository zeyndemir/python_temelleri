#Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
# *** urun sayısını kullanıcıya sorun
# *** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun
# *** urun ekleme işlemi bittiğinde urunleri ekrana while ile listeleyin.

#AŞAĞIDAKİ YORUM SATIRI HATALI EKSİK KODDUR.

# urunler = {}
# sayi = int(input("kaç ürün listelenmesini istediğinizi giriniz."))
# i=0
#
# while i< sayi:
#     urunler["urunAdi"] = input("ürünün adını giriniz")
#     urunler["fiyat"] = input("ürünün fiyatını giriniz.")
#     i += 1
#
# print(urunler)

i =1
sayi = int(input("kaç adet ürün listelenmesini istiyorsunuz"))
urunler =[]

while ( i <= sayi):
    urunAdi = input("ürünün adını giriniz")
    fiyat = input("ürünün fiyatını giriniz.")
    urunler.append({
        "urunAdi" : urunAdi,
        "fiyat" : fiyat
    })
    i+=1



# for urun in urunler:
#     print(f'ürünün adı: {urun["urunAdi"]}, ürünün fiyatı: {urun["fiyat"]}')

a =0
while (a<len(urunler)):
    print(f'ürünün adı: {urunler[a]["urunAdi"]}, ürünün fiyatı: {urunler[a]["fiyat"]}')
    a+=1