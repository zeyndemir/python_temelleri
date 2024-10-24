#Girilen bir sayının 50-100 arasında olupş olmadığını kontrol ediniz.
#sayi = int(input("bir sayı giriniz."))
#print(50 <sayi <100)

#Girilen bir sayının pozitif tek tam saı olup olmadığını kontrol ediniz.
#sonuc = sayi>0 and sayi%2==1


#Username ile parola bilgileri ile giriş kontorlü yapınız.
#username = input("kullanıcı adı giriniz")
#parola = input("parola giriniz.")
"""
_username = "zeynep"
_parola = "parola"

print(username == _username and parola ==_parola )

#Girilem 3 sayıyı büyüklük olarak karşılaştırınız.
sayi1 = input("ilk sayı:")
sayi2 = input("ikinci sayi:")
sayi3 = input("3. sayi")

sonuc = (sayi1>sayi2) and (sayi1>sayi3)
print("sayi1 en büyük",sonuc)
sonuc = (sayi2>sayi1) and (sayi2>sayi3)
print("sayi2 en büyük",sonuc)
sonuc = (sayi3>sayi1) and (sayi3>sayi2)
print("sayi3 en büyük",sonuc)


#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alığ prtalamyı hesaplayınız.
#Eğer ortalama 50 üstüyse geçti değilse kaldı yazın
#a) Ortalama 50 altında olsa bile final 50 den büyük olmalıdr.
#b) finalden 70 alındığında ortalamanın önemi olmasın

vize1 = int(input("vize giriniz: "))
vize2 = int(input("vize giriniz: "))
final = int(input("final giriniz: "))

print("geçme durumunuz : " , final> 50)

ort =  ((vize1+vize2)/2)*6/10 + (final*40/10)
sonuc = ort > 50 and final >= 50
print("dersten geçtiniz mi : ", sonuc)
print( sonuc or final >= 70)
"""

#6- Kişinin ad, kilo ve boy bilgilerini alıp kilo endeksini hesaplayınız.
# formül: (Kilo/boy uzunluğunun karesi)
# Aşağıki tabloya göre kişi hangi gruba girmektedir.
# 0-18.4 => Zayıf
# 18.5-24.9 =>Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman(Obez)

ad = input("adınızı giriniz: ")
kilo = float(input("Kilonuzu giriniz:"))
boy = float(input("boyunuzu giriniz: "))

indeks= kilo/boy**2

print(f"{ad}  zayıfsınız : ", 0<= indeks <= 18.4)
print(f"{ad} normal kilodasınız : ", 18.5<= indeks <= 24.9)
print(f"{ad} fazla kilolusunuz : ", 25<= indeks <= 29.9)
print(f"{ad} obezsiniz : ", 30<= indeks)


