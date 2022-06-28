"""
#list=[1,2,3]


for item in range(10):#0,1,2,3,4,5,6,7,8,9 bu sayıları ekrana yazar.
    print(item)

for item in range(5,10):#5,6,7,8,9 bu sayıları ekrana yazar.
    print(item)

for item in range(50,100,10):#50,60,70,80,90 bu sayıları ekrana yazar.
    print(item)

print(list(range(5,100,10)))

index=0
greeting="Hello"

for letter in greeting:
    print(letter,index)#letter yerine greeting[index] yazılabilir
    index+=1


for item in enumerate(greeting):#(0, 'H') şeklinde çıktı
    print(item)

for index,letter in enumerate(greeting):
    print(f'index: {index} letter: {letter}')


list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for a,b,c in zip(list1,list2,list3):
    print(f'list1: {a} list2: {b} list3: {c}')

"""
numbers=[]
for x in range(10):
    numbers.append(x)
print(numbers)


numbers=[x for x in range(10)] #listeleme olayı
print(numbers)

numbers2=[x**2 for x in range(10) if x%3==0]
print(numbers2)


myString="Nazli"
myList=[letter for letter in myString]
print(myList)


years=[1983,1956,1966,1967,1994,2001]
print(years)

ages=[2020-year for year in years]
print(ages)

result=[x if x%2==0 else 'TEK' for x in range(1,10)]
print(result)
result2=[(x,y) for x in range(3) for y in range(3)]
print(result2)




















