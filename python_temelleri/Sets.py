# sets : dictionatry gibi süslü parantez kullanırız ancak value key değerşleri yoktur
#sıralanması indexlenmesi önemli değildir
#Setler İNDEKSLENEMEZ, sıralanamaz
#İndexlenmediği için daha hızlıdır

meyveler = {"elma", "kiraz"}
# print(meyveler[0]) indekslenemez. hata verir
sonuc = "elma" in meyveler #true verir


meyveler.add("karpuz") #karpuz ekelenebilir ancak hangi sırayla nereye ekleneceğini bilemeyiz
meyveler.update(["çilek", "muz"]) #birden fazla meyve eklemesi yuaptık meyveler listemize

sonuc= len(meyveler)
meyveler.remove("karpuzz") #keyError veriri karpuz var kapuzz yok
meyveler.discard("karpuzz") #kapuzz yoksa hata vermez. remove da mevzutsa sler uoksa hata verirdi
sonuc = meyveler

sonuc = meyveler.pop() #her sferinde farklı bir elemanı siler çünkü bir indeks olmadığı için sonuncu eleman gibi br şey de söz konusu değildir.

sebzeler = {"bezelye", "soğan"}

meyveler.union(sebzeler)  #meyveler ve sebzeleri birleştirdi






for x in meyveler:
    print(x)

print(sonuc)


