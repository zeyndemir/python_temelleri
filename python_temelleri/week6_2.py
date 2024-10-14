import numpy as np

#########Ödev1#######
"""

dizi = np.array([5,3,9,87])

print(dizi)
print(dizi.size)
print(dizi.ndim)
print(dizi.dtype)

"""
#########Ödev2#############

array2 =  [[1,2,5,6], [4,5,8,9]]
array3 = [[10,20,30,40], [50,60,80,90], [11,12,13,14]]

print((len(array2[0])+len(array2[1])))
ar3_elemansayisi = (len(array3[0])+len(array3[1]) + len(array3[2]))
print(f"array3 eleman syaısı= {ar3_elemansayisi}")

eleman = 8
indeks = [sublist.index(eleman) for sublist in array2 if eleman in sublist]
print(f"5'in {eleman}  indeksi: {indeks}")

slicing = [satir[2:4] for satir in array3[:2]]
print(f"slicing : {slicing}")

############# Odev3##################

num_array = np.array([5,3,9,87])
num_array2 = np.array([[1,2,5,6], [4,5,8,9]])
num_array3 = np.array([[10,20,30,40], [50,60,80,90], [11,12,13,14]])

print(num_array[2])
print(num_array2[1,3])
print(num_array3[2,3])

print(num_array[0:2])


############Ödev4############

birler=np.ones(5, dtype=int)
sifirlar = np.zeros(10, dtype=int)

print(birler)
print(sifirlar)

birlesme = np.concatenate((birler, sifirlar))
print(birlesme)