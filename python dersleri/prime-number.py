sayi=int(input("bir sayi giriniz:"))
bolenSayisi=0
def asalSayiBulma(sayi):       
    for i in range(2,sayi):
        if(sayi%i==0):
            bolenSayisi+=1
            break
    if(bolenSayisi==0):
        print("girdiğiniz sayi asal sayidir...")
    else:
        print("girdiğiniz sayi asal sayi değildir...")
    

asalSayi(sayi)            

        

