import datetime

simdi=datetime.datetime.now()
print(simdi)

tarih=input('aracınız hangi tarihte trafiğe çıktı:')
tarih=tarih.split('-')
x=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
gun=simdi-x
gun=gun.days
print(gun)
