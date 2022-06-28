"""
genislik=int(input("genislik : "))
yukseklik=int(input("yukseklik : "))
def dikdortgenAlan():
    alan=genislik*yukseklik
    return alan
    


print("dikdörtgenin alanı :",dikdortgenAlan())

vizeNotu=float(input("vize notu : "))
finalNotu=float(input("final notu : "))
def notHesaplama():
    ortalama=(vizeNotu*0.4)+(finalNotu*0.6)
    if ortalama>=50:
        print("geçtiniz")
    else:
        print("kaldınız")
    return ortalama
print("ortalama :",notHesaplama())
"""
def isim(par1):
    print("İsminiz",par1)
isim("Nazli")

def sayilar(sayi1,sayi2):
    carpim=sayi1*sayi2
    print("*"*10)
    print("carpim :",carpim)
    print("*"*10)
sayilar(4,9)

def dikdortgenCevre(yukseklik,genislik):
    cevre=(yukseklik+genislik)*2
    print("çevre :",cevre)
dikdortgenCevre(11,8)

def kelime(klm):
    klm=len(klm)
    print(klm)
kelime("programlama")
kelime("merhabadünya")

def uzunlukBul(klm2):
    a=0
    for b in klm2:
        a+=1
    print(a)
uzunlukBul("nadimeesmeray")
    