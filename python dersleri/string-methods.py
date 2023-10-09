name='Nazli'
surname='Esmeray'
age=18


print('My name is {} {}'.format(name,surname))
print('My name is {1} {0}'.format(name,surname))
print('My name is {s} {n}'.format(n=name,s=surname))
print("My name is {} {} and I'm {} years old.".format(name,surname,age))


result=200/700
print('the result is {r:1.3}'.format(r=result))
#(1.3)1 sayısı baştan ne kadar boşluk bıraktığı 3 sayısı virgülden sonraki kısım
print(f"My name is {name} {surname} and I'm {age} years old.")


website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
uzunluk=len(website)
uzunluk2=len(course)


print(len(course))
print(website[7:10])
print(website[uzunluk-3:uzunluk])
print(course[:15])
print(course[(uzunluk2-15):])
print(course[::-1])#tersten yazdırma

isim='Nazlı Nur'
soyisim='Esmeray'
yas=18
meslek='mühendis'
print(f"Benim  adım {isim} {soyisim},Yaşım {yas} ve mesleğim {meslek}.")

kelime="Hello world"
print(kelime[0:6]+'W'+kelime[-4:])
print(kelime.replace('w','W'))

kelime2="abc"
print(kelime2*3)


message="Hello there . My name is Nazlı Nur Esmeray"
message=message.upper()#büyük harf
message=message.lower()#küçük harf
message=message.title()#her kelimenin başı büyük olur
message=message.capitalize()#sadece cümlenin başı büyük olur
message=message.strip()#ilk boşluk karakterini siler
message=message.split()#parçalara ayırma işlemi
message=message.split('.')
message=' *** '.join(message)#parçaları birleştirme

index=message.find('Nazlı')#bulunan kelimenin ilk harfinin index numarasını verir
isFound=message.startswith('H')#H karakteri ile mi başlıyor True endswith en sondaki harf
print(index)
print(isFound)
message=message.replace('Nazlı','Ahmet')
message=message.center(50,'*')
print(message)


#string method ile daha fazlasına ulaşabilirsin

















