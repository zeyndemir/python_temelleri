def toplam(a,b):
    return (a+b)

def fark(a,b):
    return (a-b)

def islem(a,b,fn):
    return fn(a,b)

sonuc = islem(8,7,fark)
print(sonuc)


###### Keywords #######

#args

def toplam(*args):
    print(type(args)) #bize tuple verir
    print(args)
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(toplam(1,8,5,6,9))
print(toplam(1,4,5,74))

#kwargs

def displayUser(**kwargs):
    print(type(kwargs)) #dictionary
    for key, value in kwargs.items():
        print(value)
        print(f"{key}: {value}")
    print("\n")

isim = input("isminizi giriniz")
soyisim = input("soyisminizi giriniz")
displayUser(isim = isim, soyisim = soyisim)

def myFunc(a,b,c, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(1,2,4,8,87, kitapadı = "gazap üzümleri", yazar = "john steinbeck")
