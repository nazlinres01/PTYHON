"""
numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']

#numbers[4]=40

#numbers.append(49)#sona eleman ekleme
#numbers.insert(3,78)#3.indexe 78 rakamını ekler.Konumunu biz belirleriz
#numbers.pop(0)#ilk elemanı siler parantez içine index numarası yazılır
#numbers.remove(5)#parantez içindeki sayıyı siler
numbers.sort()#küçükten büyüğe sıralama
#letters.sort()#baştan sıralama
numbers.reverse()#ters çevirme işlemi
#val=min(numbers)
val2=max(numbers)
val3=min(letters)
val4=max(letters)

val=numbers[4:]
print(val)
print(val2)
print(val3)
print(val4)


print(letters)

print(len(numbers))
print(len(letters))
print(numbers.count(10))
print(letters.count('a'))

numbers.clear()#listeyi temizler
print(numbers)


names=['Ali','Yağmur','Hakan','Deniz']
years=[1998,2000,1998,1987]


#print(names.append('Cenk'))

#print(names.insert(0,'Sena'))

print(names.index('Deniz'))
print(names.remove('Deniz'))
result='Ali' in names
print(result)
print(names.reverse())
print(years.reverse())
print(names.sort())
print(years.sort())
print(sonuc)
print(min(years))
print(max(years))
print(years.clear())



str="Chevrolet,Dacia"
sonuc=str.split(',')
print(sonuc)

"""


markalar=[]
x=input('marka1:')
y=input('marka2:')
z=input('marka3:')
markalar.append(x)
markalar.append(y)
markalar.append(z)

print(markalar)
























