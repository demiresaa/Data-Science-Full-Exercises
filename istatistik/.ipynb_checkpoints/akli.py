ali = float(input("Ali'nin soyadını giriniz: "))
veli = float(input("Veli'nin soyadını giriniz: "))

twoSoyad = complex(ali, veli)
print(twoSoyad, "oluşturuldu")

liste = ["akş", "ddd", "sddsda"]
liste.append("veli")
print(liste)

import numpy as np

ale = range(11, 22, 11)
print(ale)

ad = input("Öğrencinin adı: ")
if ad == "":
    print("Boş girme")
else:
    a = eval("33 + 33")
    print(a)  # EVAL() BİZE STRİNG İFADELERDE İNT GİBİ ÇALIŞMAMIZI SAĞLAR

veli = " adali sds "
ali = veli.strip()
print(len(ali), len(veli))

cilekes = " gerizeaklo "
print(len(cilekes))
ali=cilekes.strip()
print(len(ali))

eski = "şlskwAsADSL"
yeni = "şdllLALkfnr"
ceviriTablosu = str.maketrans(eski, yeni)
metin = "öğrewmek için tıkla"
print(metin.translate(ceviriTablosu))

metin = input("Metin giriniz: ")
kelime = input("Aranan kelimeyi giriniz: ")
gKelime = kelime.lower()
sayKelime = metin.count(kelime)
print("Aranan kelime metinde", sayKelime, "defa geçiyor.")

# String formatlama
sayi = 25
sayi2 = 366
malzeme = "anahtar"
malzeme2 = "kalem"
metin = "Ben {} tane {} ve {} tane {} aldım".format(sayi, malzeme, sayi2, malzeme2)
print(metin)

miktar = 499
ifade = "Satın aldığım bilgisayar parçası {} Tl'dir"
print(ifade.format(miktar))

dFiyat = 10
bFiyat = 23
dKilo = 2
bKilo = 1

ifade = "Marketten toplam {} kg biber ve {} kg domates aldım. Toplam {} Tl ödedim."
print(ifade.format(bKilo, dKilo, bFiyat * bKilo + dFiyat * dKilo))  # İNDEXLİ KULLANIM BU FORMATIN

dFiyat = 10
bFiyat = 23
dKilo = 2
bKilo = 1
ifade = "Marketten {0:.2f} kg biber ve {1:.3f} kg domates alarak toplam {2} Tl ödedim."
print(ifade.format(dFiyat * 10, bFiyat / 3, bKilo * dKilo))

sonuc = 10 / 3
ifade = "10 sayısının 3 e bölümünden sonuç {0:.2f}'dır."
print(ifade.format(sonuc))

dFiyat = 10
bFiyat = 23
dKilo = 2
bKilo = 1
ifade = "Marketten {0:,} kg biber ve {1:0} kg domates alarak toplam {2} Tl ödedim."
print(ifade.format(dFiyat * 10, bFiyat / 3, bKilo * dKilo))

a = 5
b = 4
if a == 3 and b == 4:
    print("Eşittir")
else:
    print("Değildir")

# Kullanıcıdan iki sayı al ve kontrol et
ali = int(input("İlk sayıyı giriniz: "))
veli = int(input("İkinci sayıyı giriniz: "))
if ali == 6 and veli == 1:
    print("Eşittir")
else:
    print("Değildir")

# Kullanıcıdan bir metin iste, metinde 'a' veya 'b' harfi geçip 'c' ve 'd' harfi geçmiyorsa bir mesaj yazdır
metin = input("Metin giriniz: ")
if ("a" in metin or "b" in metin) and ("c" not in metin and "d" not in metin):
    print("Şart sağlandı")
else:
    print("Şart sağlanmadı")

# Dizi Metodları
# Append ile ekleme
dizi = ["a", "b"]
dizi.append("c")
print(dizi)

# Clear ile temizleme
dizi.clear()
print(dizi)

# Copy ile kopyalama
dizi = ["a", "b", "c"]
kopyaDizi = dizi.copy()
print(kopyaDizi)

