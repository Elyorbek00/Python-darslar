# "For" so'zi ingliz tilidan "uchun" deb tarjima qilinadi.


#Bizda mehmonlar ro'yxati bor, biz har bir mehmonning ismini yangi qatordan chiqarmoqchimiz. Buning uchun quyidagi kodni yozamiz:
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for a in mehmonlar:
    print("Salom", a) 
    print("Hayir", a)



mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli, {mehmon}, sizni 20 Dekabir kuni nohorgi oshga taklif qilamiz" )
    print("Hurmat bilan Polonchivlar oilasi")
#Yuqoridagi kodda 2-qator bu tsikl boshi deyiladi. Aynan shu qator kodimiz nech marta takrorlanishini aniqlaydi. Bizning holatimizda tsikl mehmonlar ro'yxati ichidagi elementlar tugagunga qadar takrorlanadi. Tsikl boshlanishi ikki nuqta (:) bilan tugaydi. Undan keyingi 3 va 4-qatorlar bu tsiklning badani deyiladi.




#_______for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH_________________
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng.")



#___for yordamida yangi ro'yxat ham shakllantirish mumkin:_____
sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
for son in sonlar:  # sonlar dagi har bir son uchun
    sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz
print(sonlar)
print(sonlar_kvadrati)


#____________for va input()____________________
dostlar = []
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizni ismini kriting"))
print(dostlar)






#______________AMALIYOT_____________________________

# ______________1-AMALIYOT____________________   
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing,
#  va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ["ali", "elyor", "Muhammat", "odil", "ozod"]
for ism in ismlar:
    print(f"Assalom alaykum {ism.capitalize()}. Dasturga xush kelibsiz.")


# ______________2-AMALIYOT____________________   
#Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)

print(f"Kod {len(ismlar)} marta takrorlandi")



# ______________3-AMALIYOT____________________  
# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)
print(sonlar)



# ______________4-AMALIYOT____________________
#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.

kinolar = []
print("Yoqtirgan 5 ta kino nomini kriting")
for kino in range(5):
    kinolar.append(input(f"{kino+1}- Kino nomini kriting"))
print(kinolar)



# ______________5-AMALIYOT____________________
# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
people = int(input("Bo'gun nechta odam bilan gaplashdiz.. "))
ismlar = []
for n in range(people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamlar kim edi"))
print(ismlar)