personel=[]

while True:
    print("::menü::")
    print("1-Ekleme")
    print("2-Listeleme")
    print("3-Arama")
    print("4-Güncelleme")
    print("5-Silme")
    print("6-Çıkış")
    print("7-Listeyi Gör")

    secim= input("Seçiminiz=")

    if secim=="6":
        print("Çıkılıyor...")
        break
    elif secim=="7":
        print(personel)
    elif secim=="1":
        ad=input("ad:")
        soyad=input("Soyad:")
        telefon=input("Telefon no:")
        eklenecek_veri={
            "ad:":ad,
            "Soyad":soyad,
            "Telefon no": telefon
            }

        personel.append(eklenecek_veri)
        print("Bilgiler eklendi...")
    elif secim=="2":
        pass
    elif secim=="3":
        pass
    elif secim=="4":
        pass
    elif secim=="5":
        pass
