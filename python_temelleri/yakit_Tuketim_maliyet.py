#Bir aracın yakıt tipine göre (benzin, dizel) belirtilen bir mesafede ne kadar yakıt
# masrafı olduğunu  hesaplayan uygulama yapınız.

benzin = 44.31
dizel = 43.39

ortYakitTuketimi = float(input("100 km'de ortalama yakıt tüketimini yazınıt"))
yol = float(input("gidilecek yolu yazınız."))

yakitTipi = input("yakıt tipiniz nedir")

toplamYakitTuketimi = yol * (ortYakitTuketimi/100)



if(yakitTipi == "benzin"):
    toplamYakitUcreti = benzin * toplamYakitTuketimi

elif(yakitTipi == "dizel"):
    toplamYakitUcreti = dizel * toplamYakitTuketimi


else :
    print("yanlış yakıt ücreti girdiniz.")


print(toplamYakitUcreti)
