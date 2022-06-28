"""
sayi=float(input("sayi:"))
if sayi>0 and sayi<100:
    print("girilen sayi 0 ile 100 arasındadır...")
else:
    print("girilen sayi 0 ile 100 arasında değildir...")

sayi=float(input("sayi:"))
if sayi>0 and sayi%2==0:
    print("pozitif çift sayidir...")
elif sayi<0 and sayi%2==0:
    print("negatif çift sayidir...")
elif sayi%2!=0:
    print("tek sayidir...")


email="nazli@gmail.com"
password="1234abc"

girilen_email=input("e-mail:")
girilen_password=input("password:")

if (girilen_email==email) and (girilen_password==password):
    print("başarılı bir şekilde giriş yaptınız...")
else:
    print("lütfen tekrar deneyiniz...")

a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))

if (a>b) and (a>c):
    if (b>c): 
        print("büyükten küçüğe sıralama: a>b>c")
    else:
        print("büyükten küçüğe sıralama: a>c>b")
if (b>a) and (b>c):
    if (a>c): 
        print("büyükten küçüğe sıralama: b>a>c")
    else:
        print("büyükten küçüğe sıralama: b>c>a")
if (c>a) and (c>b):
    if (a>b): 
        print("büyükten küçüğe sıralama: c>a>b")
    else:

        print("büyükten küçüğe sıralama: c>b>a")
#Daha da örnekler bulunmaktadır bakarsın

"""
numbers=[1,2,3,4,5]
for num in numbers:
    print("num")


names=["nazli","kübra","ayşe","fatma"]
for a in names:
    print(f'My name is {a}')

name="Nazli Nur Esmeray" #harfler ekrana yazılır
for n in name:
    print(n)


tupl=[(1,2),(3,4),(5,6)]                   # a olursa 2 4 6
for t,a in tupl:    #sadece t,a olup aşağıda t olursa 1 3 5 olur alt alta
    print(t,a)      #(alt üst)(t,a) 1 2 şeklinde alt alta
    
d={'k1':1, 'k2':2, 'k3':3}
for x in d:
    print(x) #alt alta k1 k2 k3

d={'k1':1, 'k2':2, 'k3':3}
for x,a in d.items():   #('k1', 1) şeklinde 
    print(x,a)





