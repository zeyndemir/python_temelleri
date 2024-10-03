"""
sayilar = [1, 3, 5, 7]

sonuc = sayilar[1]
sonuc = sayilar[3]
sonuc = sayilar[2]


diller = ['ingilizce', 'italyanca' , 'fransızca', 'türkçe']
diller[-2] = " japonca "
print(diller)

sonuc = diller + ['çince', 'latince']

if 'türkçe' in diller:
    print('mevcut')


"""

#1 - Samsung S5, S6, S7, S8" elemanlarına sahip bir liste oluşturunuz
liste = ["Samsung S5","Samsung S6", "Samsung S7", "Samsung S8"]

#2- Liste kaç elemanlıdır?
#sonuc = liste.count() hata aldık çünkü listenin eleman sayısını bulmak için len() kullanılır

sonuc = len(liste)

#3-Listenin ilk ve son elemanı
sonuc= liste[0]
sonuc = liste[1]

#4- "Samsung S4" değerini  Samsung S9 ile değiştirin
liste[0] = "Samsung S9"
sonuc = liste

#5- "Samsung S6" listenin bir elemanı mıdır?

if "Samsung S6" in liste:
    print("mevcut")

#6- Listenin -3 indeksindeki değer nedir ?
sonuc = liste[-3]

#7- Listenin ilk 2 elemanını alın.
sonuc = liste[:2]

#8- Listenin son iki elemanı yerine "Samsung S9" ve "Smaung S10" ekleyin
liste[-2:] = ["Samsung S9" , "Samsung S10"]

#9- Listenin üzerine "Iphone X" ve "Iphone XR" değerlerini ekleyin
sonuc = liste + ["Iphone X", "Iphone XR"]


#10- Listenin son elemanını silin
del liste[-1] #eleman silmek için del kullanılır
sonuc = liste


#11- Liste elemanlarını tersten yazdırınız.
sonuc = liste[::-1]


#12- Aşağıdaki verileri bir liste içinde saklayınız. ***
    #kullaniciA: Yiğit Bilgi 2010, (70,60,70)
    #KullaniciB: Sena Turan 1999,  (80,80,70)
    #KullaniciC: Ahmet Turan 1998,  (80,70,90)

kullaniciA= "Yiğit", "Bilgi", 2010, [70,60,70]
kullaniciB= "Sena", "Turan", 1999,  [80,80,70]
kullaniciC= "Ahmet", "Turan", 1998, [80,70,90]
kullanicilar = [kullaniciA, kullaniciB, kullaniciC]

for kullanici in kullanicilar:
    print(kullanici)
    print(f"{kullanici[0]} {kullanici[1]} {2024- kullanici[2]} {kullanici[3][0]}")


    ad = kullanici[0]
    soyad = kullanici[1]
    yas = 2021-kullanici[2]
    ortalama = (kullanici[3][0] + kullanici[3][1]+ kullanici[3][2]) / 3
    print(f"{ad} {soyad} {yas} {ortalama}")


