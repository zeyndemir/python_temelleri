# #1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# #ehliyet alma kouşulu en az 18 yaş ve eğitim durumunun lise ya da üniversite mezuniyeti olmasıdır.
#
# isim = input("lütfen asınızı giriniz")
# yas = int(input("lütfen yaşınızı giriniz."))
# egitimDurumu = input("eğitim durumunuzu giriniz.")
#
# if yas >= 18 and (egitimDurumu == "lise" or egitimDurumu == "üniversite"):
#     print(f"sayın {isim} ehliyet alabilirsiniz")
#
# else:
#     print(f"sayın {isim} maalesef ehliyet almak için gereklilikleri taşımıyorsunuz.")
#
#
# #2- Bir öğrencinin 2 yazılı bir sözlü notulku alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
# # 0-24 => 0
# #25-44 => 1
# #45-54 => 2
# #55-69 => 3
# #70-84 => 4
# #85-100 => 5
#
# yazili1 = float(input("lütfen ilk yazılı notunuzu giriniz"))
# yazili2 = float(input("lütfen ikinci yazılı  notunuzu giriniz"))
# sozlu = float(input("lütfen  sözlü notunuzu giriniz"))
#
# ortalama = (yazili1 + yazili2+ sozlu) /3
#
# if ortalama >=0 and ortalama <= 24:
#     print("not aralığınız 0'dır")
#
# elif ortalama >=25 and ortalama <= 44:
#     print("not aralığınız 1'dir")
#
# elif ortalama >=45 and ortalama <= 54:
#     print("not aralığınız 2'dir")
#
# elif ortalama >= 55 and ortalama <= 69:
#     print("not aralığınız 3'tür")
#
# elif ortalama >=70 and ortalama <= 84:
#     print("not aralığınız 4'türr")
#
# elif ortalama >=85 and ortalama <= 100:
#     print("not aralığınız 5'tir")
import datetime
#Trafiğe Çıkış tarihi alına bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
# 1.Bakım => 1.yıl
# 2.Bakım => 2.yıl
# 3.Bakım => 3. yıl

#Süre hesabını alınan gün ay yıl bilgisine göre hesaplayınız.
#datetime modülünü kullanmanız gerekmektedir.

#(simdi) - (2018/8/1) => gün

import datetime as dt

tarih = input("aracınızın trafiğe çıkmatarihini giriniz (2019/7/11)")
tarih = tarih.split('/')


simdi = dt.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0],tarih[1],tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

if gun<=365:
    print('1.serviste bakımı')

elif( gun>365 ) and (gun <= 365*2):
    print("2.servis bakımı")
elif gun>= 365*2 and gun<=365*3:
    print("3.servis bakımı")

else : print("hatalı bilgi girdiniz.")