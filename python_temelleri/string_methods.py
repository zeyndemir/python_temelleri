str = "Python kursuna hoş buldum. ben Zeynep DEMİR"

print(str.upper()) #tüm harfleri büyüttük
print(str.lower()) #tüm harfleri küçülttük
print(str.title()) #Her bir kelimenin BAŞ HARFİni büyütür
print(str.capitalize()) #Sadece cümlenin ilkharfini büyütür.
print("str".islower()) #Tüm harfleri küçük harf mi diye soruyor
print("    abc ".strip()) #strip dediğimizde başındaki ve sonundaki boşluk karakterleri alınmış olur
print(str.split('.'))
sonuc1 = str.split()#her bir bşluktan kelimeleri ayırdı
print("---".join(sonuc1)) #ayrılan kelimeleri --- kullanarak (aralara koydu) birleştirdi
index = str.index('hoş')
print(index)
sonuc2 = str.startswith('P') #startswith içindeki harfle başlayıp başlamadığınız verir
print(sonuc2)
print(str.endswith('l')) #fonksiyon içindeki j-harfe itip itmediğini sorar
print(str.replace('Zeynep', 'zeyn'))# (eski değer, yeni değer) eski değeri yeni değer ile replace ederiz.
#ilk etapta replace (zeynep, zeyn) yaptın olmadı çünkü str de zeynep değil Zeynep var. Case sensitivity
sonuc = str.lower().replace(' ', '_').replace('i', 'm').replace('t', 's')
print(sonuc)
tekrar = str.count('i') #count içerisindeki elemanı kaç kere tekrarladığını verir bizlere

