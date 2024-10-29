isimler = ["Ahmet", "ali", "Çınar", "DeNiz "]
string = "Hello 12345 World"
yıllar = [1983,1999,2008,1956,1986]
dereceler = [20,5,15,-2,0,-6]

#1- "1-100" arasındaki sayılardan 12'e tam bölünebilen sayı listesi oluşturun.
sayilar = [sayi for sayi  in range(1,101) if sayi%12 == 0 ]
sayilar = [sayi for sayi in range(1,101) if sayi %3 ==0 if sayi %4 ==0 ]
print(sayilar)

#2- isimler listesindeki her ismi küçük harfe çevirip tersten yazdırınız.
harfler = [harf.lower()[::-1] for harf in isimler] #slicing ile tersten yazdırdık
print(harfler)

#3- verilen "string" içindeki  rakamları içeren bir liste oluşturunuz.
rakamMi = [stringmi for stringmi in string if stringmi.isdigit()]
print(rakamMi)

#4- "yıllar dizisindeki her doğum yılı için yaş bilgisini içeren bir liste oluşturunuz.
yas = [2024-yaslar for yaslar in yıllar]
#veya
import datetime
simdi = datetime.datetime.now().year
yas = [simdi-yaslar for yaslar in yıllar]
print(yas)

#5- "dereceler" listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma tehkiesi yazınız.
tehlike = ["buzlanma tehliesi var" if derece < 0  else "buzlanma tehlikesi yok" for derece in dereceler ]
print(tehlike)