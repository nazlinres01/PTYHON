"""
ad=input("ad:")
kilo=float(input("kilo:"))
boy=float(input("boy:"))
index=(kilo)/(boy**2)
zayıf=(index>0)and(index<=18.4)
normal=(index>=18.5)and(index<=24.9)
fazla_kilolu=(index>=25)and(index<=29.9)
sisman=(index>=30)and(index<=34.9)
print("index:",index)
print(zayıf)
print(normal)
print(fazla_kilolu)
print(sisman)

#1.si true ise zayıf... şeklinde ilerler

vize1=float(input("1.vize notu:"))
vize2=float(input("2.vize notu:"))
final=float(input("final notu:"))
ort=((vize1+vize2)/2)*0.6+(final*0.4)
x=((ort>=50)and(final>=50))or(final==70)#true ise geçti
print(x)


x=y=[1,2,3]
z=[1,2,3]

print(x==y)
print(x==z)

print(x is y) #is operatörü adreslerin aynı olup olmadığına bakar
print(x is z)

a=[1,2,3]
b=[2,4]
del a[2]
b[1]=1
b.reverse()
print(x==y)
print(a is b)#farklı adresler


k=['apple','banana']

print('banana' in k)

name='nazli'
print('b' in name)



username='sadikturan'
password='1234'

if (username=='sadikturann'):
    if (password=='12345'):
        print('Hoş geldiniz')
    else:
        print('parola yanlış')
else:
    print('username yanlış')



x=float(input("1.sayi:"))
y=float(input("2.sayi:"))

if x>y:
    print("1.sayi 2.sayidan büyüktür")
elif x==y:
    print("1.sayi 2.sayiya eşittir")
else:
    print("2.sayi 1.sayidan büyüktür")



number=float(input('sayi:'))
if number>0:
    print('sayi pozitif')
elif number<0:
    print('sayi negatif')
else:
    print("girilen sayi 0'a esittir")




isim=input("isim:")
yas=int(input("yas:"))
egitim_durumu=input("egitim durumu:")
if (yas>=18) and ((egitim_durumu=='lise') or (egitim_durumu=='üniversite')):
    print('Ehliyet kursuna kayıt olabilirsiniz...')
else:
    print('Bu kursa kayıt olma şartlarına uymuyorsunuz...')





yazili1=float(input("1.yazili:"))
yazili2=float(input("2.yazili:"))
sozlu=float(input("sözlü:"))
ort=(yazili1+yazili2+sozlu)/3
if (ort>=0) and (ort<=24):
    print(f'ortalamanız:{ort},sonuc:0')
    print('Maalesef kaldınız!!!')
elif (ort>24) and (ort<=44):
    print(f'ortalamanız:{ort},sonuc:1')
elif (ort>44) and (ort<=54):
    print(f'ortalamanız:{ort},sonuc:2')
elif (ort>54) and (ort<=69):
    print(f'ortalamanız:{ort},sonuc:3')
elif (ort>69) and (ort<=84):
    print(f'ortalamanız:{ort},sonuc:4')
elif (ort>84) and (ort<=100):
    print(f'ortalamanız:{ort},sonuc:5')
    print('tebrikler!!!')
else:
    print('yanlıs bir bilgi girdiniz')
#Bugunün tarihini bulma işlemi
import datetime

t=datetime.date.today()
print(t)
"""

import datetime

simdi=datetime.datetime.now()
print(simdi)

tarih=input('aracınız hangi tarihte trafiğe çıktı:')
tarih=tarih.split('-')
x=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
gun=simdi-x
gun=gun.days
print(gun)

if gun<=365:
    print('1.servis aralığı')
elif (gun>365) and (gun<=365*2):
    print('2.servis aralığı')
elif (gun>365*2) and (gun<=365*3):
    print('3.servis aralığı')
else:
    print('hatalı süre bilgisi')





























