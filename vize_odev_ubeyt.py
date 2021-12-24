class tarifler :
    def tarif_gir(self) :
        tarifIsmi = input("Tarıf İsmi : ")
        tarif.append(tarifIsmi)
        while True :
            tarifSatiri = input('Tarif Satırı Ekle(Satırlarınız Sonlandıysa "25" giriniz.) : ')
            if tarifSatiri == "25" :
                tarifler_listesi.append(tarif)
                tarif.append("\n")
                break
            else :
                tarif.append(tarifSatiri)


    def goster(self) :
        number = len(tarifler_listesi)
        print("Bütün Tarifler")
        for asama in tarif :
                print(asama)




def menuy() :
    while True :
        print("\Tarif Gir : 1\nTarifleri Goster : 2\n Çıkış Yap : 3 ")
        secim = input("Yapmak İstediğiniz İşlem Numarasını Giriniz: ")
        islem = tarifler()
        if secim == "1" :
            islem.tarif_gir()
        elif secim == "2" :
            islem.goster()
        elif secim == "3" :
            exit(0)
        else :
            print("Hatalı İşlem Yaptınız.")



tarifler_listesi = []
tarif = []

menuy()
