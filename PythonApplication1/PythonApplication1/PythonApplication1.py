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
"""
