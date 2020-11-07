"""
#Girilen Sayının Tek veya Çift Olduğunu Söyleyen Program
sayi=input('Sayı:')
if (int(sayi)%2==0):
    print("Sayı Çift")
else:
    print("Sayı Tek")


#String Metotları Örnek

site = "http:/www.sadikturan.com"
course = "Python Kursu: Baştan Sona İleri Seviye Python"

#sitedeki http kısmını silin
result1 = site.lstrip('/:htp')
#course harfleri küçült
result2 = course.lower()
print(result1)
print(result2)

#Listeler Örnek1
userA = ['Elif',36]
userB = ['Kara',2]
users=userA + userB
print(users)

#Listeler Örnek2 hesaplanan liste

Liste = [x**3 for x in (2,4,6)]
print(Liste)

#Listelerde işlemler
names=['Ali','Sevim','Ahmet','Eda']
years=[1998,2005,1988,1975]
names.append('Ayşe') #listenin sonuna eleman ekleme
names.insert(0,'Elif') #Belirttiğimiz indexe eleman ekleme
names.remove('Ahmet') #eleman silme işlemi
print(names)
index = names.index('Sevim') #istediğimiz elemanın indexini öğrenmek ve öğrendiğimiz indexteki veriyi silmek
names.pop(index) 

names.sort()
print(names)
min=min(years) #yıllar arasındaındaki en büyük ve en küçük değeri yazdırma işlemi
max= max(years)
print(min,max)
"""
#Atama operatörleri Örnek
x,y,z =2,5,10    #Kullanıcıdan aldığımız iki sayının çarpımı ile x+y+z toplamının farkı
numbers=1,5,7,10,6
a=int(input('1.sayı: '))
b=int(input('2.sayı: '))

result=(a*b)-(x+y+z)
print(result)