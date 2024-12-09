#________________if-elif-else KETMA-KETLIGI_______________________

son = 50 
if son<0:
    print("Manfi son")
else:
    print("Musbat son")

# Keling bir misol ko'ramiz. Hayvonot bo'giga kirish quyidagicha belgilangan:

# 4 yoshdan kichik bolalarga kirish bepul
# 4 yoshdan 12 yoshgacha kirish 5000 so'm
# 12 yoshdan kattalarga 10000 so'm

# Foydalanuvchidan yoshini so'rab, hayvonot bog'iga kirish chiptasi narhini chiqaruvchi dastur yozamiz.

yosh = int(input("Yoshingiz nechida? "))
if yosh<=4: # yosh bolalarga bepul
    narx = 0    
elif yosh<=12:      # 4 dan 12 yoshgacha 5000 so'm
    narx = 5000
elif yosh <= 18: # 12 dan katta va 18 dan kichiklarga narh 8000 so'm
    narx = 8000
else:               # qolgan barcha yoshga 10000 so'm
    narx = 1000
print(f"Sizga krish {narx} so'm")





#____________OR OPERATORI_____________________

# OR - yokiy degani

kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')



#___________AND OPERATORI________________________

# AND "va" deb tarchima qilinadi 

kun = input("Bugun nima kun? ")
harorat = float(input("Havo harorati qanday? "))

if kun.lower()== "yakshanba" and harorat >= 30:
    print("Chomilishga kedik!")
elif kun.lower()=="yakshanba" and harorat < 30:
    print("Uyda dam olamiz")
else:
    print("Bugun ish kuni") 



#__________BIR NECHTA SHARTLARNI KETMA-KET YOZISH___________________

kun = input("Bugun nima kun? ")
harorat = float(input("Havo harorati qanday? "))

if kun.lower()=="yakshanba" or kun.lower()=="shanba" and harorat>=30:
    print("Chomilgani ketdik!")
elif kun.lower()=="yakshanba" or kun.lower()=="shanba" and harorat<30:
    print("Uyda dam olamiz ")




#_______________BOOLEAN MA'LUMOTLAR TURI_________________________

narh = 15000 # mijoz 15000 so'mga taom oldi.
choy = True # mijoz choy ham oldi
salat = False # mijoz salat olmadi

if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
elif choy or salat: # agar choy yoki salat olgan bo'lsa
    narh = narh + 5000 # narhga 5000 so'm qo'shamiz

print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz




#_________________SHARTLARNI KETMA-KET TEKSHIRISH_________________

narh = 15000 # mijoz 15 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti = False

#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:   # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000

if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000

if non:    # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000

if kompot: # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000

if assorti: # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000
    
print(f"Jami {narh} so'm")




#_________________in OPERATORI___________RO'YXAT TARKIBINI TEKSHIRISH______________________

menu = ['osh','qazonkabob','shashlik','norin','somsa']  # ovqat ruyxati
ovqat = input('Nima ovqat yeysiz?>>>')      # Foydalanuvchidan nima ovqat yiyishini surash

if ovqat.lower() in menu:   # ruyxat ichinini tekshirish
    print("Buyurtma qabul qilindi")  
else:           # ruyxat ichida ovqat bulmasa 
    print("Afsuski bizda bunday ovqat yo'q")



#_____________________not in OPERATORI__________________________________

menu = ['osh','qazonkabob','shashlik','norin','somsa']  # ovqat ruyxati
ovqat = input('Nima ovqat yeysiz?>>>')      # Foydalanuvchidan nima ovqat yiyishini surash

if ovqat.lower() not in menu:   # ruyxat ichinini tekshirish
    print("Afsuski bizda bunday ovqat yo'q")  
else:           # ruyxat ichida ovqat bulmasa 
    print("Buyurtma qabul qilindi") 


#____________________IKKI RO'YXATNI SOLISHTIRISH__________________________
#Ikki ro'yxatning tarkibi quyidagicha tekshiriladi:

menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")



#____________________RO'YXAT BO'SH EMASLIGINI TEKSHIRISH_____________________

menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")