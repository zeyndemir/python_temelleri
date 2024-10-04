#key => value
#süslü parantez

plakalar = {'kocaeli' : 41, 'istanbul': 34}
#print(plakalar['kocaeli'])

plakalar['rize'] = 53
plakalar['elazığ'] = 24

plakalar['elazığ'] = 23

print(plakalar)

ogrenciler = {
    100: {
        "ad" : "Çınar",
        "soyad" : "Turan",
        "yas" : 4,
        "notlar" : [70,80,70]
    },
    101: {
        "ad" : "Ada",
        "soyad" : "Bilgi",
        "yas" : 10
    }
}

sonuc = ogrenciler[100]
sonuc = ogrenciler[101]["ad"]

sonuc = (ogrenciler[100]["notlar"][0] + ogrenciler[100]["notlar"][1] + ogrenciler[100]["notlar"][2]) / 3

print(ogrenciler)
