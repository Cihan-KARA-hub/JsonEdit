import json


# JSON dosyasını oku  ilk gelen jsonu
with open('in.json', 'r', encoding='utf-8-sig') as f:
    veri = json.load(f)

# Yeni düzenlenmiş veri
duzenlenmis_veri = []
index = 0
yeni_eleman1 = {}

# Her bir öğeyi düzenlenmiş formata dönüştür
for eleman in veri:
    if index == 0:
        yeni_eleman1.update({
            "imsak_hadisi": eleman.get("meal", ""),
            "imsak_muctehidi": eleman.get("Ravi", "bilinmiyor")
        })

    elif index == 1:
        yeni_eleman1.update({
            "sabah_hadisi": eleman.get("Aciklama", ""),
            "sabah_muctehidi": eleman.get("Ravi", "bilinmiyor")
        })
    elif index == 2:
        yeni_eleman1.update({
            "oglen_hadisi": eleman.get("Aciklama", ""),
            "oglen_muctehidi": eleman.get("Ravi", "bilinmiyor")
        })
    elif index == 3:
        yeni_eleman1.update({
            "ikindi_hadisi": eleman.get("Aciklama", ""),
            "ikindi_muctehidi": eleman.get("Ravi", "bilinmiyor")
        })

    elif index == 4:
        yeni_eleman1.update({
            "aksam_hadisi": eleman.get("Aciklama", ""),
            "aksam_muctehidi": eleman.get("Ravi", "bilinmiyor")
        })
    elif index == 5:
        yeni_eleman1.update({
            "yatsi_hadisi": eleman.get("Aciklama", ""),
            "yatsi_muctehidi": eleman.get("Ravi", "bilinmiyor")
        })
        
        duzenlenmis_veri.append(yeni_eleman1)
        # Yeni bir nesne oluşturmak için index'i sıfırla
        yeni_eleman1 = {}
        index = 0
        continue
    
    index += 1

# Düzenlenmiş veriyi yaz
with open('in_düzenli.json', 'w', encoding='utf-8') as f:
    json.dump(duzenlenmis_veri, f, ensure_ascii=False, indent=2)
