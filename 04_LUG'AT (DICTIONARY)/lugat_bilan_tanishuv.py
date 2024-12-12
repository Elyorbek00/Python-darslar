#____________DICTIONARY____________________________
#__________LUG'AT BILAN ISHLASH_________________________
car_0 = {"model":"ferrari", "rang":"qizil"}
print(car_0["model"])
print(car_0["rang"])

en_uz = {'apple':'olma', 'apricor':"o'rik", 'banana':'banan'}
print(en_uz)  # lug'atni kurish
print(en_uz['apricor'])   # key bilan chaqrish

mevalar = {'olma':10000, 'tarvuz':15000, 'qovun':10000}
print(f'Olma narxi {mevalar['olma']} so\'m')   # olmani narxini chiqarish



## Lug'atda istalgan ma'lumot turlarini saqlash mumkin
talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
#Lug'atdagi qiymatlar son (int, float), matn (string), ro'yxat (list, tuple, set) va hatto boshqa lug'at ham bo'lishi mumkin.
print(f"{talaba_0['ism'].title()},\
    {talaba_0['t_yil']}-yilda tu'gilgan,\
    {talaba_0['yosh']} yoshda")             # malumotlarni chiqarish

#______________YANGI JUFTLIK QO'SHISH_________________________
talaba_0['kurs'] = 1     # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
talaba_0['fakultet'] = 'programming'    # 'fakultet' ga esa 'informatika' 
talaba_0['ism'] = 'abdulloh'    # ism key qiymatini uzgartirish
print(talaba_0)




#___________________BO'SH LUG'AT___________________________

talaba_1 = {}   # bo'sh lug'at
talaba_1 ['ism'] = 'Elyor Sharifov'
talaba_1 ['kurs'] = 1
talaba_1 ['yosh'] = 26
print(talaba_1)





#________Kalit so'z-qiymat o'chrib tashlash__________________________

talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(talaba_0)
del talaba_0['yosh']
print(talaba_0)




#____________Lug'atlarni bir nechta qatordan yozish____________________

telefonlar = {
    'ali':'iphone 15',
    'vali':'galaxy s21',
    'olim':'mi 20 pro',
    'orif':'nokia 3310'
}
print(telefonlar['ali']) # kalit suzi bilan chaqrish



#_____________get() metodi______________________
phone = telefonlar.get('hasan', 'Bunday ism mavjud emas')  # get orqali kaliti bilan chaqrish agar lug'ada mavjud bo'lmasa boshqa habar chiqadi
print(phone)





#_________________AMALIYOT________________________________

"""
otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi
Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
"""

"""
Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
"""

"""
Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
"""

"""
Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
"""

"""
Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
"""