sayilar = [1,5,15,35,57,72]

#  #1- sayilar listesindeki her bir elemanı yazdırın.
# for sayi in sayilar:
#      print(sayi)
#
#
# #2- Sayilar listesindeki hangi sayilar 5 in katidir?
#
# for sayi in sayilar:
#     if sayi % 5 == 0:
#         print(sayi)

#3- Sayilar listesinde sayıların toplamı kaçtır?
i =0
for sayi in sayilar:
    i = i + sayi

print(i)

#4- Sayilar listesindeki çift sayilarin karesini aliniz.
for sayi in sayilar:
    if sayi%2 ==0:
        print(sayi**2)




urunler = ["iphone 8","iphone X","iphone XR","Samsung S10", ]
#5- Urunler listesindeki tüm urunlerin 2. karakterlerini ekrana yazdırın.

for urun in urunler:
    print(urun[1])


#6- urunler listesinde içinde iphone geçen kaç urun vardir?
for urun in urunler:
    if "iphone " in urun:
        print(urun)