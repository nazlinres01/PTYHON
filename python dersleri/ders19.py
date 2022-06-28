"""
for x in range(1,10):#1,2,3,4,5,6,7,8,9
    print(x)

for y in range(4):#0,1,2,3
    print(y)

for z in range(1,10,2):#1,3,5,7,9
    print(z)

for a in range(10):
    if a%2==0:
        continue #2'ye bölünenleri alma 
    print(a)


for b in range(1,10):
    if b%3==0: #sayı 3 e bölününceye kadar devam ettir 1,2
        break #sonra döngüden çıkılır
    print(b)


metin=input("bir metin giriniz:")
for c in range(5):#sayı olarak 0,1,2,3,4 sayıları yazılır
    print(metin)

toplam=0
sayi1=int(input("1.sayi:"))
sayi2=int(input("2.sayi:"))
for sayi in range(sayi1+1,sayi2):
    toplam+=sayi
print(toplam)

carpim=1
sayi=int(input("bir sayi:"))
for x in range(1,sayi+1):
    carpim*=x
print("faktöriyel:",carpim)
print("{0} sayısının faktoriyeli : {1}".format(sayi,carpim))


sayac=0
sayi=int(input("sayi:"))
for i in range(2,sayi):
    if(sayi%i==0):
        sayac+=1
        break #bir tane bölen bulması yeterli
    
if(sayac==0):#bölen sayısını gösteriyor sayac yani hiç böleni yoksa asaldır
    print("sayi asaldir...")
else:
    print("sayi asal değildir...")
        

a=1
while a<10:
    print(a,end=" ")#yan yana yazar arada boşluk bırakarak
    a+=1


a=1
toplam=0
while a<=10:
    toplam+=a
    a+=1
print(toplam)
    


a=0
toplam=0
while a<=101:
    a+=1
    if(a%2==1):
        toplam+=a
print(toplam)
        



x=0
sonuc=0
p=int(input("bir p değeri giriniz:"))
while x<=10:
    sonuc+=x**p
    x+=1
print(sonuc)
"""

# 0 sayısı girilene kadar döngü çalışır
while True:#şart hep doğru - sonsuz döngü
    sayi=int(input("bir sayi giriniz:"))
    if sayi==0:
        break








