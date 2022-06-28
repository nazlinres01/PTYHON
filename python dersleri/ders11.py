"""
sayilar=[1,3,5,7,9,12,19,21]

i=0
while (i<len(sayilar)):
    print(sayilar[i])
    i+=1

baslangic=int(input("başlangıç değeri:"))
bitis=int(input("bitiş değeri:"))

i=baslangic
while i<bitis:
    i+=1
    if i%2!=0:
        print(i)
    

i=100
while i>0:
    print(i)
    i-=1
    


numbers=[]
i=0
while i<5:
    sayi=int(input("sayi:"))
    numbers.append(sayi)#listeye ekleme yapıyor
    i+=1
numbers.sort()#küçükten büyüğe sıralama yapıyor
print(numbers)

"""
urunler=[]
urunsayisi=int(input("ürün sayisi:"))
i=0
while i<urunsayisi:
    name=input("ürünün ismini giriniz:")
    price=float(input("ürünün fiyatını giriniz:"))
    urunler.append({
        'ad':name,
        'fiyat':price
    })
    i+=1

print(urunler)

for urun in urunler:
    print(f"ürün adı:{urun['ad']} ürün fiyatı:{urun['fiyat']}")



















































