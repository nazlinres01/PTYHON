#error =>hata

#print(a) =>NameError
#int('1a2') =>ValueError
#print(100/0) =>ZeroDivisionError
#print('naz'li) =>SyntaxError
#error handling =>hata yönetimi
"""  
while True:
    try:
        x=int(input('x:'))
        y=int(input('y:'))
        print(x/y)

    except Exception as hata:#hatanın türü 
        print('hatalı bilgi girdiniz.')
        print(hata)
    else:
        print('her şey yolunda.')
        break
    finally:
        print('try except sonlandı.')#her seferinde çıkar

 
except (ZeroDivisionError,ValueError) as e:
    print('yanlış bilgi girdiniz.')
    print(e)#hatanın ismi veriliyor

except ZeroDivisionError:
    print('y için 0 girilemez.')

except ValueError:
    print('x ve y için sayısal değer girmelisiniz.')
"""

def check_password(psw):
    import re
    if len(psw)<7:
        raise Exception('parola en az 7 karakter olmalıdır')
    elif not re.search("[a-z]",psw):
        raise Exception("parola küçük harf içermelidir.")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf içermelidir.")
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam içermelidir.")
    elif not re.search("[_@$]",psw):
        raise Exception("parola alpha numeric karakter içermelidir.")
    elif re.search("\s",psw):
        raise Exception("parola boşluk içermemelidir.")

password="1234567aP@"

try:
    check_password(password)
except Exception as hata:
    print(hata)
finally:
    print("validation tamamlandı")
