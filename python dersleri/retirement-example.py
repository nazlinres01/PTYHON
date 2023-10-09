list=[1,2,3,4]
list.append(5)#üzerine ekleme metodu
list.pop()#silme metodu
print(list)

myString="Hello"
print(type(myString))
print(myString.upper())#büyük harfe çevirme
print(help(myString.upper))
#fonksiyonlar
def sayHello(name='user'):
    print("Hello "+name)

sayHello("ayşe")
sayHello()#parametre verilmiyorsa name='user' bilgisinden dolayı ekrana user çıkar 


def sayHello2(name):
    return 'Hello '+name
print(sayHello2('NAZLİ'))


def total(num1,num2):
    return num1+num2
print(total(10,20))


def yasHesapla(dogumYili):
    return 2020-dogumYili

ageCinar=yasHesapla(2017)
print(ageCinar)


def EmekliligeKacYilKaldi(dogumYili,isim):
    '''
    DOCSTRİNG:Dogum yiliniza gore emekliliginize kac yil kaldi
    İNPUT:Dogum Yili
    OUTPUT:Hesaplanan Yil Bilgisi
    '''
    yas=yasHesapla(dogumYili)
    emeklilik=65-yas
    if emeklilik>0:
        print(f'emekliliğinize {emeklilik} yıl kaldı...')
    else:
        print('Zaten emekli oldunuz...')
EmekliligeKacYilKaldi(1940,'Ali')
print(help(EmekliligeKacYilKaldi))#help nasıl kullanıdığı felan vs bilgi veriyor
       
    
