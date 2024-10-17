#1- Girilen 2 sayıdan hangisi daha büyüktür?
#a = input("a:")
#b = input("b:")
#
#print(f" a büyüktür b ifadesi: {a > b}")
#print(f" b büyüktür a ifadesi: {a < b}")
#print(f"a eşittir b ifadesi : {a==b}")

#2- Girilen bir sayının tek mi çift mi olduğunu yazın
#a = input("a:")
#print(f"a ifadesi tektir {int(a)%2 == 1}")
#print(f"a ifadesi çifttir {int(a)%2 == 0}")

#3- Girilen bir sayının negatif pozitif olduğunu yazdır.
a =int(input("a: "))
print(f"a ifadesi pozitiftir : {a > 0}")
print(f"a ifadesi negatiftir: {a<0}")

#4- Kullanıcıdan 2 vize(½60) ve final (½40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 üstüyse geçti değilse kaldo yazdırın
vize1 = int(input("ilk vizeyi giriniz: "))
vize2 = int(input("ikinci vizeyi giriniz: "))
final = int(input("final notunuzu giriniz"))

ort = (vize1 + vize2) *(60/100)  + (final*40/100)
print(f"dersten geçmeniz: {ort >= 50}")



#5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
_email = "zeynep@mail.com"
_parola = "1234"

email = input("email: ")
parola = input("parola: ")

isEmail = (email.lower().strip() == _email)
isParola = (parola.strip()==_parola)

print(f"mail doğruluğu {isEmail} parola doğruluğu {isParola}")


#print(f"email bilginiz : {email =='zeynep@mail.com'} parolanız: {parola == '12345'}")