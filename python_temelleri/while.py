# sayilar = [4,6,9,10,35,57,89,125,244]
#
# #1: sayilar listesini while ile ekrana yazdırın.
#
# i=0
# while i<len(sayilar):
#     print(sayilar[i])
#     i += 1
#
# #while sayilar:
# #   print(sayilar.pop()) // listenin sonundan başlaytarak tüm sayılar listesini yazdırır
#
 #3- Bailangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayı değerlerini ekrana yazdırın
baslangic = int(input("başlangoç değerini giriniz."))
bitis = int(input("bitis degerini giriniz"))
deger = baslangic +1

while deger < bitis:
    if deger %2==1:
        print(deger)

    deger += 1


# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

sayi = 100
while sayi >= 1 :
     print(sayi)
     sayi -= 1

#4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekiilde yazdırınız.

sayilar = []
i =0

while (i<5):
    sayi = int(input(i,".sayiyi giriniz"))
    sayilar.append(sayi)
    i += 1

sayilar.sort() #listeyi sıraladı
print(sayilar)