# Count ile sayma
notlar = [80, 45, 74, 52, 36, 80, 50, 33, 80]
arananNot = 80
sayac = notlar.count(arananNot)
print("İstenilen değerden", sayac, "tane geçti")

# Extend ile birleştirme
dizi1 = [1, 2, 3, 4,2,4]
dizi2 = [5, 6, 7, 8,5]
dizi1.extend(dizi2)
print(dizi1)

# Insert ile ekleme
dizi = [1, 2, 3, 4]
dizi.insert(2, 5)
print(dizi)

# Pop ile eleman çıkarma
eleman = dizi.pop(2)
print("Çıkarılan eleman:", eleman)
print("Güncellenmiş dizi:", dizi)

# Remove ile eleman silme
dizi.remove(4)
print(dizi)

# Reverse ile ters çevirme
dizi.reverse()
print(dizi)

# Sort ile sıralama
dizi = [3, 1, 4, 2, 5]
dizi.sort()
print(dizi)

a=input()
print(a)

ad=input("Adınız:")
yas=input("Yaşınız:")
print(ad+" "+yas+" yaşındadır.")

#Kullanıcının girdiği iki sayıyı toplama

s1=input("Sayı 1:")
s2=input("Sayı2:")
sonuc=s1+s2
print(sonuc)

s1=input("Sayı 1:")
s2=input("Sayı2:")
s1=int(s1)
s2=int(s2)
print(s1+s2)

#Girilen sayının tek veya çift sayı olduğunu belirleme

sayi=input("Bir sayı giriniz:")
sayi=int(sayi)
sonuc=""
if(sayi%2==0):
    sonuc="çift"
else:
    sonuc="tek"
print(sonuc)

#İki sayı ile işlem yapan basit hesap makinesi
s1=input("Birinci sayı giriniz:")
s1=float(s1)
s2=input("İkinci sayı giriniz")
s2=float(s2)
sonuc=0
tur=input("İşlem türünü giriniz(*,/,+,-)")
if(tur=="+"):
    sonuc=s1+s2
elif(tur=="-"):
    sonuc=s1-s2
elif(tur=="*"):
    sonuc=s1*s2
elif(tur=="/"):
    sonuc=s1/s2
else:#bilinmeyen işlem
    sonuc="bilinmeyen işlem girişi yapıldı"
print(sonuc)

#Hesap makinesinde kullanıcı hatalarını önleme
try:
    s1 = input("Birinci sayı giriniz:")
    s1 = float(s1)
    s2 = input("İkinci sayı giriniz")
    s2 = float(s2)
    sonuc = 0
    tur = input("İşlem türünü giriniz(*,/,+,-)")
    if (tur == "+"):
        sonuc = s1 + s2
    elif (tur == "-"):
        sonuc = s1 - s2
    elif (tur == "*"):
        sonuc = s1 * s2
    elif (tur == "/"):
        sonuc = s1 / s2
    else:  # bilinmeyen işlem
        sonuc = "bilinmeyen işlem girişi yapıldı"
    print(sonuc)
except ValueError as e:
    print(e)
except ZeroDivisionError as e2:
    print("Sıfıra bölünme hatası:",e2)
finally:
    print("İşlem bitti")

#+/- işaretine her basıldığında sayıyı atttırma/azaltma
sayi=0
while True:
    durum=input()
    if(durum=="+"):
        sayi=sayi+1
    elif(durum=="-"):
        sayi=sayi-1
    else:
        quit()
    print(sayi)

#+10 ile -10 arasındaki sayıları ekrana yazma
for i in range(10,-11,-2):
    metin=str(i)+" sayı"
    print(metin)

#Metindeki her harfin arasına virgül koyma
metin=input("Bir metin giriniz: ")
sonuc=""
for harf in metin:
    sonuc=sonuc+harf+","
print(sonuc)
#en son kısımda virgül olmasını istemiyorsak
metin=input("Bir metin giriniz: ")
sonuc=""
for harf in metin:
    sonuc=sonuc+harf+","
