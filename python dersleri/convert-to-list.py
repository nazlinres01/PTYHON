"""
def yazdir(kelime,adet):
    print(kelime*adet)
yazdir('Merhaba\n',5)


def listeyeCevir(*params):
    liste=[]

    for param in params:
        liste.append(param)
    return liste
result=listeyeCevir(10,20,40,'Nazo')
print(result)


sayi1=int(input("sayi1:"))
sayi2=int(input("sayi2:"))
def asalSayiBulma(sayi1,sayi2):
   for sayi in range(sayi1,sayi2+1):
       if sayi>1:
           for i in range(2,sayi):
               if(sayi%i==0):
                   break
           else:
               print(sayi)
                    
asalSayiBulma(sayi1,sayi2)
"""
sayi=int(input("sayi:"))
def bolenBulma(sayi):
    tamBolenler=[]
    for i in range(2,sayi):
        if(sayi%i==0):
            tamBolenler.append(i)
    print(tamBolenler)
bolenBulma(sayi)
