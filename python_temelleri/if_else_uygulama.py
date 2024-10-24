#1- Girilen bir sayının 50-100 arasındaolup olmadığını kontrol ediniz.
"""
sayi = int(input("bir sayı giriniz."))
if sayi >50 and sayi<=100:
    print("sayi 50 ile 100 arsındadır")

else:
    print("sayi 50 ile 100 arsında değildir.")
"""
"""
#2- girilen sayının pozitif  tek tam sayı olup olmadığını kontrol ediniz.
sayi = int(input("bir sayı giriniz."))
if sayi > 0 and sayi %2==1:
    print("girdiğiniz sayi pozitif ve tem tam sayıdır")

#Username ve parola bilgileri ile giriş kontrolü yapınız.
_username = "zeynep"
_parola = "parola"

username = input("kullanıcı  adı giriniz.")
parola = input("parolanızı giriniz.")

if _username == username and _parola==parola:
    print("hoşgeldiniz.")



"""
#Girilen 3 sayiyi büyüklük olarak karşılaştırınız:
"""
x= int(input("birinci sayiyi griniz."))
y = int(input("ikinci sayiyi griniz."))
z = int(input("üçüncü sayiyi griniz."))




if (x>y and not x==y) and (x>z and not x==z ) :
    if y> z and not y==z:
        print("x > y> z")
    elif x ==z :
        print("x = z> y")


elif (y>x and not ) and (x>z and not x==z ):
    if x>z and not x==z:
        print(" y > x > z ")

"""

vize1 = float(input("1. vizeyi giriniz."))
vize2 = float(input("ikinci vizeyi giriniz."))
final = float(input("final notunuzu giriniz."))

ort = ((vize1 + vize2) /2)*0.4 + (final * 0.6)

if final >= 70:
    print("dersi geçtiniz.")

elif final >= 50 and ort >= 50:
    print("dersi geçtiniz")

else:
    print("dersten kaldınız")


ad = input("adınızı giriniz")
boy = float(input("boyunuzu m cinsinden giriniz"))
kilo = float(input("kilonuzu giriniz"))

indeks = kilo / boy**2

if indeks <=18.4:
    print("zayıfsınız")

elif indeks <= 24.9:
    print("normal kilodasınız.")

elif indeks <= 29.9:
    print("kilolusunuz")

else:
    print("obezsiniz")