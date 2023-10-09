"""
def changeName(n):
    n='ada'

name='yiğit'

changeName(name)
print(name)

def change(n):
    n[1]='İstanbul'

sehirler=['ankara','izmir']
change(sehirler)
print(sehirler)

#fonksiyonsuz
sehirler2=['adana','malatya']
print(sehirler2)
sehirler2[0]='istanbul'
print(sehirler2)

def add(a,b,c=0):
    return sum((a,b,c))#sum toplama yapar

print(add(10,20))
print(add(5,20,20))


def add(*params):#(tuple olduğu için *)istediğin kadar parametre girebilirsin 
    print(type(params))
    print(params)
    return sum((params))

print(add(10,20,30,40,50))
print(add(1,2,3,4,5,6,7,8,9,10))

def displayUser(**args):#dictionary olduğu için **
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))
    
displayUser(name='Çınar',age=2,city='Ankara')
displayUser(name='Fatma',age=2,city='Ankara',phone='105023')
displayUser(name='Nazli',age=2,city='Ankara',phone='157865',email='esmer.naz@gmail.com')
"""
def myFunc(x,y,z,*args,**kwargs):
    print(x)
    print(y)
    print(z)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1='value1',key2='value2')



