# 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri işe buldurmaya çalışın
# "random moodülü" için "python random" şeklinde arama yapın.
# 100 üzerinden puanlama yapın. Her soru 20 puan
# Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.

# Benim kodum
import random

hak = int(input("haç hakkınız olsun istiyorsunuz"))
puan = 0

sayi = random.randint(1,10)

for i in range(hak,0,-1):
    tahmin = int(input("tahmininizi giriniz."))

    if tahmin == sayi:

        puan = i*100/hak
        print("tahmininiz doğru puanınız: ",puan)
        break

    elif tahmin < sayi :
        print("tahmininiz sayidan küçüktür .Daha büyük bir sayı tahmin ediniz.")

    else:
        print("tahmininiz sayıdan büyüktür. Daha küçük bir sayı tahhmin ediniz.")

    if i > 1:
        print("kalan tahmin hakkınız",i-1)

    else:
        print("tahmin hakkınız kalmadı")

# #hocanın kodu
# import random
# sayi = random.randint(1,10)
# can = int(input("kç hakkınız olsun istersiniz."))
# hak =can
# sayac = 0
#
# while hak > 0:
#     hak -=1
#     sayac += 1
#     tahmin = int(input("tahmin"))
#
#     if sayi == tahmin :
#         print(f"tebrikler {sayac} defada bildiniz. Toplam puanınız {100-(100/can)*(sayac-1)}")
#         break
#     elif sayi > tahmin:
#         print("yukarı")
#
#     else:
#         print("aşağı")
#
#     if hak == 0:
#         print(f"hakkınız bitti. tutulan sayı {sayi}")