sonuc=sonuc[0:len(sonuc)-1]
print(sonuc)

#1 ile 100 arasında rastgele 10 tam sayı üretip dizi içine ekleme
import random
dizi=list()
for i in range(10):
    sayi=random.randint(1,100)
    dizi.append(sayi)
print(dizi)

#-100 ile +100 arasındaki 5'e tam bölünen sayıları yan yana gösterme
metin=""
for i in range(-100,101,1):
    if(i%5==0):
        if(i==100):
            metin=metin+str(i)
        else:
            metin = metin + str(i) + ","
    else:
        continue
print(metin)
#while döngüsü kullanarak gösterme
metin=""
i=-101
while i<=100:
    i+=1
    if(i%11==0):
        if i==100:
            metin=metin+str(i)
        else:
            metin=metin+str(i)+","
    else:
        continue
print(metin)
#daha kısa gösterimi
metin=""
dizi=list()
for i in range(-100,101,1):
    if(i%5==0):
        dizi.append(i)
    else:
        continue
print(*dizi,sep=",")

#Üç adet sayıyı karşılaştırıp sıralama
s1=input("Sayı 1 giriniz:")
s1=int(s1)
s2=input("Sayı 2 giriniz:")
s2=int(s2)
s3=input("Sayı 3 giriniz")
s3=int(s3)
enBuyuk=0
if s1>s2 and s1>s3:
    enBuyuk=s1
elif s2>s1 and s2>s3:
    enBuyuk=s2
else:
    enBuyuk=s3
print(enBuyuk)
#for dögüsüyle bulma
dizi=list()
for i in range(3):
    sayi=input("Sayı "+str(i+1)+" giriniz:")
    sayi=int(sayi)
    dizi.append(sayi)
dizi.sort()
print(dizi)

#Faktöriyel hesaplama ve açılımını yazdırma
sayi=input("Sayı giriniz:")
sayi=int(sayi)
sonuc=1
metin=""
for i in range(sayi,0,-1):
    sonuc *=i
    metin +=str(i)+"*"
metin=metin[0:len(metin)-1]
print(metin+"="+str(sonuc))

#Metindeki ilk kelime ile son kelimeyi bulma
metin=input("İfade giriniz:")
dizi=metin.split(" ")
print("İlk kelime=",dizi[0])
print("Son kelime=",dizi[len(dizi)-1])
#index ve rindex ile ilk ve son kelimeyi bulma
metin=input("İfade giriniz:")
ilkBoslukKonum=metin.index(" ")
sonBoslukKonum=metin.rindex(" ")
ilkKelime=metin[0:ilkBoslukKonum]
sonKelime=metin[sonBoslukKonum:len(metin)]
print("İlk Kelime=",ilkKelime)
print("Son Kelime=",sonKelime)

toplam=0
for i in range(10):
    sayi=input("sayi"+str(i+1)+"giriniz")
    sayi=int(sayi)
    toplam+=sayi
ortalama=toplam/10
print("toplam="+str(toplam))
print("ortalama="+str(ortalama))

metin=input("ifade giriniz")
ilkBoslukKonum=metin.index(" ")
sonBoslukKonum=metin.rindex(" ")

sonKelime=metin[sonBoslukKonum:len(metin)]
ilkKelime=metin[0:ilkBoslukKonum]
print("ilk kelime= "+ilkKelime)
print("son kelime= "+sonKelime)

maas=float(maas)
zamOran=float(zamOran)
prim=float(prim)

zamMik=(maas*zamOran)/100
yeniMaas=maas+zamMik+prim

print("zam miktarı :"+str(zamMik))
print("yeni maas miktarı:"+str(yeniMaas))


toplam=0
sayi=input("sayi giriniz")

if sayi.isnumeric()==False:
    print("lütfen sadece sayı girinşiz")
else:
    for i in sayi:
        toplam+=int(i)
print(sayi+ " sayısının sayi değeri toplama"+str(toplam))

