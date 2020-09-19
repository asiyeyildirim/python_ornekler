"""
#Girilen Sayının Tek veya Çift Olduğunu Söyleyen Program
sayi=input('Sayı:')
if (int(sayi)%2==0):
    print("Sayı Çift")
else:
    print("Sayı Tek")
"""

#String Metotları Örnek

site = "http:/www.sadikturan.com"
course = "Python Kursu: Baştan Sona İleri Seviye Python"

#sitedeki http kısmını silin
result = site.lstrip('/:htp')
print(result)