website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviyeye Python Programlama"



# 1- ' Hello World ' karakter dizisinin baş ve sondaki buşluk karakterlerini silin
cevap1 = " Hello World ".strip()
print(cevap1)
" Hello World ".lstrip() #Soldan siler sağ taraftaki karakterler kalır
" Hello World ".rstrip() #Sağ taraftaki boşuklar silinir sol taraf kalır

#2 -  içindeki saikturan bilgisi haricindeki her karakteri silin
silinmis='www.sadikturan.com'.strip('wcom.')
print(silinmis)

#3 - 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın
print(kursAdi.lower())

#4- 'website' içinde kaç tane a karakteri vardır? (count('a'))
print(website.count('a'))
print(website.count('www',0,10)) # 0'dan başla 10'a kadar say www bul var mı

#5- 'website' 'www' ile başlayıp com ile bitiyor mu ?
print(website.startswith('www'))
print(website.endswith('com'))

#6- 'website' içinde '.com' ifadesi var mı?
sonuc = website.find('com') #bulmak için kullanırız olmasaydı -1 dödürecekti
sonuc = website.find('com', 0,10)
sonuc = website.rfind('com') #sağda var mı? baladığı indeksi dödürür
sonuc = website.find('Python')

# find() ve index() farkı istenilen şeyi bulamadıklarında döndürdükleridir. biri value error dönderirken = index find = -1 dönderir

sonuc = kursAdi.index('Python')
sonuc = kursAdi.rindex('Python')

#7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
print(kursAdi.isalpha()) #hepsi alfabetik semboller mi
print("123".isdigit()) #hepsi sayı mı

#8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

print('Contents'.center(50,'*')) #Verilen stringi ortalasın sağına ve soluna 50 şer tane * koysun
print('Contents'.ljust(50,'*')) #Verilen strini ortalasın  soluna 50 şer tane * koysun
print('Contents'.rjust(50,'*')) #Verilen strini ortalasın sağına 50 şer tane * koysun

#9- KursAdi karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
print(kursAdi.replace(' ','-'))

#10- 'Hello World' karakter dizisinin 'World' ifadeesini 'there olarak değiştirin
print('hello world'.replace('world','there'))

#11- 'kursAdi' karakter dizisini boşluk karakterlerinden ayırın
print(kursAdi.split())