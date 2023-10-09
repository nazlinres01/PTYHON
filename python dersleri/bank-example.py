"""
#def square(number): return number**2 # olabilir
square=lambda num: num**2 #isimsiz fonksiyon
numbers=[1,3,5,7,9,8,2]

result=list(map(square,numbers))
print(result)

#for item in map(square,numbers):
    #print(item)
x
def check_even(num): return num%2==0
numbers=[1,3,5,7,9,8,2]
result=list(filter(check_even,numbers))
#check_even(numbers[2]) indeksi 2 olan sayı çift değil bu yüzden false
print(result)


x='global x'
def function():
    x='local x'
    print(x)

function()
print(x)

name='Çınar'

def changeName(new_name):
    name=new_name
    print(name)

changeName('Ada')
print(name)


a=50
def test():
    global a # değişkenin başına global yazmadığımda 50, yazdığımda
    # fonksiyonun içindeki değer(100) ekrana çıkar
    print(f'a : {a}')
    
    a=100
    print(f'changed x to {a}')

test()
print(a)

"""
#Bankamatik olayını anlatan bir örnek
hesapA={
    'ad':'Nazlı Nur ESMERAY',
    'hesapNo':'156416541',
    'bakiye':5000,
    'ekhesap':4000
}
hesapB={
    'ad':'Nazlı Nur ESMERAY',
    'hesapNo':'156416541',
    'bakiye':1000,
    'ekhesap':2000
}
def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap['bakiye']>=miktar:
        hesap['bakiye']-=miktar
        print('paranızı alabilirsiniz.')
    else:
        toplam=hesap['bakiye']+hesap['ekhesap']
        if(toplam>=miktar):
            ekHesapKullanimi=input('ek hesap kullanılsın mı (evet/hayır)')
            if(ekHesapKullanimi=="evet"):
                ekHesapKullanilacakMiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-=ekHesapKullanilacakMiktar
                
                print('paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz,bakiye yetersiz')
paraCek(hesapA,10000)















































