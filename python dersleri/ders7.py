"""
#x=5
#y=10
#z=20

x,y,z=5,10,20

#x,y=y,x #x ile y değerleri değişiyor 
#x=x+5
#x+=5 #x=x+5
#x-=5 #x=x-5
#x*=5 #x=x*5
#x/=5 #x=x/5
#x%=5  #x=x%5
#x//=2 #x=x//2 #bölmedeki bölüm
#y**=5  #y=y**5 #üs alma
#print(x,y,z)


#values=1,2,3,4 #fazla veya eksik eleman olmamalı
values=1,2,3,4
print(values)
print(type(values))

x,y,*z=values #fazla olan eleman yıldızlı elemana dizi şeklinde ilerler
print(x,y,z)
print(x,y,z[1])



x,y,z=2,5,10
numbers=1,5,7,10,6

a=int(input("1.sayı:"))
b=int(input("2.sayı:"))

carpım=a*b
toplam=x+y+z
print(carpım-toplam)

print(y//x)

print(toplam%3)

print(y**x)

x,*y,z=numbers
print(x,y,z)
print(z**3)
print(y[0]+y[1]+y[2])



a,b,c,d=5,5,10,4

username='nazli'
password='12345'


#result= (a==b) #a b'ye eşit mi True
#result= (a==c) #a c'ye eşit mi  False
#result=('nzl'==username)
#result=(a!=b) #a b'ye eşit değil mi False
#result=(a!=c) #a 'c ye eşit değil mi True
result=(a>b) #a b'den büyük mü False
result=(a<c)
result=(a>=b)#birinin doğru olması o ifadenin doğru sayılmasına neden olur
result=(True==0) #False olur.
result=False+True+35
print(result)


sayi1=int(input("1.sayi:"))
sayi2=int(input("2.sayi:"))

                
result=(sayi1>sayi2)
print(result)




vize=float(input("vize notu:"))
final=float(input("final notu:"))
result=vize*(60/100)+final*(40/100)
print(result)
kontrol=(result>=50)
print(kontrol)



sayi=int(input("bir sayi giriniz:"))
sonuc=(sayi%2==0)#True ise çift değilse tek
print(sonuc)


sayi=int(input("bir sayi giriniz:"))
sonuc=(sayi>0)#True ise pozitif
print(f'girdiğiniz sayi {sayi} pozitif olma durumu ise {sonuc}')


email=input("e-mailinizi giriniz:")
password=input("parolanızı giriniz:")
sonuc_email=('email@sadikturan.com'==email)
sonuc_password=('abc123'==password)
print(sonuc_email)
print(sonuc_password)

x=6
#result=5<x<10
result=(x>5 and x<10) #ikisi de doğruysa True kabul edilir
result=(x>0)or(x%2==0) #birinin doğru olması yeterlidir,ikisi de doğru olabilir
result=not(x>0)
print(result)


sayi=float(input("bir sayi giriniz:"))
result=(sayi>0)and(sayi<100)
print(result)

sayi=float(input("bir sayi giriniz:"))    
result2=(sayi>0)and(sayi%2==0)
print(result2)

email=input("e-mailinizi giriniz:")
password=input("parolanızı giriniz:")
result3=('email@sadikturan.com'==email)and('abc123'==password)
print(f'giriş yapılabilir mi {result3}')


sayi1=int(input("1.sayi:"))
sayi2=int(input("2.sayi:"))
sayi3=int(input("3.sayi:"))
result4=(sayi1>sayi2)and(sayi1>sayi3)
#ikiside doğruysa sayi1 değeri en büyük (True)
print(result4)
result5=(sayi1<sayi2)and(sayi1<sayi3)
#ikiside doğruysa sayi1 değeri en küçük (True)
print(result5)
result6=((sayi1<sayi2)and(sayi1>sayi3))or((sayi1>sayi2)and(sayi1<sayi3))
#ikiside doğruysa sayi1 değeri ortanca (True)
print(result6)
result7=(sayi2>sayi3)
print(result7)


"""






































































































