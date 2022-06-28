"""
#quiz uygulaması var onu da yapmalısın
#import math #math modulü
import math as islem  #kendimiz isim verebiliriz ve bu isimle çağırabiliriz
#value=dir(math)#metodlar bulunur
#value=help(math)#metodları açıklar
#value=help(math.pow)#sadece üs alma olayını açıklar
#value=math.sqrt(64)
#value2=math.factorial(4)
#value3=math.floor(5.7)#çıktı 5
#value4=math.ceil(5.6)#çıktı 6
value5=islem.pow(4,2) 
#print(value)
#print(value2)
#print(value3)
#print(value4)
print(value5)


#from math import * #hepsini kabul eder
from math import factorial,sqrt,ceil
value=factorial(5)
value2=sqrt(9)
value3=ceil(4.3)
print(value)
print(value2)
print(value3)


import random
result=dir(random)
result=help(random)
result=random.random()#0.0 - 1.0 arasında rastgele sayı üretilir
result=random.random()*100 # üretilen sayılar 100 ile çarpılır
result=random.uniform(1,10)# 1 ile 10 arasında sayı üretilir
result=int(random.uniform(1,10)) #1 ile 10 arasındaki tam sayılar üretilir
result=random.randint(1,100) # 1 ile 100 arasındaki tam sayılar üretilir

greeting="hello there"
names=['ali','yağmur','deniz','cenk','ahmet','mustafa']
result=names[random.randint(0,len(names)-1)]
result=random.choice(names)#bu metodla isimler rastgele seçiliyor
result2=random.choice(greeting)

liste=list(range(10))
random.shuffle(liste) # listedeki elemanlar rastgele atanıyor
result3=liste

liste2=range(100)
result4=random.sample(liste2,4) #rastgele 4 sayı seçiliyor ve liste içerisinde
result5=random.sample(names,2)
print(result)
print(result2)
print(result3)
print(result4)
print(result5)

"""
'''
    Modül hakkında bilgilendirme 
'''
print('modül eklendi.')
number=10
numbers=[1,2,3]

person={
    "name":"Ali",
    "age":25,
    "city":"İstanbul"

}

def func(x):
    '''
    fonksiyon hakkında bilgilendirme
    '''
    print(f'x:{x}')

class Person:
    def speak(self):
        print("I'am speaking...")

























