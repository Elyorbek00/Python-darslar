

# ___________RO'YXATNI TARTIBLASH______________

# sort() -  ruyhatni alifbo va tartib raqam  buyicha tartiblab beradi
# sorted() - asil ruyhatga tegmagan holda ruyhatni tartiblash
# reverse=True - ruyhatni teskarisiga tartiblash
# reverse()  -  ro'yxatni ortidan boshiga qarab ugirib beradi


# ____________-_TARTIBLASH______________
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)




#___________KOTTA VA KICHIK HARIF________________
cars = ['Bmw', 'mercedes benz', 'volvo', 'general Motors', 'tesla', 'audi']
cars2 = cars.copy()
cars.sort()
print(cars)
cars2.append("malinu")
print(cars2)



# _________TESKARI TARTIBLASH____________________
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)



#______________SORTED()______________________
# asil ro'yxatni tegmagan holda tartiblab consolga chiqarish 
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
print(cars)
print(sorted(cars))


# asil ruyhatga tegmagan holda tartiblash va ruyhatni teskari tariblash
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
print(cars)
print(sorted(cars, reverse=True))



#___________SONLI RO'YXATLAR__________________

# sorted() - ruyhatni uzgartirmagan holda sonlarni tartiblash
sonlar = [12, 45, 56, 78, 69, 668, -15, -20, - 35, -8.5, -9.6]
print(sorted(sonlar))

# sort() -  ruyhatni alifbo va tartib raqam  buyicha tartiblab beradi
#sorted() - asil ruyhatga tegmagan holda ruyhatni tartiblash
#reverse=True - ruyhatni teskarisiga tartiblash
ages = [12, 45, 56, 78, 69, 668, -15, -20, - 35, -8.5, -9.6]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))




# __________RO'YXATNI AYLANTRISH_____________

# .reverse() - ro'yxatni ortidan boshiga qarab chiqarish
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.reverse()
print(cars)




# ______RO'YXATNI UZUNLIGINI TOPISH___________

#len() - ruyxt ichidagi elemetlarni uzunligini sanab beradi
sonlar = [12, 45, 56, 78, 69, 668, -15, -20, - 35, -8.5, -9.6]
print('Elementlar soni: ', len(sonlar))
# Natija: Elementlar soni: 11




# ________RANGE() FUNKSIYASI_____________

#range() - Malum bir oraliqdagi sonlarni qaytaradi
sonlar = list(range(0,10)) 
print(sonlar)
# Natija: [0,1,2,3,4,5,6,7,8,9]

sonlar = list(range(1,11)) 
print(sonlar)
# Natija: [1,1,2,3,4,5,6,7,8,9,10]




#_______RANGE VA QADAM_____________

# range() yordamida qadamni ham berishimiz mumkun
juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
print("Juft sonlar ", juft_sonlar)
print("Toq sonlar ", toq_sonlar)
# Natija: Juft sonlar  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# Natija: Toq sonlar  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]




# ___MIN(), MAX(), SUM()___

narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print("Eng arzon narx ", arzon, \
    "Eng qimmat ", qimmat, \
        "Jami ", jami)
# Natija: Eng arzon narx  5600 Eng qimmat  32874 Jami  116164



#_______RO'YXATNI KESISH__________

# ro'yxatni indekis orqali kesib olish
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:3]
print(my_cars)
# Natija: ['bmw', 'mercedes benz', 'volvo']


# remoce()  -  Ro'yxatdagi biron bir malumotni uchirish 
cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.remove('bmw')
print(cars)





#___________RO'YXATDAN NUSXA OLISH___________

# lisdan boshqa listga nusxa chuchirish uchun [:] foydalanamiz listni to'liq kuchirib oladi
sonlar = [1,2,3,4,5,6,7]
nusxa = sonlar[ : ] # nusxa ga sonlar dan nusxa olish
nusxa.append(8) # nusxa ga 8 sonini qushish

print(sonlar)
print(nusxa)
# Natija:  [1, 2, 3, 4, 5, 6, 7]
#          [1, 2, 3, 4, 5, 6, 7, 8]




#_____________TUPLES_______________

# listni butunlay chaqrish
toys = (20, 30, 55.2)
print(toys)

# index bo'icha chaqirish
toys = ('bua', 'car', 'bear', 'dino', 'snake', 'lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])

# tuples ga yangi qiymat qushib bo'lmaydi 
toys = ('bua', 'car', 'bear', 'dino', 'snake', 'lizard')
toys[3] = 'dragon'
print(toys)
# Natija:  xatolik beradi

#________________TUPLES<->LIST_______________
toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantrish
# ro'yxatga uzgartrisk kritish
toys.append('dragon') # ro'yxat ohiriga qushish
toys.remove('bus') # ro'yxatdagi bita elementni uchrish
toys[1] = 'mcqueen' # yo'yxatni 1 indexsiga yangi elementbilan yangilash
toys = tuple(toys) # Ro'yxatni qaydadan o'zgarmas ro'yxatga (Tuple) aylantramiz
print(toys)





#   ________________AMALIYOT_________________

#__________1.amaliyot_________________
# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Malayziya", "Singapur", "AQSh"]
print(davlatlar)

#Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True) )

#Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)




#__________2.amaliyot_________________
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120,1200,2))
print(sonlar)

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
sonlar = list(range(120,1200))
jami = sum(sonlar)
print(jami)

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
sonlar = list(range(120,1201))
print(max(sonlar) - min(sonlar))


# Ro'yxatdagi elementlar sonini hisoblang
sonlar = list(range(120,130))
print(len(sonlar))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
sonlar = list(range(1,101))
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[40:61])




#__________3.amaliyot_________________
# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh','somsa','norin','shashlik','qozonkabob']
#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('qozonkabob')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')
#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"