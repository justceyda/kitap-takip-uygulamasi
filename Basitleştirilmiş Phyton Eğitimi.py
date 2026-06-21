import json

kitaplar = []
dosya_adi = "kitaplar.json"

def dosya_kaydet():
    with open(dosya_adi, "w", encoding="utf-8") as f:
        # ensure_ascii=False Turkce karakterlerin bozulmasini onler, indent=4 ise dosyayi duzgun gosterir
        json.dump(kitaplar, f, ensure_ascii=False, indent=4)
    print("Kitaplar basariyla kaydedildi.")

print("Kitap Takip Uygulamasina Hos Geldiniz!")

# Program acilisinda JSON dosyasini okuyoruz
try:
    with open(dosya_adi, "r", encoding="utf-8") as f:
        kitaplar = json.load(f)
    print("Kitaplar basariyla yuklendi.")
except FileNotFoundError:
    print("Kayit dosyasi bulunamadi. Yeni bir liste olusturuldu.")

# Ana dongu
while True:
    print("\n--- MENU ---")
    print("1- Listele")
    print("2- Yeni kitap ekleme")
    print("3- Durum guncelleme")
    print("4- Kitap silme")
    print("5- Cikis")
    
    secim = input("Seciminiz (1-5): ")

    if secim == "1":
        if len(kitaplar) == 0:
            print("Henuz kayitli kitap yok.")
        else:
            print("--- KITAP LISTESI ---")
            for i in range(len(kitaplar)):
                k = kitaplar[i]
                print(str(i + 1) + ". " + k["baslik"] + " — " + k["yazar"] + " [" + k["durum"] + "]")
            print("---------------------")

    elif secim == "2":
        baslik = input("Kitap basligi: ")
        if baslik.strip() == "":
            print("Baslik bos olamaz!")
        else:
            yazar = input("Yazar: ")
            kitap = {
                "baslik": baslik,
                "yazar": yazar,
                "durum": "okunmadi"
            }
            kitaplar.append(kitap)
            print("'" + baslik + "' eklendi.")
            dosya_kaydet()

    elif secim == "3":
        if len(kitaplar) == 0:
            print("Guncellenecek kitap yok.")
            continue
            
        print("--- KITAP LISTESI ---")
        for i in range(len(kitaplar)):
            k = kitaplar[i]
            print(str(i + 1) + ". " + k["baslik"] + " — " + k["yazar"] + " [" + k["durum"] + "]")
        print("---------------------")

        no_str = input("Durumunu degistirmek istediginiz kitabin numarasi: ")
        try:
            no = int(no_str)
            if 1 <= no <= len(kitaplar):
                secilen = kitaplar[no - 1]
                if secilen["durum"] == "okunmadi":
                    secilen["durum"] = "okundu"
                else:
                    secilen["durum"] = "okunmadi"
                
                print("'" + secilen["baslik"] + "' artik [" + secilen["durum"] + "] olarak isaretlendi.")
                dosya_kaydet()
            else:
                print("Gecersiz kitap numarasi!")
        except ValueError:
            print("Lutfen bir sayi girin!")

    elif secim == "4":
        if len(kitaplar) == 0:
            print("Silinecek kitap yok.")
            continue
            
        print("--- KITAP LISTESI ---")
        for i in range(len(kitaplar)):
            k = kitaplar[i]
            print(str(i + 1) + ". " + k["baslik"] + " — " + k["yazar"] + " [" + k["durum"] + "]")
        print("---------------------")

        no_str = input("Silmek istediginiz kitabin numarasi: ")
        try:
            no = int(no_str)
            if 1 <= no <= len(kitaplar):
                silinen = kitaplar.pop(no - 1)
                print("'" + silinen["baslik"] + "' silindi.")
                dosya_kaydet()
            else:
                print("Gecersiz kitap numarasi!")
        except ValueError:
            print("Lutfen bir sayi girin!")

    elif secim == "5":
        print("Programdan cikiliyor...")
        break

    else:
        print("Gecersiz secim! Lutfen 1-5 arasi bir deger girin.")