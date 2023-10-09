"""
x=input('1.sayi:')
y=input('2.sayi:')
print(type(x))
print(type(y))
toplam=int(x)+int(y)#x+y olursa string olarak algılıyor.
print(toplam)

x=5
y=2.5
name='Çınar'
isOnline=True

#print(type(x))
#print(type(y))
#print(type(name))
#print(type(isOnline))



#x=float(x)
#print(x)
#print(type(x))

#y=int(y)
#print(y)
#print(type(y))


result=x+y
print(result)
print(type(result))

result=str(x)+str(y)
print(result)
print(type(result))



pi=3.14
r=input("Bir yarıçap giriniz:")#inputta tip dönüşümü yapmalıyız
#float(input("Bir yarıçap giriniz:"))
daireAlani=pi*(float(r)**2)
daireCevresi=2*pi*float(r)
print("dairealanı:",daireAlani)
print("dairecevresi:",daireCevresi)

print("alan:"+str(daireAlani)+" cevre:"+str(daireCevresi))
"""

name='Nazlı Nur'
surname='Esmeray'
age=18

greeting='My name is '+ name +' '+surname+' and \nI am '+str(age)+' years old.'
print(greeting)
print(greeting[0])#ilk harfin index numarası
#\n alt satıra geçmek için kullanılır
print(len(greeting))
print(greeting[len(greeting)-1])
print(greeting[-1])#sondaki harfin index numarası -1 den başlar
print(greeting[0:4])
print(greeting[3:])
print(greeting[:15])
print(greeting[0:40:2])#2 karakterden birini alır



























