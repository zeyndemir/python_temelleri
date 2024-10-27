isim = "Zeynep DEMİR"
harfler = []
#isim = isim.lower() #farklı bir değişkene geri atamadığın takdirde isimdeki harfler küçültülse de kaydedilmiyor

for harf in isim :
    harf= harf.lower()
    if harf == "e":
        continue
    harfler.append(harf)
print("harfler: ",harfler)

letters = []
for letter in isim:
    if letter == "E":
        break
    letters.append(letter)

print("letters :",letters)


"""SONSUZ DÖNGÜ"""
# i = 0
# while i < 8:
#     if i==6:
#         continue # i'yi artırmadan başa dönüyor. i'yi artıramadığı için asla 8 olamadığından sonsuz döngü oluştu.
#     print(i)
#     i +=1


i = 0
while i < 8:
    i +=1
    if i==6:
        continue
    print(i)

print("sonsuz döngüye girmedi ve gerçekten bitti bu defa")

#1-100 arasındaki çift sayılar toplamı

i =1
toplam = 0

while i<=100:
    i += 1
    if (i-1)%2 ==1 :
        continue

    toplam += (i-1)

print(f"1 ile 100 arasındaki çift sayıların toplamı = {toplam}")

#veya direk i'yi sıfırdan başlatabilirdim. Fazla karmaşıklaştırdım.

