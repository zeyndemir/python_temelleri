markalar = ["opel", "bmw", "mercedes"]
index = 0

# for marka in markalar:
#     print(f"{index+1}-{marka[index]}")
#     index += 1   #markaların indeksine ulaşma ihtiyacı duyuyorsak

#enumerate : yaptığımız işlemi enumerate ile basitçe kendimiz yapabiliriz.

obj1 = enumerate(markalar)
print(type(obj1)) #enumerate in type'ını verdi
print(list(obj1))

for index, value in enumerate(markalar):
    print(index,value)


#zip
liste1 = [1,2,3,5,4,5]
liste2 = ["a","b","c","d","e","f"]
liste3 = [100,200,300,400,500]

print(list(zip(liste1,liste2,liste3)))

for item in zip(liste1,liste2):
    print(item)

for a,b,c in zip(liste1,liste2,liste3):
    print(a,b,c)