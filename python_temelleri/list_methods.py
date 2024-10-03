sayilar = [1,5,8,9,3,45]
harfler = ["a", "b", "e", "s", "a", "y"]

sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = max(harfler)


####EKLEME#####
sayilar.append(10)
sayilar.insert(3,5) #3 numaralı indekse 5 sayısını yerleştirdik
sayilar.insert(-1,50)
sayilar.insert(len(sayilar), 150)    #sayilar dizisinin sonuna 150 değerini ekledik


####SİLME#####
sayilar.pop()#listenin en sonundan bir elemna siler
sayilar.pop(2) #Silmek istediğiniz İNDEKSİ vererek belirli bir indeksteki değeri de silebilirsiniz
harfler.remove('y')
sayilar.remove(45) #slmek istediğiniz DEĞERİ  vererek silbilirsiniz


#####SIRALAMA####

sayilar.sort()
harfler.sort()
sayilar.reverse() #artan değil azalan şekilde sıralar

print(sayilar.count(5))  #kaç tane 5 var
print(harfler.count('a'))

print(harfler.index("a")) #listede istediğimiz değerin yerini , nindeksini öğrenmemizi sağlar


sayilar.clear() # tüm listeyi siler temizler
sonuc = sayilar



print(sonuc)