isimler = ['Ada', 'Yiğit', 'Hasan', 'Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1- "Cenk ismini listenin sonuna ekleyiniz.
isimler.append("Cenk")

# 2- 'Sena' değerini listenin başına ekleyiniz.
isimler.insert(0,"Sena")

# 3- "Yiğit" ismini listeden silin
#isimler.remove("Yiğit")

# 4- "Yiğit" isminin indeksi nedir?
print(isimler.index("Yiğit"))
#isimler.pop(index) ile silme işlemi yapabiliriz

# 5- "Beril" listenin bir elemanı mıdır?
if "Beril" in isimler:
    print("evet elemanıdır")

# 6- Liste elemanlarını ters çevirin.
isimler.reverse()
yaslar.reverse()

# 7- Liste elemanlarını alfabetik olarak sıralayınız.

isimler.sort() #sırlamak için


# 8- years(yaslar) listesini rakamsal büyüklüğe göre sıralayınız.
yaslar.sort()


# 9- str= "Iphone X, Iphone XR" karakter dizisini listeye çeviriniz.
str= "Iphone X,Iphone XR"
liste = str.split(',')
print(liste)

#10 - yaslar dizisinin en büyük ve en küçük elemanı nedir?
print(min(yaslar))
print(max(yaslar))

# 11- yaslar dizisinde kaç tane 1998 değeri vardır?
print(yaslar.count(1998))

# 12 - yaslar dizisinin tüm elemanlarını siliniz.
yaslar.clear()
print(yaslar)

# 13- kullanıcıdan alacağınız 3 adet marka bilgisini bir listede saklayınız.
m1 = input("birinci marka giriniz")
m2 = input("ikinci marka giriniz")
m3 = input("üçüncü marka giriniz")

marka_listesi = [m1,m2,m3]
print(marka_listesi)