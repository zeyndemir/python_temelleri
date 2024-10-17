a, b, c = 2,5,10

#1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c farkı nedir?
ilk_deger = input("ilk degeri giriniz")
ikinci_deger = input("ikinci değeri giriniz.")

sonuc = (ilk_deger*ikinci_deger)-(a*b*c)

#2- c'nin b'ye kalansız bölümünü hesaplayınız.
sonuc = c//b

#- (a,b,c) toplamının mod ^' neir ?
sonuc = (a+b+c)%3

#4- b'nin a. kuvvetini hesaplayınız.
sonuc = b**a

#sayilar = 1,5,10,3
#5- a, *b, c = sayilar işlemine göre c'nin küpü kaçtır?
sayilar = 1,5,7,10,3
a, *b, c = sayilar
print(c**3)


#6- a,*b, c = sayilar işlemine göre b'nin değerleri toplamı kaçtır?
print(b[0] + b[1] + b[2])










print(sonuc)