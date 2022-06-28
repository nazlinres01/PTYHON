"""
liste=["1","2","5a","10b","abc","10","50"]
for list in liste:
    try:
        result=int(list) #dönüşüm bu şekilde yapılır
        print(result) 
    except:
        continue #hatalı elemanlar yazılmayacak

while True:
    eleman=input("eleman:")
    if eleman=='q':
        break
    try:
        sonuc=int(eleman)
        print(sonuc)
    except:
        print("sayısal ifade girilmelidir.")

turkce_karakterler="çğıöşüİ"

parola=input("parola:")

for i in parola:
    if i in turkce_karakterler:
        raise TypeError('parola türkçe karakterler içermemelidir')
    else:
        pass
print('geçerli parola')
          
"""
def faktoriyel(x):
    x=int(x)

    if x<0:
        raise ValueError("Negatif değer")
    sonuc=1
    for i in range(1,x+1):
        i+=1
        sonuc*=i
    return sonuc

for x in [5,10,20,-3,'10v']:
    try:
        y=faktoriyel(x)
    except ValueError as err:
        print(err)
        continue

    print(y)


