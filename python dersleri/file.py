"""
dosya açma ve yazma işlemleri
file=open("newfile.txt","w")#python klasörü içerinde dosya oluşur
file.close()
file=open("C:/Users/nazlı.hp-pc/Desktop/newfile2.txt","w")
print(file)
file.close()

#w dosya açma
#a dosyaya yazı ekleme,çalıştırdıkça üzerine eklenir
file=open("newfile.txt","a")#türkçe karakter için encoding='utf-8'
file.write("\nZehra")
file.close()

file2=open("newfile2.txt","x")#dosya oluşturma tekrar çalıştırıldığında hata verir
file2.close()



file=open("newfile.txt","r")
#for i in file:
    #print(i,end="") #boş satır ekleme
#file.close()

content=file.read(5) #5 yazarsam içeri ilk 5 harfi alır yazmazsam hepsini okur
print(content)
file.close()


file=open("newfile.txt","r")
print(file.readline(),end="")
print(file.readline(),end="")
file.close()
"""
file=open("newfile.txt","r")
liste=file.readlines()
print(liste[0])
print(liste[1])
