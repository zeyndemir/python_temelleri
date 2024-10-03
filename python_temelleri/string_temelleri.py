
"""


name = "zeynep"
surname = "demir"
age = "23"

message = "my name is" + " " + name + " and my surname is " + surname + " i am " + age+ " years old"
print(message[-3])

#STRING SlICING

clength = len(message)

print(type(clength))
print(message[0:13])
print(message[0:12:2])
print(message[:13])
print(message[13:])
"""


#String Formatlama
"""
#print('benim adım {} '.format(name))
#print('benim adım {}{} '.format(name, surname))
#print('benim adım {0}{1} '.format(name, surname))
#print('benim adım {n}{n} '.format(n=name,s= surname))

#number = 300/800
#print('the result is {:1.4}.format(n=number)')

print(f"My name is {name} {surname} and ı'am {age} years old ")

"""

###Uygulamalr###
website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviyeye Python Programlama"

# 1- 'Kursadi' karakter dizisinde kaç karakter bulunmaktadır?
print(len(kursAdi))

#2- website içinden www karakterlerini alın
print(website[7:10])

#3- website içerisinden 'com' karakterlerini alın
print(website[-3:])

#4- kursAdi isminden ilk 15 ve son 15 karakteri alınız
print(kursAdi[:16]+kursAdi[-16:])

#5- kursAdi ifadesindeki karakterleri tersten yazdırın
print(kursAdi[::-1]) # :: dediğimizde bize tüm karakterleri verir. Ancak bunun varsayılanı birdir ama biz sağdan sola saymak için -1 i ekleriz sağa

#7- 'hello world' ifadesindeki w harfini 'W' ile değiştirin
str1= 'hello world'
print(str1[:6]+"W"+str1[7:])

#8 'abc' ifadesini 3 defa yanyana yazdırın
str2='abc'
print(str2+str2+str2)

print(str2*3) # çarpı(*) operatörü string,n tekrarlamasını sağlar

name, surname, age, job = 'Zeynep', 'DEMIR', 23, 'ogrenci'
#Yukarıda verilen ifadelerle aşa# ğıdaki ifadeyi yazdırınız
#Benim adım Zeynep DEMİR, Yaşım 23 ve mesleğim öğrenci

print(f"Benim adım {name} {surname} ve yaşım {age} mesleğim {job}")
print("benim adım " + name + " " + surname + " " + "yaşım" + " " + str(age) + " mesleğim" + job)
print("Bemim adım {0} {1}, yaşım {2} ve mesleğim {3}" .format(name, surname, age, job) )