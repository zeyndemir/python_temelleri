# 1- 3 ürün bilgisini (id, ad, fiyat) kullanıcıdan aldığınız bilgilerler dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin (bu id nin key olması anlamınıa geliyor.)
"""
id = input("ürün id sini giriniz")
ad = input("ürünün adını giriniz")
fiyat = input("ürünün fiyatını giriniz.")

dict = {
    "urun1" :{
        "ad" : ad,
        "id" : id,
        "fiyat" : fiyat
    }

}
print(dict)


ürünler = {}

print("girdiğiniz ürünün id'si :" + dict["urun1"]["id"])
"""
id = input("ürün id sini giriniz")


urunler = {id : {
    "ad" : "çanta",
    "fiyat" :100
    }

}

print(f" id : {id} ürün adı: {urunler[id]['ad']} urun fiyatı : {urunler[id]['fiyat']} ")