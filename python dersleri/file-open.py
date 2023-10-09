"""
file=open("newfile.txt","r")
content=file.read()
print(content)
file.seek(15)#kürsörün yerini ayarlar
content2=file.read()
print(content2)
print(file.tell())#kürsörün yerini belirler
file.close()


with open("newfile.txt","r") as file:
    content=file.read()
    print(content)
kürsör,imleç(cursor)

"""

with open("newfile.txt","r+") as file:
    file.write("deneme")
with open("newfile.txt","r+") as file:
    print(file.read())

with open("newfile.txt","r+") as file:
    content=file.read()
    content="Ayşe Çelik\n"+content
    print(content)
