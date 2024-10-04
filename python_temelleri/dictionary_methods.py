opelObj = {
    "marka" : "Opel",
    "model" : "Corsa",
    "yil" : 2020
}

# sonuc = opelObj["marka"]
# sonuc = opelObj.get("marka")

# for x in opelObj:  #Key değerini yazdırdık
#     print(x)

# for x in opelObj:
#     print(opelObj[x]) #Value değerini yazdırdık

# for x in opelObj.values():
#     print(x)


for x,y in opelObj.items(): #key ve value bilgilerine birlikte ulaşmak istiyorsam
    print(x,y)

sonuc = len(opelObj) #satır sayısınız verir
opelObj["renk"] = "kırmızı" #eleman ekleme

#opelObj.pop()#son satuırda eklenen silindi

#opelObj.popitem() #yıl bilgisi silindi

# del  opelObj["marka"]
#del opelObj #objeyi sildik

#opelObj.clear() #tüm sözlüğü sildik


obj = opelObj.copy()  #Yeni bir objeyi kopyalamak

obj = opelObj #tutuldukları yeri referans olarak aktarıyoruz
obj["marka"] = "mazda" #artık value olarak "mazda" yazacak

opelObj.update({
    "marka" : "bmw",
    "renk" : "siyah"
})

print(obj)


print(sonuc)
