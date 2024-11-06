#Kendisine gönderilen bir kelimeyi belirtilen tekrar sayısı kez ekranda yazınız
import random


# def tekrarla():
#     kelime = input("Tekrarlanmasını istediğiniz kelimeyi giriniz.")
#     tekrar = int(input("Kelimenin kaç defa tekrarlanmasını istiyorsunuz"))
#     for i in range(tekrar):
#         print(kelime)
#
# tekrarla()


# 2- Dikdörtgenini alan ve çevresini hesaplayan fonsksiyonu yazınız.
#
# def dıkdortgen(uzun,kisa):
#     alan = uzun* kisa
#     cevre = (uzun+kisa) * 2
#
#     return f"dikdörtgenin alanı : {alan}, dikdörtgenin çevresi: {cevre}"
#
#
# uzunKenar = int(input("dikdörtgenin uzun kenarını giriniz."))
# kisaKenar = int(input("dikdörtgenin kısa kenarını giriniz."))
#
# print(dıkdortgen(uzunKenar,kisaKenar))

# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. random modülü
# def tahmin():
#     sayi = random.randint(0,1)
#     if sayi == 1:
#         print("Tura")
#
#     else:
#         print("Yazı")

#Kendisine gönderilen 2 sayi arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
# def asalSayiBul(sayi1,sayi2):
#     asalSayilar = []
#     sayi=2
#     for i in range(sayi1,(sayi2+1)):
#         for k in (sayi,i):
#
#             if i % k != 0 and sayi!= 1:
#                 asalSayilar.append(i)
#
#     return asalSayilar
#
# a = int(input("ilk sayıyı giriniz"))
# b = int(input("ilk sayıyı giriniz"))
#
# print(asalSayiBul(a,b))


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonskiyonu yazınız.

def tamBolenBul(sayi):
    tam_bolenler=[]

    for i in range(1,(sayi+1)):
        if sayi % i == 0 :
            tam_bolenler.append(i)

    return tam_bolenler

a = int(input("sayiyi giriniz"))
print(tamBolenBul(a))












