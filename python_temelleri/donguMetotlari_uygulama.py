#1- çarpım tablosu hazırlayınız.

for i in range (1,11):
    print("*************")
    for k in range(1,11):
        print(f"{i} x {k} = {i*k}")

#2- girilen bir sayının asal olup olmadığını kontrol ediniz.
sayi = int(input('"bir sayı giriniz'))
toplam =0
for i in range(2,sayi):
    if sayi % i == 0:
        toplam +=1
        break

#for i in range(2, sayi) döngüsünde i otomatik olarak birer birer arttırılır;
# yani i değerini döngü içerisinde manuel olarak artırmanıza gerek yoktur.
# for döngüsü her tekrarda iyi otomatik olarak sıradaki değere çeker.

if toplam == 0 and sayi !=1:
    print(f"girmiş olduğunuz {sayi} sayisi bir asal sayıdır. ")

else:
    print(f"girmiş olduğunuz {sayi} sayisi bir asal sayı değildir. ")

#Hocanın kodu

# asalmi = True
#
# if sayi==1:
#     asalmi = False
#
# for i in range(2,sayi):
#     if(sayi%i==0):
#         asalmi = False
#         break
#
# if asalmi:
#     print("sayı asaldır")
#
# else:
#     print("sayı asal değildir")
