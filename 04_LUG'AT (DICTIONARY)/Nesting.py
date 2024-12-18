#_________________NESTING________________________
#Ba'zida dasturlash jarayonida lug'atning ichida ro'yxatlar yoki boshqa lug'atni, yoki aksincha ro'yxat ichida lug'atni saqlash ham qo'l kelishi mumkin. Bu ingliz tilida Nesting deyiladi. Nesting Pythondagi foydali xususiyatlardan biri.





#____________________LUG'ATLAR RO'YXATI________________________
car0 = {
    'model':'laxetti',
    'rang':'oq',
    'yil':2021,
    'narx':13000,
    'km':50000,
    'karobka':'avtomat'
}

car1 = {
    'model':'nexia 3',
    'rang':'oq',
    'yil':2022,
    'narx':9000,
    'km':550000,
    'karobka':'avtomat'
}

car2 = {
    'model':'gentra',
    'rang':'oq',
    'yil':2024,
    'narx':15000,
    'km':20000,
    'karobka':'avtomat'
}




# Agar biz har bir lug'atga alohida murojat qiladigan bo'lsak, lug'atlarning nomlarini yodlab qolishimiz talab qilinar edi:

car = car0   # Ro'yxatni bita bita chiqarish
print(f"{car['model'].title()}, "
      f"{car['rang']} rang, "
      f"{car['yil']}-yil, "
      f"{car['narx']}$ ")

car = car1   # Ro'yxatni bita bita chiqarish
print(f"{car['model'].title()}, "
      f"{car['rang']} rang, "
      f"{car['yil']}-yil, "
      f"{car['narx']}$ ")

car = car2   # Ro'yxatni bita bita chiqarish
print(f"{car['model'].title()}, "
      f"{car['rang']} rang, "
      f"{car['yil']}-yil, "
      f"{car['narx']}$ ")




#Keling, barcha avtolarni bitta ro'yxatga joylaymiz, va for tsikli yordamida birma-bir konsolga chiqaramiz:
cars = [car0,car1,car2]
for car in cars:
    print(f"{car['model'].title()}, "
      f"{car['rang']} rang, "
      f"{car['yil']}-yil, "
      f"{car['narx']}$ ")
    





# ___________`for` tsikli yordamida biz bo'sh lug'atlar ro'yxatini ham yaratib olishimiz mumkin:______________

malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = { # har bir yangi mashina uchun lug'at yaratamiz
        'model':'malibu',
        'rang':None, # rangi noaniq
        'yil':2020,
        'narh':None, # narhi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz



for malibu in malibus[:3]:
    malibu['rang']='qizil'
    print(malibu)

for malibu in malibus:
    print(malibu)

for malibu in malibus[6:]:
    malibu['rang']= 'qora'
    malibu['korobka']='mexanika'

for malibu in malibus:
    print(malibu)


for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narx']=40000
    else:
        malibu['narx']=35000

for malibu in malibus:
    print(malibu)     


    #  12:33