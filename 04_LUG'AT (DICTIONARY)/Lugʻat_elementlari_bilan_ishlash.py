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