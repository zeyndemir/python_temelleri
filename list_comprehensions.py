#[expression for item in list]

sayilar = [i for i in range(10)]
sayilar2 = [k*2+8 for k in range(1,20)]
print(sayilar2)

liste = [10,12,15,63]
sayilar3 = [i*9 for i in liste]
print(sayilar3)

isim = ["ahmet", "ayse", "ali","veli"]
ihbuyuk= [i.capitalize() for i in isim]
print(ihbuyuk)

sonuc= [str(sayi) for sayi in liste]
sonuc= [sayi.isdigit() for sayi in isim]
print(sonuc)