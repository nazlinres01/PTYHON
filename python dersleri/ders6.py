"""
list=[1,2,3]
tuple=(1,'iki',3)
print(type(list))
print(type(tuple))

print(list[2])
print(tuple[1])

print(len(list))
print(len(tuple))


list=['ali','veli']
tuple=('nazli','ayşe','ayşe')#tek bir elemanda değişiklik yapamıyoruz
tuple=('gül','emel','ayşe')+tuple

print(list)
print(tuple)

print(tuple.count('ayşe'))
print(tuple.index('ayşe'))





sehirler=['kocaeli','istanbul']
plakalar=[41,34]

print(plakalar[sehirler.index('kocaeli')])



plakalar={'kocaeli':41,'istanbul':34}

print(plakalar['kocaeli'])
print(plakalar['istanbul'])

plakalar['kocaeli']='new value'
plakalar['ankara']=6
print(plakalar)




users={
    'sadikturan':{'age':36,
                  'email':'sadik@gmail.com',
                  'roles':['admin','user'],
                  'address':'istanbul',
                  'phone':25641501},
    'cinarturan':{'age':19,
                  'email':'cinar@gmail.com',
                  'roles':['user'],
                  'address':'sakarya',
                  'phone':24165468},

    
}

print('age:',users['cinarturan']['age'])
print(users['cinarturan']['email'])
print(users['cinarturan']['address'])
print(users['cinarturan']['phone'])
print(users['sadikturan']['roles'][0])


ogrenciler={}
x=input('ad:')
y=input('soyad:')
z=input('telefon:')

ogrenciler['ad']=x
ogrenciler['soyad']=y
ogrenciler['telefon']=z


print(ogrenciler)

ogrenciler2={}
numbers=input('öğrenci numarası gir:')

ogrenciler2[numbers]=ogrenciler
print(ogrenciler2)

"""


"""
ogrenciler={}
number=input("öğrenci nosu:")
name=input("öğrenci adı:")
surname=input("öğrenci soyadı:")
phone=input("öğrenci telefonu:")

ogrenciler[number]={
    'ad':name,
    'soyad':surname,
    'telefon':phone

}

print(ogrenciler)

ogrenciler={}
number=input("öğrenci nosu:")
name=input("öğrenci adı:")
surname=input("öğrenci soyadı:")
phone=input("öğrenci telefonu:")

ogrenciler.update({
    number:{
    'ad':name,
    'soyad':surname,
    'telefon':phone
      
    }

})
print(ogrenciler)

ogrNo=input('öğrenci no:')
ogrenci=ogrenciler[ogrNo]
print(ogrenci)


#ekrana yazdırıldığı zaman her seferinde listedekilerin yeri farklı oluyor
fruits={'orange','apple','banana','tomato'}

#print(fruits[0]) #indekslenemez

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape','apple'])#elemanlar listede tekrarlanmaz


print(fruits)

#myList=[1,5,5,6,5,8,7,4,7,4,4,4,4,4,4,4,4,4,4]
#print(set(myList))#sayılar tekrarlanmaz

fruits.remove('mango')
fruits.discard('apple')#silme işlemini yapıyor


print(fruits)
fruits.clear()
print(fruits)

"""
#value types=>string,number
x=5
y=25
x=y
y=10
print(x,y)#çıktı 25 10



#reference types=>list  adresler eşitleniyor
a=["apple","banana"]
b=["apple","banana"]

a=b
b[0]="grape"
print(a,b)






















