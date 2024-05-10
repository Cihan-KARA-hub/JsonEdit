import json


# JSON dosyasını oku  ilk gelen jsonu
with open('yeni_sureler_turkce.json', 'r', encoding='utf-8-sig') as f:
    veri = json.load(f)

# Yeni düzenlenmiş veri
duzenlenmis_veri = []
index = 0
yeni_eleman1 = {}

# Her bir öğeyi düzenlenmiş formata dönüştür
for eleman in veri:

    if index == 0:
        yeni_eleman1.update({
            "gunes": eleman.get("meal", ""),
            "gunes_h_ayet": eleman.get("isim"),
           
        })

    elif index == 1:
        yeni_eleman1.update({
            "sabah": eleman.get("meal", ""),
            "sabah_h_ayet": eleman.get("isim", "bilinmiyor"),
       
        })
    elif index == 2:
        yeni_eleman1.update({
            "ogle": eleman.get("meal", ""),
            "ogle_h_ayet": eleman.get("isim", "bilinmiyor"),
          
        })
    elif index == 3:
        yeni_eleman1.update({
            "ikindi": eleman.get("meal", ""),
            "ikindi_h_ayet": eleman.get("isim", "bilinmiyor"),
         
        })

    elif index == 4:
        yeni_eleman1.update({
            "aksam": eleman.get("meal", ""),
            "aksam_h_ayet": eleman.get("isim", "bilinmiyor"),
         
        })
    elif index == 5:
        yeni_eleman1.update({
            "yatsi": eleman.get("meal", ""),
            "yatsi_h_ayet": eleman.get("isim", "bilinmiyor"),
          
        })
        
        duzenlenmis_veri.append(yeni_eleman1)
        # Yeni bir nesne oluşturmak için index'i sıfırla
        yeni_eleman1 = {}
        index = 0
        continue
    
    index += 1

# Düzenlenmiş veriyi yaz
with open('yeni_sureler_turkce1.json', 'w', encoding='utf-8') as f:
    json.dump(duzenlenmis_veri, f, ensure_ascii=False, indent=2)
