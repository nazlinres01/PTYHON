"""
10 tane sayı girme 
sayi=0

while sayi<10:
    sayi+=1
    gir=int(input("sayi:"))

#rastgele sayıyı tahmin etme 
import random
rastgele=random.randint(1,5)#rastgele sayi

can=int(input("hak sayisi:"))
hak=can
sayac=0
while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input("bir sayi giriniz:"))


    if rastgele==tahmin:
        print(f"Tebrikler {sayac}. defada bildiniz.Puanınız:{100-(sayac-1)*(100/can )}")
        break
    elif rastgele>tahmin:
        print("yukarı çıkın...")
    else:
        print("aşağı inin...")

    if hak==0:
        print(f"hakkınız bitti.Tutulan sayi:{rastgele}")

"""

sayi=int(input("bir sayi giriniz:"))

bolen=1
bolensayısı=0
while sayi-1>bolen:
    bolen+=1
    if sayi%bolen==0:
        bolensayısı+=1
        print(f'bölen{bolensayısı}:{bolen}')
print(f'bölen sayısı:{bolensayısı}')
if bolensayısı>0:
    print("sayi asal değildir...")
elif sayi==1:
    print("sayi asal değildir...")
else:
    print("sayi asaldir...")

####################################
sayi=int(input("bir sayi giriniz:"))
asalmi=True

if sayi==1:
    asalmi=False

for i in range(2,sayi):
    if(sayi%i==0):
        asalmi=False
        break

if asalmi:
    print("sayi asaldir...")
else:
    print("sayi asal değildir...")
    





    














    
