

#______________KITOB_________________________
# Foydalanuvchi kritgan  son 0 dan kota bo'lsa "musbat son " deb konsolga chiqaring
son = int(input("Istalgan son kriting: "))
if son>0:
    print(son, "musbat son")


# Yuqoridagi dasturda foydalanuvchi yoshini so raymiz. Agar foydalanuvchi 7 yoshdan kichik bo lsa, "Sizga avtobus bepul", aks holda (else), "Chipta narxi 5000 so'm" degan yozuvni konsolga chiqaramiz.
yosh = int(input("Yoshingizni kriting: "))
if yosh <= 7:
    print("Sizga avtobus tekin")
else:
    print("Chipta narxi 2000 so'm")



#______________IF-ELSE__________________________

avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    else: # aks holda ... 
        print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yoz.


#________QIYMATLARNING TENG EMASLIGINI TEKSHIRISH_____________________

# Demak kodning 2-qatorida ism ichidagi qiymat 'ali' ga teng bo'lmasa "Uzr, {ism} biz Alini kutyapmiz" degan xabarni chiqar dedik. Aks holda (else), "Salom, Ali" degan xabar chiqadi.
ism = input("Ismingiz nima?\n>>>")
if ism.lower() != "ali":
    print(f"Uzur, {ism.title()} biz Alini kutayabmiz.")
else:
    print("Salom, Ali")


#___________SONLARNI SOLISHTIRISH_________________________

# foydalanuvchidan 12x6 ni surang javobi 72 bo'lsa "Javob to'g'ri dehan" habar chiqaring aks xolda "Javob xato" degan habar chiqsin
javob = float(input("12x6 nechiga teng:?>>>"))
if javob!=72:
    print("Javob xato")
else:
    print("Javob to'g'ri")



# Foydalanuvchi yoshi 18 dan kota bo'lsa yoki teng "Dasturga xush kelibsiz." degan habar chiqsin aks holda "Dasturga kirish mumkun emas!" desin
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18:
    print("Dasturga xush kelibsiz.")
else:
    print("Dasturga kirish mumkun emas!")


# foydalanuvchidan Yangi login kritishini surang login 5 ta harifdan kam bo'lsa "Login 5 harifdan ko'proq bo'lishi shart!" degan matin chiqsin
login = input("Yangi login tanlang: ")
if len(login)<=5:  # Login uzunligini tekshiramiz
    print("Login 5 harifdan ko'proq bo'lishi shart!")


# Foydalanuvchidan "To'g'ilgan yilingizni kriting:" kritishini surang
# agar yoshi 18 yoshdan kichik bo'lsa "Yoshingiz {yosh} da ekan" "Krish mumkun emas!" degan habar chiqsin aks holda "Xush kelibsiz" xabari chiqsin
yil = int(input("To'g'ilgan yilingizni kriting:"))
if 2024-yil<18:
    print(f"Yoshingiz {2024-yil}da ekan.")
    print("Krish mumkun emas!")
else:
    print("Xush kelibsiz!")


yosh = int(input("Yoshinizni kriting: "))
if yosh > 65: print("Siz COVUD-19 risk guruhida ekansiz")


x, y = 25, 50
print(x>y) if x>y else print("x<y")




#_______________________AMALIYOT_____________________________________

#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())



#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.

login = input("Login kriting: ")
if login.lower() == "admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}")


# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
son1 = int(input("1 sonni kriting: "))
son2 = int(input("2 sonni kriting: "))
if son1==son2:
    print(f"Sonlar teng: {son1}={son2}!")


# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.

son = int(input("Istalgan son kriting: "))
if son < 0:
    print(f"{son} Manfi son ")
elif son>0:
    print(f" {son} Musbat son ")
else:
    print(f"Son {0} teng")


# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
son = float(input('Istalgan son kiriting: '))
if son>0:
    print(son**(1/2))
else: 
    print('Musbat son kiriting')