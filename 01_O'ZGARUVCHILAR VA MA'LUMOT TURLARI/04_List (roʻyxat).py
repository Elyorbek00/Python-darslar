#___________RO'YXATLAR - LIST_____________________

# LIST- quyidagicha yaraladi
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]    # mevalar ro'yxati (matnlar)
narxlar = [12000, 18000, 20900, 22000, -25, 63.2]   # narxlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5]                   # sonlar va matinlar aralash ro'yhati
ismlar = []                                         # bo'sh ro'yxat




#_____________RO'YXAT ELEMENTLARI__________________

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]    # mevalar ro'yxati (matnlar)
print("Brinchi meva: ", mevalar [0])                # index [] buyicha chaqirish
print("Ikkinchi meva: ", mevalar [1])

# string metodlar qulash
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]    # mevalar ro'yxati (matnlar)
print("Brinchi meva: ", mevalar [0].title())        
print("Ikkinchi meva: ", mevalar [1].upper())

# List elementlari ustidan arifmetik amallar bajarish
narxlar = [12000, 18000, 20900, 22000, -25, 63.2]   # narxlar ro'yxati (sonlar)
print(narxlar[2] + narxlar[3])





#____________LIST ELEMENTINI O'ZGARTIRISH___________ 

# element qiymatini uzgartrish
narxlar = [12000, 68000, 10900, 22000, -25, 63.2]   # narxlar ro'yxati (sonlar)
narxlar[0] = 13000
narxlar[1] = 660000
print(narxlar) 




#____________LIST ELEMENT QO'SHISH_________________

# .append() list ohiriga element qushish
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]    # mevalar ro'yxati (matnlar)
mevalar.append('tarvuz')
print(mevalar)


# Bush listga element qo'shish
cars = []
cars.append("baw")
cars.append('cheri')
cars.append("jentra")
print(cars)


# .insert() ro'yxatni hoxlagan indexiga element qo'shish
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]    # mevalar ro'yxati (matnlar)
mevalar.insert(1, "bexi")
print(mevalar)


#_____________Elementni o'chirish__________________

# del elementni indexi yordamida olib tashlash uchun del operatoridan foydalanamiz
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]    # mevalar ro'yxati (matnlar)
del mevalar[1]
print(mevalar)


# .remove() elementni qiymati bo'icha uchirish
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
print(mevalar)


# .pop(indeks)    Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi mumkin. Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)







#_________________AMALIYOT______________________

#_______1.amaliyot________
#  ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
ismlar = ['sher', 'ali', 'muxammat', 'doston']
print(ismlar[0], 'qalaysan do\'st')
print(f"dostim {ismlar[1]} yahshi yuribsanmi")


#_______2.amaliyot________
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
print(sonlar)
sonlar[0] = sonlar[0]+ sonlar[1]
sonlar[1] = -67.5
sonlar[4] = sonlar[4]+41
del sonlar[5]
print(sonlar)


#_______3.amaliyot________
# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan\n\
suhbat qilishni istar edim\n")



#_______4.amaliyot________

#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append('John')
friends.append('Alex')
friends.append('Danny')
friends.append('Sobirjon')
friends.append('Vanya')
print(friends)


#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friends.remove('John')
friends.remove('Alex')
print(friends)


#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append('Hasan')
friends.insert(0, 'Husan')
friends.insert(2, 'Ivan')
print(friends)


#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)