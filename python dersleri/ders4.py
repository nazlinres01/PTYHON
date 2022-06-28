"""
website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

sonuc=' Hello World '
sonuc=sonuc.strip()#lstrip()soldaki boşluk rstrip() sağdaki boşluk
print(sonuc)

#website=website.strip(':/htpw.moc')
#print(website)

course=course.lower()
print(course)

#website=website.count('a')
#print(website)

#website=website.startswith('www')
#website=website.endswith('com')
#print(website)


website=website.find('com',0,10) #0 ile 10(index numaraları) arasında arar 
print(website)#rfind() sağdan başlama  find yerine index de kullanılır
#farkı index de hata geliyor

result=course.isalpha()#harf kontrolü
print(result)

result2='4561'.isdigit()#rakam kontrolü
print(result2)
 
result3='Contents'.center(50,'*')
print(result3)


result4='Contents'.ljust(50,'*')
print(result4)


result5='Contents'.rjust(50,'*')
print(result5)


result6=course.replace(' ','-')
print(result6)

result7='Hello World'.replace('World','There')
print(result7)

result8=course.split(' ')
print(result8)
print(result8[2])


my_list=[1,2,3]
my_list=['bir',2,True,5.6]
print(my_list)


list1=['one','two','three']
list2=['four','five','six']

numbers=list1+list2
print(numbers)
print(len(numbers))
print(numbers[2])


userA=['Sadık',36]
userB=['Nazlı',18]

users=[userA,userB]
print(users[1])
print(users[1][0])



arac=['Bmv','Mercedes','Opel','Mazda']
aracc=len(arac)
print(aracc)
print(arac[0])
print(arac[-1])
arac[-1]='Toyata'
arac3=arac
print(arac3)

arac4='Mercedes' in arac
print(arac4)

arac5=arac[-2]#-2 indexinde yer alan kelime
print(arac5)
print(arac[:aracc-1])
arac[-2:]=['Toyota','Renault']
print(arac)
arac+=['Audi','Nissan']
print(arac)
del arac[-1]
print(arac)

print(arac[::-1])

"""

studentA=['Yiğit','Bilgi',2010,[70,60,70]]
studentB=['Sena','Turan',1999,[80,80,70]]
studentC=['Ahmet','Turan',1998,[80,70,90]]

print(studentA[3][1])
print(studentB)
print(studentC)
toplam=studentA[3][1]+studentB[3][0]

result=f"{studentA[3][1]} + {studentB[3][0]} = {toplam} herhangi 2 öğrencinin herhangi 2 notunun toplamı"    
print(result)