maas=input("maaş miktarı gir")
zamOran=input("zam oranı % griniz")
prim=input("prim miktarını grinşz")

dizi=[]
print("cıkış için Q harfine basın aksi halde sayı girmeye devam edinşiz")

while True:
    sayi=input("sayi girinşz")
    if sayi.upper()=="Q":
        break
    sayi=int(sayi)
    durum=""
    if sayi%2==0:
        durum="çift"
    else:
        durum="Tek"
    dizi.append(str(sayi)+":" + durum)

print(dizi)


dizi=[]
for sayi in range(1,300):
    teklerTop=0
    ciftlerTop=0
    sayi=str(sayi)
    for i in range(0,len(sayi)):
        if i%2==0:
            ciftlerTop+=int(sayi[i])
        else:
            teklerTop+=int(sayi[i])
        if abs(ciftlerTop-teklerTop)%11==0:
            dizi.append(sayi)
print(*dizi,sep="\n")

vize=float(input("vize notunu gir"))
final=float(input("final notunu gir"))

gecmeNotu=vize*0.4+final*0.6
durum=""

if gecmeNotu>=70:
    durum="geçri"
else:
    durum="kaldı"
print("geçme notu:{0} ".format(gecmeNotu))
print("durumunuz:{0}".format(durum))

a=float(input("a kenari giriniz"))
b=float(input("b kenari girinşz"))
c=float(input("c kenari girinşz"))

u=(a+b+c)/2

import math

alan=math.sqrt(u*(u-a)*(u-b)*(u-c))
print("alan:{0}".format(alan))

metin=input("metin giriniz")
metin=metin.lower()
sesliHarf="aeiıoöüu"

sayac=0

for i in metin:
    for j in sesliHarf:
        if i==j:
            sayac+=1
print("%s metindeki sesli harf sayısı: %d" % (metin, sayac))

baslangic=int(input("başlangıc giriniz"))
bitis=int(input("bitis giriniz"))

sonuc=""

for i in range(baslangic,bitis+1):
    for i in range(1,i+1):
        sonuc   +=str(i)
    sonuc+="\n"
print(sonuc)


baslangic=input("başlangıc giriniz")
bitis=input("bitiş giriniz")
urtSayıAdet=input("üretilecek sayı adedini giriniz")
bitis=int(bitis)
urtSayıAdet=int(urtSayıAdet)
baslangic=int(baslangic)

dizi=list()

import random

while True:
    sayi=random.randint(baslangic,bitis)
    if dizi.count(sayi)>0:
        continue
    else:
        dizi.append(sayi)
        urtSayıAdet-=1
    if  urtSayıAdet==0:
        break
print(dizi,sep="\n")


baslangic=input("başlangıc girinşiz")
bitis=input("bitiş giriniz")
urtSayiAded=input("üretilecek sayi adedini giriniz")
baslangic=int(baslangic)
bitis=int(bitis)
urtSayiAded=int(urtSayiAded)

dizi=list(range(baslangic,bitis+1))

import random
random.shuffle(dizi)
parcaDizi=dizi[1:urtSayiAded]
print(*parcaDizi,sep="\n")

sayi=input("sayı giriniz")
sayi=int(sayi)

diziAsalCarp=list()

bolen=2
while sayi !=1:
    if sayi % bolen ==0:
        sayi=sayi/bolen
        diziAsalCarp.append(bolen)
        bolen=-1
    bolen+=1
print("diziAsalCarp",sep="/n")

metin=input("metin giriniz")
sozluk={}
enUzunKlmUznlk=0
enUzunKlm=" "

diziKelimeler=metin.split(" ")

for i in diziKelimeler:
    sozluk[i]=len(i)


for i in sozluk:
    if sozluk[i]>enUzunKlmUznlk:
        enUzunKlmUznlk=sozluk[i]
        enUzunKlm=i

print("en uzun kelime uzunluk:"+str(enUzunKlmUznlk))
print("en uzun kelime: "+enUzunKlm)


