"""
list=[1,2,3,4]
result=type(list)
print(result)

#object = instance



class Person:
    #class attributes
    adress='no information'
    #constructor(yapıcı metod)
    def __init__(self,name,year):#self oluşturulan objeleri temsil eder
        #object attributes
        self.name=name
        self.year=year
        print("init metodu çalıştı")
    #method
    def intro(self):
        print("Hello There")

    def calculate(self):
        return 2019-self.year

p1=Person('ayşe',1860) # p1 objesi tanımlanmış oldu
p1.adress='sakarya'
print(f'name: {p1.name} year: {p1.year} adress: {p1.adress}' )
p1.intro()
print(p1.calculate())
print(p1)
print(type(p1))



class Circle:
    #class object attribute
    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    #methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap

    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)

c1=Circle()#yaricap=1
c2=Circle(5)

print(f'çevre:{c1.cevre_hesapla()} ve alan:{c1.alan_hesapla()}')
print(f'çevre:{c2.cevre_hesapla()} ve alan:{c2.alan_hesapla()}')    



#Inheritance(Kalıtım)=>miras alma durumu
class Person():
    def __init__(self):
        print('Person Created')
class Student(Person):
    pass

p1=Person()
s1=Student()
print("*************")
class Person():
    def __init__(self):
        print('Person Created')
class Student(Person):
    def __init__(self):
        print('Student Created')

p1=Person()
s1=Student()
print("*************")

class Person():
    def __init__(self):
        print('Person Created')
class Student(Person):
    def __init__(self):
        Person.__init__(self)
        print('Student Created')

p1=Person()
s1=Student()

"""

mylist=[1,2,3]
print(len(mylist))


class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print('Movie objesi oluşturuldu')

    def __str__(self):
        return f"{self.title} and {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("Movie objesi silindi")
m=Movie("film adı"," yönetmenin adı",120)
print(len(m))
del m
print(m)
















