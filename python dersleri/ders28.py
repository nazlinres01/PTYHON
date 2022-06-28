"""
def yazdir():
    print("Nazli Nur Esmeray")
yazdir()

#Burda değer döndürülmüştür yazdırma işlemi yapılmamış onu da fonksiyonu
#çağırırken print kullanırız
def yazdir2():
    return "Bu zamanda her şey yavan"
print(yazdir2())


def toplama(sayi1,sayi2):
    return sayi1+sayi2

print(toplama(6,5))


def carpma(sayi3=4,sayi4=10):
    return sayi3*sayi4

print("Çarpım:",carpma())
print("Çarpım:",carpma(2))#sonuç 20
print("Çarpım:",carpma(7,8))#sonuç 56
"""

#hesap makinesi örneği
sayi1=int(input("1.sayi:"))
sayi2=int(input("2.sayi:"))
def toplama():
    return sayi1+sayi2
def cikarma():
    return sayi1-sayi2
def carpma():
    return sayi1*sayi2
def bolme():
    return sayi1/sayi2
print("toplam:",toplama())
print("çıkarım:",cikarma())
print("çarpım:",carpma())
print("bölüm:",bolme())