metin=input("metin giriniz:")
enUzunKlmUznlk=0
enUzunKlm=""

sozluk={i: len(i)for i in metin.split(" ")}

for i in sozluk:
    if sozluk[i]>enUzunKlmUznlk:
        enUzunKlmUznlk=sozluk[i]
        enUzunKlm=i

print("en uzun kelime uzunluk:"+str(enUzunKlmUznlk))
print("en uzun kelime: "+enUzunKlm)
print(sozluk)


puan=input("not giriniz")
puan=float(puan)

notListesi={
    84:["AA",4.0,"Geçti"],
    77:["AB",3.7,"Geçti"],
    71:["BA",3.3,"Geçti"],
    66:["BB",3.0,"Geçti"],
    61:["BC",2.7,"GEçti"],
    56:["CB",2.3,"Geçti"],
    50:["CC",2.0,"GEçti"],
    46:["CD",1.7,"Ortalamay aBağlı Geçti"],
    40:["DD",1.3,"Ortalamaya baplı geçti"],
    33:["DD",1.0,"Ortalamaya bağlı geçti"],
    0:["FF",0.0,"Kaldi"]
}
for i in notListesi:
    if puan>=i:
        dizi=notListesi[i]
        print("harf notu :"+dizi[0])
        print("4'lük not:" +str(dizi[1]))
        print("durum:"+dizi[2])
        break

cumle=input("cumle giriniz")
kelimeler=cumle.split(" ")
yeniCumle=""
tersCumle=""

for kelime in kelimeler:
    for harf in kelime:
        tersCumle=harf+tersCumle
    yeniCumle+=tersCumle+""
    tersCumle=""
print(yeniCumle)


""""""
cumle = input ("cümle giriniz")
cumle=cumle.upper()
sozluk={
    " ": "  ",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",

}
yeniCumle=""
for harf in cumle:
    yeniCumle+=sozluk[harf]

print(yeniCumle)

toplam = 0
for i in range(100,150,1):
    try:
        toplam+=(2*(i-2))/abs(i+2)**(1/3)
    except:
        continue
    print(toplam)

import math
toplam  =0
for i in range(100,-150,-1):
    try:
        toplam+=(2*(i-2))/math.pow(abs(i+2),1/3)
    except:
        continue
print(toplam)





# Boş bir liste oluştur
dizi = []

# 1'den 10'a kadar olan sayıları listeye ekle
for i in range(1, 11):
    dizi.append(i)

print(dizi)

# Büyük harfleri 5 kez tekrarlayarak bir liste oluştur
metin = "SAKARYA belediyesi"
dizi = [i * 5 for i in metin if i.isupper()]
print(dizi)

# Tuple'lar oluştur ve yazdır
demet1 = ("ankara", "istanbul", "kayseri")
demet2 = ("ankara", "istanbul", "kayseri")
print(demet2, demet1)

# Tuple'ı dilimle ve türünü yazdır
print(demet2[0:2])
print(type(demet2))

# Tuple üzerinde index ve count metotlarını kullan
demet = ("Ankara", "istanbul", "izmir")
indis = demet.index("Ankara")
print(indis)

say = demet.count("izmir")
print(say)

# Renklerin bulunduğu tuple üzerinde iterasyon yap
renkler = ("kırmızı", "mavi", "sarı", "mor")
for renk in renkler:
    print(renk)

# Tuple'ı dilimle
print(renkler[:2])

# Tuple'ları birleştir
digerRenkler = ("ali", "veli")
tumRenkler = renkler + digerRenkler
print(tumRenkler)

# Şu anki tarih ve saati al
from datetime import datetime

saat = datetime.now()
print(saat)

# Belirli bir tarih ve saat oluştur
saat2 = datetime(2024, 11, 2)
print(saat2)

