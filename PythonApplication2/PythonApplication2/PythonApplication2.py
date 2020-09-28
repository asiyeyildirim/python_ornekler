"""
# Python'da Liste İşlemleri

#1  diziyi ve dizi eleman adedini ekrana yazdırma
il=["istanbul","izmir","antalya","ankara"]
print(il)
adet=len(il)
print(adet)


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

#Listeden eleman silme işlemleri

#remove ile listede ilk bulduğu elemanı siler
kisi=["ali","ahmet","veli"]
print(kisi)
kisi.remove("ahmet")
print(kisi)

#pop ile listede indexe göre silme işlemi yapılır

kisi=["ayse","kubra","meltem"]
print(kisi)
kisi.pop(1)
print(kisi)
kisi.pop()
print(kisi)

#del ile silme
kisi=["burak","ali","hakan"]
print(kisi)
del kisi [0:2]
print(kisi

#clear ile silme işleminde tüm dizi silinir
kisi=["yeliz","ali","burak","ayşe"]
print(kisi)
kisi.clear()
print(kisi)



#Count metodu bir elemanın listede kaç defa geçtiğini öğrenmek için kullanılır

meyve= ["armut","elma","erik","üzüm","şeftali","erik","çilek"]
print(meyve.count("erik"))


#Boş Küme tanımlama
kume= set()
print(type(kume))
print(kume)
""" 
#Listeyi kümeye dönüştürme
liste={10,20,"aysu","elif","hande",15,20}
kume=set(liste)
print(kume)