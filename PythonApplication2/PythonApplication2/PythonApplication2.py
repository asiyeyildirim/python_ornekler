"""
# Python'da Liste İşlemleri

#1  diziyi ve dizi eleman adedini ekrana yazdırma
il=["istanbul","izmir","antalya","ankara"]
print(il)
adet=len(il)
print(adet)
"""

#Listeye eleman ekleme işlemleri

#append ile listenin sonuna, aynı anda bir tane olacak şekilde eleman eklenir
kisi = ["elif"]
print(kisi)
kisi.append("buse")
print(kisi)

#insert ile listenin istediğimiz yerine eleman ekleyebiliriz
kisi = ["ali"]
print(kisi)
kisi.insert(0,"ömer")
print(kisi)
kisi.insert(2,"ahmet")
print(kisi)