# Belirli bir tarihin ayına eriş
print(saat2.month)
print(saat2.strftime("%d.%m.%Y"))
print(saat2.strftime("%a"))
print(saat2.strftime("%A"))
print(saat.strftime("%B"))
print(saat.strftime("%w"))
print(saat.strftime("%p"))
print(saat.strftime("%m"))
print(saat.strftime("%H"))
print(saat.strftime("%I"))
print(saat.strftime("%d.%m.%Y %H:%M:%S.%f."))
print(saat.strftime("%c"))

# Kullanıcıdan doğum tarihi al ve ekrana yaz
gun = int(input("Günü giriniz: "))
ay = int(input("Ayı giriniz: "))
yil = int(input("Yılı giriniz: "))

dogum_tarihi = datetime(yil, ay, gun)
print("Doğum tarihi: ", dogum_tarihi.strftime("%d.%m.%Y"))

# Şu anki Unix zaman damgasını al ve datetime nesnesine dönüştür
simdikiZ = datetime.now()
unixZaman = simdikiZ.timestamp()
print("Şuanki zaman damgası", unixZaman)
tarih = datetime.fromtimestamp(unixZaman)
print("Tarih", tarih.strftime("%Y-%m-%d %H:%M:%S"))


sozluk=dict()
sozluk={"armut":"armut","ali":"veli"}

sozluk["elma"]="apple"
sozluk["muz"]="banana"
sozluk[4]="four"

print(sozluk)

sozluk2={}
sozluk2[3]="üç"
sozluk2[2]="iki"
sozluk2[4]=sozluk
print(sozluk2)

sozluk2[5]=[3,4,5,7,8]
print(sozluk2)

sozluk3={"muz":"banana","ahmet":"orrrrrrrmancocu"}
print(sozluk3)

print(sozluk2)
print(sozluk2[5][2]) #sozluk2 nin 5indisli elemanının 2. sıradaki değeri
print(sozluk2[4]["elma"])

print(sozluk.keys()) #sozlugun sadece anahtar kelimelerini verir
print(sozluk.values()) #sozlugun sadece anahtar kelime karsılıklarını verir
print(sozluk.items()) #sozlugun tüm anahtar kelime ve karsılıklarını verir
print(sozluk.get("muz")) #sözlükte muz kelimesi varsa karşılıgını getirir
print(sozluk.get("bababa")) #eger sorgulanan deger yoksa None cevabını verir
#print(sozluk.pop("muz")) muz sozcugunun sözlükten silinmesini saglar
#print(sozluk.popitem())  sozlugun son degerini ve anlamını siler

for anahtar,deger in sozluk.items():
    print(anahtar,deger)

#soru: 0-10 sayılarının türkçe karşılıklarını bir sözlükte tutun.her bir elemanın alt alta görünecegi şekilde yazdırın

sozluk = {
    0: "sıfır",
    1: "bir",
    2: "iki",
    3: "üç",
    4: "dört",
    5: "beş",
    6: "altı",
    7: "yedi",
    8: "sekiz",
    9: "dokuz",
    10: "on",
}

for anahtar,deger in sozluk.items():
    print(anahtar,":",deger)
import random

# x sayısı0-100 arasındaki sayılar için (2x + 5)/x*x denklemine göre hesaplanıp nir sözlük içinde tutun.
#kullanıcı tarafından girilen sayıyı sorgulayın eger sayı sözlükte yoksa belirtilen sayı sözkükte yoktur yazdırın

sozluk={}

for x in range(1,101):
    sozluk[x]= (2*x+5)/(x**2)
print(sozluk)

giris= input("bir sayı giriniz:")
giris=int(giris)

sonuc= sozluk.get(giris,"belirtilen sayı hesaplanmamıştır")
print(sonuc)

