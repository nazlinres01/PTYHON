"""
sayilar=[1,3,5,7,9,12,19,21]

for a in sayilar:
    if a%3==0:
        print(a)

for a in sayilar:
    if a%2!=0:
        print(a**2)

toplam=0
for a in sayilar:
    toplam=toplam+a
print(toplam)



sehirler=['kocaeli','istanbul','ankara','izmir','rize','samsun','kars']
for a in sehirler:
    if len(a)<=5:
        print(a)

urunler =[
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S8','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'},
]
toplam=0
for urun in urunler:
    toplam=int(urun['price'])+toplam
print(toplam)

for urun in urunler:
    if int(urun['price'])<=5000:
        print(urun['name'])
x=1
while x<=100:
    if x%2!=0:
        print(f'sayi tektir... {x}')
    else:
        print(f'sayi çiftir... {x}')
    x+=1



name=''
while not name.strip():
    name=input('isminizi giriniz:')
print(f'Merhaba {name}')

"""








