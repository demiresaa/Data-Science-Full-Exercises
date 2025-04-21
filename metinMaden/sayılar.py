import  os

dosya_dizini=r"C:\Users\dell\Desktop\nesne\Texts"

almanca_metinler=[]
turkce_metinler=[]
ispanyolca_metinler=[]
ingilizce_metinler=[]

for dosya in os.listdir(dosya_dizini):
    if dosya.endswith(".txt"):
        dosya_yolu = os.path.join(dosya_dizini, dosya)
        with open(dosya_yolu, "r", encoding="utf-8") as haberler:
            metin = haberler.read()
            if "ALMANCA" in dosya:
                almanca_metinler.append(metin)
            elif "TURKCE" in dosya:
                turkce_metinler.append(metin)
            elif "İSPANYOLCA" in dosya:
                ispanyolca_metinler.append(metin)
            elif "İNGİLİZCE" in dosya:
                ingilizce_metinler.append(metin)

with open("almanca_metinler.txt","w",encoding="utf-8")as f:
    for metin in almanca_metinler:
        f.write(metin+"\n")

with open("turkce_metinler.txt","w",encoding="utf-8")as f:
    for metin in turkce_metinler:
        f.write(metin+"\n")


with open("ispanyolca_metinler.txt","w",encoding="utf-8")as f:
    for metin in ispanyolca_metinler:
        f.write(metin+"\n")


with open("ingilizce_metinler.txt","w",encoding="utf-8")as f:
    for metin in ingilizce_metinler:
        f.write(metin+"\n")


ort_karakter_sayisi=0
topl_karakter_sayisi=0

for metin in ingilizce_metinler:
    for i in metin:
        karakter_sayisi=len(i)
        topl_karakter_sayisi=topl_karakter_sayisi+karakter_sayisi
    ort_karakter_sayisi=topl_karakter_sayisi/1000
print("ort karakter sayısı :",ort_karakter_sayisi)

for metin in turkce_metinler:
    for i in metin:
        karakter_sayisi=len(i)
        topl_karakter_sayisi=topl_karakter_sayisi+karakter_sayisi
    ort_karakter_sayisi=topl_karakter_sayisi/1000
print("ort karakter sayısı :",ort_karakter_sayisi)

for metin in ispanyolca_metinler:
    for i in metin:
        karakter_sayisi=len(i)
        topl_karakter_sayisi=topl_karakter_sayisi+karakter_sayisi
    ort_karakter_sayisi=topl_karakter_sayisi/1000
print("ort karakter sayısı :",ort_karakter_sayisi)

for metin in almanca_metinler:
    for i in metin:
        karakter_sayisi=len(i)
        topl_karakter_sayisi=topl_karakter_sayisi+karakter_sayisi
    ort_karakter_sayisi=topl_karakter_sayisi/1000
print("ort karakter sayısı :",ort_karakter_sayisi)



ort_cumle=0
toplam_kelime=0
toplam_cumle=0
ort_kelime=0



import re

for metinx in turkce_metinler:
    ali = metinx.split()
    veli=re.split(r"[.?!]",metinx)
    toplam_kelime = toplam_kelime + len(ali)
    toplam_cumle=toplam_cumle+len(veli)
    ort_cumle=toplam_cumle/1000
    ort_kelime = toplam_kelime / 1000
print("Türkçe Ortalama Kelime Sayısı :",int(ort_kelime))
print("Türkçe Ortalama Cumle Sayısı :",int(ort_cumle))

for metinx in ispanyolca_metinler:
    ali = metinx.split()
    veli=re.split(r"[.?!]",metinx)
    toplam_kelime = toplam_kelime + len(ali)
    toplam_cumle=toplam_cumle+len(veli)
    ort_cumle=toplam_cumle/1000
    ort_kelime = toplam_kelime / 1000
print("Türkçe Ortalama Kelime Sayısı :",int(ort_kelime))
print("Türkçe Ortalama Cumle Sayısı :",int(ort_cumle))

for metinx in almanca_metinler:
    ali = metinx.split()
    veli=re.split(r"[.?!]",metinx)
    toplam_kelime = toplam_kelime + len(ali)
    toplam_cumle=toplam_cumle+len(veli)
    ort_cumle=toplam_cumle/1000
    ort_kelime = toplam_kelime / 1000
print("Türkçe Ortalama Kelime Sayısı :",int(ort_kelime))
print("Türkçe Ortalama Cumle Sayısı :",int(ort_cumle))

for metinx in ingilizce_metinler:
    ali = metinx.split()
    veli=re.split(r"[.?!]",metinx)
    toplam_kelime = toplam_kelime + len(ali)
    toplam_cumle=toplam_cumle+len(veli)
    ort_cumle=toplam_cumle/1000
    ort_kelime = toplam_kelime / 1000
print("Türkçe Ortalama Kelime Sayısı :",int(ort_kelime))
print("Türkçe Ortalama Cumle Sayısı :",int(ort_cumle))