"""#X sayısı 0-100 arasındaki sayılar için yandaki denkleme göre hesaplanıp (2*x+5)/x*2
#bir sözlük içerisinde tutun. Kullanıcı tarafından verilen sayının sonucunu gösterin. Eğer sonuç
#bulunamazsa “Belirtmiş olduğunuz sayı hesaplanmamıştır” mesajı göstersin

sozluk = {}
for i in range(1, 101):
    sozluk[i] = (2 * i + 5) / (i ** 2)
print(sozluk)
giris = input("Sayı giriniz: ")
giris = int(giris)
sonuc = sozluk.get(giris, "Aradığınız sayı bulunmamaktadır")
print(sonuc)

try:
    sozluk = {i: (2 * i + 5) / (i ** 2) for i in range(1, 101)}
    print(sozluk)
    giris = input("Sayı giriniz: ")
    giris = int(giris)
    sonuc = sozluk[giris]
    print(sonuc)
except:
    print("Hata oluştu")


try:
    sozluk = {i: (2 * i + 5) / (i ** 2) for i in range(1, 101)}
    print(sozluk)
    giris = input("sayı giriniz:")
    giris = int(giris)
    sonuc = sozluk[giris]
    print(sonuc)
except:
    pass


import random #bu şekilde 0 ile 1 arasında random sayılar veriyor

sayi=random.random()
print(sayi)

import random

sayi= random.uniform(2,3)   #random.uniform() sayesinde verilen aralık içerisinden ondalıklı sayı tahmini yapar
print(sayi)

import random

sayi = random.randint(2,23)   #random.randint() metodu ile verilen aralıkta random tam sayı verir
print(sayi)

dizi = ["armut","mehmet","malrıfkı"]
secim = random.choice(dizi)     #random.choice(dizi) metodu ile dizi içerisinden random eleman verir
print(secim)

secim= random.choice("rıfkıeşşeğimaldır")   # bu şekilde stringden rastgele karakter verir
print(secim)

dizi = list(range(100))     # bu şekilde liste olan sayıları karıştırarark yazar
random.shuffle(dizi)
print(dizi)

dizi = list(range(100))
random.shuffle(dizi)
print(dizi)

sayi = random.sample(dizi , 5)  #sample metodu sayesinde karışık listeden istediğimiz kadar sayı alırız
print(sayi)

#soru: abcdefg harflerinden 4karakterli rastgele 10 tane kelime oluşturup bunları ekrana yazın.

import random

harfler = "abcdefg"
kelimeler= []

for i in range(10):
    harfdizisi = random.sample(harfler,4)
    kelime="".join(harfdizisi)
    kelimeler.append(kelime)
print(kelimeler)"""""""""""



sayi = int(input("Sayı giriniz: "))

if sayi > 1:
    for i in range(2, sayi):
        if (sayi % i) == 0:
            print(sayi, "asal değildir.")
            break
    else:
        print(sayi, "asaldır.")
else:
    print(sayi, "asal değildir.")

soru = input("Python mu?, C mi?")
while soru != "Python":
 print("Yanlış cevap!")

a="velibos sdeeeer ersddwww"
b=a.startswith("l")
print(b)

i = 1
while i <= 10:
    metin=str(i)+".sayı"
    i += 1
    print(metin)

metin="ali eve geldi"
dizi=[str(j)+"."+i for i in metin for j in range(2,len(metin)+1)]
print(dizi)

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleriBul(20))
def asalSayılariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

sayi1 = int(input('sayı 1:'))
sayi2 = int(input('sayı 2:'))

asalSayılariBul(sayi1, sayi2)

sayi = int(input("Bir sayı girin: "))
toplam = 0
i = 1

while i <= sayi:
    if i % 2 != 0:
        toplam += i
    i += 1

print("1 ile", sayi, "arasındaki tek sayıların toplamı:", toplam)

aa = float(input("Vize notunu giriniz: "))
bb = float(input("Final notunu giriniz: "))

aaa = aa *0.40
bba = bb *0.60

print("Sonuç: " + str(aaa + bba))

ali = float(input("0 ile 1 arasında bir sayı girin: "))
veli = int(input("100 ile 200 arasında 5'e tam bölünebilen bir sayı girin: "))

if ali <= 0 or ali >= 1:
    print("Ali için geçersiz bir sayı girdiniz. Lütfen 0 ile 1 arasında bir sayı girin.")
