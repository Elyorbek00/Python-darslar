
#_______________STRING VA UNICODE_______________________________

#STRING (matn) — Pythondagi eng mashxur ma'lumot turlaridan biri.  O'zgaruvchiga matn yuklash uchun matn qo'shtirnoq (" ") yoki birtirnoq (' ') ichida yozilishi kerak.
smail = "☎ va 😂"         # icon olish siyte  https://symbl.cc/
print(smail)



# Matnlarni qo'shish operatori (+)
# Matnlarni qo'shish uchun + operatoridan foydalanmiz:
ism = "elyor"
print("Mening ismim " + ism)

ism = "Elyor"
familiya = "Sharifov"
print(ism + familiya)   # faqat  +  quysak matini orasida joy qolmaydi qushib quyadi 
print(ism + ' ' + familiya)   # bu 2 ta matini orasiga joy tashab ketadi 







# ___________f - string____________________

#Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish uchun f-string usulidan f"{matn1} {matn2}" ham foydalansak bo'ladi:
ism = "Elyor"
familiya = "Sharifov"
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)


ism = "Elyor"
familiya = "Sharifov"
print(f"Mening ismim {ism}. {ism} {familiya}!") 






#__________MAHSUS BELGILAR____________________

# Matnga bo'shliq qo'shish uchun \t belgisidan, yangi qatordan boshlash uchun \n belgisidan foydalanamiz:
print('Hello World')
print('Hello\tWorld')   # \t - bir muncha bushliq qoldirish
print('Hello \nWorld')  # \n - suzlarni keyingi qatordan yozish






#_________STRING METODLAR______________________

# #Pythonda string ustida amalga oshirish mumkin bo'lgan tayyor amallar to'plami mavjud. Bunday amallar to'plami metodlar deb ataladi.

ism = "elYor"
familiya = "shariFov"
ism_sharif = f"{ism} {familiya}"  
ism_sharif = ism_sharif.upper()    # Uzgaruvchini ham kota harif qilib yozish mumkun 
print(ism_sharif.upper())          #  .upper() metodi matndagi har bir harfni katta harfga o'zgartiradi. 
print(ism_sharif.lower())          #  .lower() - metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.
print(ism_sharif.title())          #  .title() - metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.
print(ism_sharif.capitalize())     #  .capitalize() - esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.



meva = '   olma   '
print("Men " +meva.lstrip() + " yahshi kuraman" )     # .lstrip() — matn boshidagi bo'shliqni,
print("Men " +meva.rstrip() + " yahshi kuraman" )     # .rstrip() – matn oxiridagi bo'shliqni,
print("Men " +meva.strip() + " yahshi kuraman" )      # .strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi 
print("Men " +meva + " yahshi kuraman" )              #  metod quymasak bush joylarni olib tashlamaydi uz holicha chiqarib beradi 





#_______________INPUT — FOYDALANUVCHI BILAN MULOQOT___________________

ism = input("Ismingiz nima? ")          # input() -   USER dan malumot kritishini suraydi
print("Assalomu alaykum, "  + ism)

ism = input("Ismingiz nima?\n>>>")    # Foydalanuvchi ismini yangi qatordan kiritadi
print("Assalom alaykum, " + ism.title())






#_________________AMALIYOT__________________________

# _____1-amaliyot______
# Quyidagi o'zgaruvchilarni yarating:
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"

print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati")




#____________ 2-amaliyot______________
#Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.

kocha = input("ko'changizni kriting? ")
mahalla=input("Mahallangizni kiriting? ")
tuman=input("Tumaningizni kriting? ")
viloyat=input("Viloyatingizni kriting? ")

print(f"{kocha.title()} ko'chasi, {mahalla.title()} mahalasi, {tuman.title()} to'mani, {viloyat.title()} viloyati")




#__________3.amaliyot_________________
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"

print(f"{kocha} ko'chasi, \n{mahalla} mahalasi, \n{tuman} to'mani, \n{viloyat} viloyati")




#__________4-amaliyot________________
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
malumot = f"{kocha.title()} ko'chasi, \n{mahalla.lower()} mahalasi, \n{tuman.capitalize()} to'mani, \n{viloyat.upper()} viloyati"

print(malumot)


