#_______________.items() METODI__________________
#Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin.
talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4 
    }
print(talaba_0.items())

#Bu metodni to'g'ridan-to'g'ri emas, for tsikli yordamida chaqirish orqali lug'atdagi barcha elementlarni tushunarliroq shaklda ko'rishimiz mumkin.
for key,value in talaba_0.items():
    print(f"key:{key}")
    print(f"Value:{value} \n")



# Bu usul ba'zi lug'atlardagi ma'lumotlarni chiroyli ko'rinishda chiqarish uchun juda qo'l keladi
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for key,value in telefonlar.items():
    print(f"{key.title()}ning telifoni {value}")




#____________.keys() METODI________________________
#Agar lug'atdagi kalit so'zlarni ko'rish talab qilinsa, .keys() metodidan foydalanishimiz mumkin.

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
print(mahsulotlar.keys())


print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())
    
#Yuqoridagi kodimizda, for tsiklida .keys() metodini ishlatmasak ham huddi shu natija chiqadi.





bozorlik = ['anor', 'uzum', 'non', 'baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

#Yuqordagi kodga e'tibor bering. Biz avval borolik degan ro'yxat yaratdik (uyga bozor qilyapmiz), keyin esa mahsulotlar lug'atidagi har bir mahsulotni bizdagi bozorlik ro'yxati bilan solishtirdik. Agar mahsulot bizning bozorlik ro'yxatimizda bo'lsa, uning narxini konsolga chiqardik.



#Yuqordagi kodga e'tibor bering. Biz avval borolik degan ro'yxat yaratdik (uyga bozor qilyapmiz), keyin esa mahsulotlar lug'atidagi har bir mahsulotni bizdagi bozorlik ro'yxati bilan solishtirdik. Agar mahsulot bizning bozorlik ro'yxatimizda bo'lsa, uning narxini konsolga chiqardik.
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")



#___________________LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH_______________________

print("Do'konimizdagi magsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())





#______________.values() METODI

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

print(telefonlar.values())






print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in telefonlar.values():
    print(tel)

#Yuoqirdagi natijaga e'tibor bersanigz, bir nechta foydalanuvchilar iphone x va galaxy s9 telefonidan foydalanishar ekan, va bu modellar qayta-qayta konsolga chiqdi.



#_______________set() funktsiyasi
# Buning oldini olish uchun set() funktsiyasidan foydalanishimiz mumkin.
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in set(telefonlar.values()):
    print(tel)






#____________________AMALIYOR______________________________________

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.



# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.



# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.



#  Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.