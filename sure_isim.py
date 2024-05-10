import json

# Öncelikle, Endonezya dilindeki surelerin JSON verisini oluşturalım ve dosyaya yazalım



# Ardından, işlemler için Endonezya dilindeki surelerin JSON verisini yükleyelim
with open('turkce.json', 'r',encoding='utf-8') as f:
    endonezya_sureler = json.load(f)
with open('turkce_sure.json', 'r',encoding='utf-8') as a:
    diger_sureler = json.load(a)

# Yeni bir JSON dosyası oluşturmak için boş bir liste oluşturalım
yeni_sureler = []

for item_a in diger_sureler:
    # Sure_no değerini al
    sure_no_a = item_a.get('sure_no')
    ayet_no = item_a.get('ayet_no')
    meal = item_a.get('meal')
    
    for item_f in endonezya_sureler:
        sure_no_f = item_f.get("sure_no")
        isim_f = item_f.get("isim")
        
        if sure_no_a == sure_no_f:
            yeni_veri = {
                'sure_no': sure_no_f,
                'isim': isim_f+" "+ayet_no+".Ayet",  # Endonezya sure ismi
                'meal': meal
            }
            yeni_sureler.append(yeni_veri)

# Son olarak, yeni JSON verisini dosyaya yazalım
with open('yeni_sureler_turkce.json', 'w') as f:
    json.dump(yeni_sureler, f)