elif veli < 100 or veli > 200 or veli % 5 != 0:
    print("Veli için geçersiz bir sayı girdiniz. Lütfen 100 ile 200 arasında ve 5'e tam bölünebilen bir sayı girin.")
else:
    print("Girdiğiniz sayılar uygun aralıklarda ve koşulları sağlıyor.")
    print("Sonuç:", ali * veli)

#soru: 0-10 sayılarının türkçe karşılıklarını bir sözlükte tutun.her bir elemanın alt alta görünecegi şekilde yazdırın

sozluk = {
    0: "sıfır",
    1: "bir",
    2: "iki",
    3: "üç",
    4: "dört",
    5: "beş",
    6: "altı",
    7: "yedi",
    8: "sekiz",
    9: "dokuz",
    10: "on",
}

for anahtar,deger in sozluk.items():
    print("türkçede",anahtar,"sayısı",":",deger,"olarak yazılır")


from datetime import datetime
# Kullanıcıdan doğum tarihi al ve ekrana yaz
gun = int(input("Günü giriniz: "))
ay = int(input("Ayı giriniz: "))
yil = int(input("Yılı giriniz: "))
sımdıkıYıl=datetime.now()
dogum_tarihi = datetime(yil, ay, gun)
sonuc=sımdıkıYıl.year-dogum_tarihi.year
print("yaşı: ", float(sonuc))

sozluk = {}
for i in range(1, 101):
    sozluk[i] = (2 * i + 5) / (i ** 2)
print(sozluk)
giris = input("Sayı giriniz: ")
giris = int(giris)
sonuc = sozluk.get(giris, "Aradığınız sayı bulunmamaktadır")
print(sonuc)

try:
    sozluk = {i: (2 * i + 5) / (i ** 2) for i in range(1, 101)}
    print(sozluk)
    giris = input("Sayı giriniz: ")
    giris = int(giris)
    sonuc = sozluk[giris]
    print(sonuc)
except:
    print("Hata oluştu")

try:
    sayi1=int(input("sayı gır"))
    kare=sayi1**2
    print(kare)
except ValueError:
    print("hjatalı girdin")

try:
    ad="faruk"
    aranan_indis=int(input("istediğin sayıy grir"))
    karakter=ad[aranan_indis]
    x=3
except IndexError:
    print("bu indis yok ")
finally:
    print("program bitti")


# random randint  = tam sayı üretir
import random

dizi=["ali","veli","vekas"]
secim=random.choice(dizi) # choice diziden rastgele eleman secer
print(secim)

secim=random.choice("alicekkfn")
print(secim)

# shuffle diziyi karıştırır,

import random
dizi=list(range(10))
print(dizi)
random.shuffle(dizi)
print(dizi)
#

#randrange 0-100 arasında 100 dahil değil

sayi1=random.randrange(10,21)
print(sayi1)

# sample ise choice gibi ama samğle 1 den fazla secim yaparsın choice sadece 1 tane yazar

harfler ="dsdaggddei"
kelimeler= []

for i in range(10):
    harfdizisi = random.sample(harfler,4)
    kelime="".join(harfdizisi)
    kelimeler.append(kelime)
print(kelimeler)



import os

# Dosyanın bulunduğu dizini belirtin
dosya_dizini = r"C:\Users\dell\Desktop\nesne\Texts"

# Almanca ve Türkçe dosyalar için boş listeler oluşturun
almanca_metinler = []
turkce_metinler = []

# Dosyaları kontrol edin ve Almanca ve Türkçe dosyalara ayırın
for dosya in os.listdir(dosya_dizini):
    if dosya.endswith(".txt"):
        dosya_yolu = os.path.join(dosya_dizini, dosya)
        with open(dosya_yolu, "r", encoding="utf-8") as haberler:
            metin = haberler.read()
            if "ALMANCA" in dosya:
                almanca_metinler.append(metin)
            elif "TURKCE" in dosya:
                turkce_metinler.append(metin)
print(turkce_metinler)
