"""
name='Nazli Nur Esmeray'

for letter in name:
    if letter=='z':
        break #N,a harfleri ekrana çıkar 
    print(letter)

for letter in name:
    if letter=='a':#a harfi hariç tüm harfler ekrana çıkar
        continue
    print(letter)

x=0
while x<5:
    if x==2:
        break #0,1 sayıları ekrana çıkar
    print(x)
    x+=1


x=0
while x<5:
    x+=1
    if x==2:
        continue #1,3,4,5 ekrana çıkar(2 hariç hepsi)
    print(x)
    
"""
y=0
toplam=0
while y<=100:
    y+=1
    if y%2==0:
        continue
    toplam+=y
print(toplam)
