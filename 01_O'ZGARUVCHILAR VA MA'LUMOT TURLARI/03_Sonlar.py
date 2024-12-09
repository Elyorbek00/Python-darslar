#________________01 INTEGERS — BUTUN SONLAR______________________

#Butun sonlarni ham o'zgaruvchida saqlash, ularning ustida qo'shish (+), ayirish (-), ko'paytirish(*), bo'lish (/) kabi arifmetik amalarni bajarish mumkin:
a = 20  # Sonlar musbat yoko
b = -30 # manfiy bo'lishi mumkin
c = a + b
print(c)


# Kvadratning yuzini hisoblaymiz
kvdrt_tmni = 20 # Kavdratning tomoni 20 ga teng
kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
print(kvdrt_yuzi)






#________________02 FLOATS — O'NLIK SONLAR__________________________

#Pythonda o'nlik sonlar floating point numbers yoki qisqa qilib floats deyiladi. "Floating point numbers" atamasini o'zbek tiliga "suzuvchi nuqtali sonlar" deb tarjima qilish mumkin. Ingliz tilida o'nlik sonlarni yozishda vergul (,) emas nuqta (.) belgisi ishlatiladi, va bu nuqta sonning katta kichikligiga qarab joyi o'zgargani uchun "floating" (suzuvchi) deyiladi.

PI = 3.14159 # o'nlik son (float)
radius = 10  # butun son (integer)
diametr = 2*radius
print("Aylana uzunligi ", PI*diametr, " ga teng.")






#______________________03 BUTUN SONDAN O'NLIK SONGA_______________________________

# # #Avval aytganimizdek ikki butun sonni bo'lish (/) natijasida o'nlik son hosil bo'ladi (natija butun bo'lsa ham).

a = -20
b = 40
c = b/a
print(c)  # natija o'nlik son bo'ladi

a = 2
b = 3.0
# Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
print(a+b)
print(a*b)
print(a**b)
print(2*(a+b))





#_________________UZUN SONLARNI KIRITISH_________________________

# #Uzun sonlarni kiritishda, qulaylik uchun, raqamlarni pastki chiziq (_) yordamida guruhlash mumkin. Python - son tarkibidagi pastki chiziqlarni (_) inobatga olmasdan, uzun sonligicha qabul qiladi.

aholi_soni = 7_594_675_800
print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")






#______________ KONSTANTA_________________________

# # Aksar dasturlash tillarida konstant qiymatlar tushunchasi bor. Konstantlar o'zgarmas bo'ladi (misol uchun ning qiymati konstant, o'zgarmas qiymat). Pythonda konstant tushunchasi yo'q, shuning uchun dasturchilar bunday o'zgaruvchilarning nomini katta harflar bilan yozadilar (ogohlantirish sifatida). Bu albatta qat'iy qonun emas, lekin kelajakda o'zgaruvchilar orasida konstant qiymatlarni ajratish uchun yaxshi usul.

PI = 3.14159
raduis = 21.2

radius = 20
PI = 3.14159
diametr = 2*radius                        # Agar uzgaruvchi kota harifda yozilsa uni uzgartirish kerak emas
print("Aylana uzunligi=", PI*diametr)






#_______________BIR NECHTA UZGARUVCHILARGA QIYMAT BERISH_______________________

x, y, z = 10, 5.5, -36   # Uzgaruvchilarni bir qatorda yozsa ham bo'ladi
print(type(x))
print(type(y))
print(type(z))


a = 20
b = 5.5
print(type (a*b))     # agar uzgaruvchilarni orasida unlik son bo'lsa  javobi ham unlik son bo'ladi






#_______________O'ZGARUVCHI TURINI ALMASHTRISH_____________________
ism ="Elyor"
yosh = 25
xabar = ism + ' ' + str(yosh) + ' yoshda'      # son bilan suzlarni qushish uchun (str) dan foydalanish kerak
print(xabar)


t_yil = int(input("Tug'ilgan yilingzni kriting: "))      # yoshni hisoblashda son bilan hisoblasak inputni oldiga int funksiyasini kritishimiz kerak
yosh = 2024 - t_yil
print("Siz ", yosh, " yoshda ekansiz")






#__________________O'ZGARUVCHI TURINI TEKSHIRISH_______________________

# # Kodimizda o'zgaruvchilar ko'payib ketdi. Yuqoridagi kabi xatolar qilmaslik uchun ba'zida o'zgaruvchinig turini tekshrish talab qilinadi. Buning uchun type() funktsiyasidan foydalanamiz:

ism = 'Jobir'
yosh = 36
print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
print(type(yosh)) # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz

# #Kurib turganingizdek, ism nomli o'zgaruvchi 'str' ya'ni matn, yosh esa 'int' son turida ekan.






#____________________INPUT() VA SONLAR______________________________

# # Avvalgi darsimizda foydalanuvchidan ma'lumot olish uchun input() funktsyasidan foydalanishni o'rgandik. Kelin endi shu funktsiya yordamida foydalanuvchidan son olishni ko'raylik. Quyidagi kod foydalanuvchining tug'ilgan yilini so'raydi va uning yoshini hisoblab beradi:

t_yil = input("Tug'ilgan yilingizni kiriting: ")
yosh = 2024 - t_yil #
print("Siz " + yosh + " yoshda ekansiz")


# # Kutilgan natija o'rniga xatolik. Lekin xato qayerda? Dastur tug'ilgan yilimni so'radi, men 1983 deb kiritdim va shu zaxoti xato ro'y berdi va dastur to'xtadi. Xatoni tarjima qilsak son (int) va matn (str) o'rtasida ayirish (-) amalini bajarib bo'maydi deyapti.

# # Gap shundaki, input() funktsiyasi har qanday kiritilgan qiymatni matn (string) ko'rinishida qabul qiladi (garchi biz son kiritgan bo'lsak ham). Keling, konsolda t_yil degan o'zgaruvchining turini tekshirib ko'ramiz.

t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh = 2024 - t_yil #
print("Siz " + str(yosh) + " yoshda ekansiz")


# # Yuqoridagi kodning 2-qatoriga e'tibor bersangiz, biz ikki funktsiyani bir biriga joylab yozdik (int(input()). Aslida, ajratib ham yozishimiz mumkin edi:

t_yil = input("Nechi yoshga krdingiz: ")
t_yil = int(t_yil)
yosh = 2024 - t_yil #
print("Siz " + str(yosh) + " yoshda ekansiz")

# # Tug'ilgan yilingizni kiriting: 1983
# # Siz 37 yoshda ekansiz
