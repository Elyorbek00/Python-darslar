"""
# EKUK ni hisoblash uchun funksiya
def find_ekuk(a, b):
    # EKUB ni topish uchun ichki yordamchi funksiya
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    # EKUK ni hisoblash
    ekuk = abs(a * b) // gcd(a, b)
    return ekuk

# Funksiyani chaqirish
son1 = 12
son2 = 18
natija = find_ekuk(son1, son2)

print(f"{son1} va {son2} sonlarining EKUKi: {natija}")
"""


"""

def find_ekuk(a,b):
    def el(x,y):
        while y !=0:
            x,y = y,x % y
        return x
    
    ekuk = abs(a*b) //el(a,b)
    return ekuk

son1 = 12
son2 = 18
natija = find_ekuk(son1, son2)

print(f"{son1} va {son2} sonlarning EKUK: {natija}")

"""





#______________________1 - masala________________________
#1. Berilgan 5 ta sonning eng kichigini topuvchi funksiya tuzing 



#______________________2 - masala________________________
#2. Berilgan haqiqiy sonni natural son ekanligini tekshiruvchi funksiya tuzing.

def son (a):
    if a % 1 ==0 and a >= 0:
        print("Natural son")
    else:
        print("Natural son emas")

print(son(int(input("Son kriting"))))





#______________________3 - masala________________________
#3.Berilgan satrda nechta katta harf, nechta kichik harf borligini aniqlovchi funksiya tuzing.
def harf_sanash(satr:str):
    global kata, kichik
    kata = 0
    kichik = 0
    for harf in satr:
        if harf.isupper():
            kata+=1
        if harf.islower():
            kichik+=1
    return kata, kichik
satr = "Assalomu alaykum"
harf_sanash(satr)
print(f"kata harif {kata}")
print(f"kichik harif {kichik}")



#______________________4 - masala________________________
#.Berilgan satrdagi harf va raqam bo’lmagan belgilarni Qaytaradigan funksiya tuzing.
def belgi (a:str):
    sanoq = 0
    for i in a:
        if not i.isalnum():
            sanoq=sanoq+1
    
    print(f"{sanoq} ta belgi bor")

matn = input("Matin kriting......")
belgi(matn)



#______________________5 - masala________________________
# 5 - Foydalanuvchi tomonidan kiritilgan satr ko’rinishidaparolni yaroqli yoki yaroqli emasligini tekshiring.
# Parol yaroqli hisoblanadi, agarda:
# 1) Uzunligi 8 ta belgidan kam bo’lmasa;
# 2) Kamida bitta katta harf ishtirok etsa;
# 3) Kamida bitta kichik harf ishtirok etsa;
# 4) Kamida bitta raqam ishtirok etsa;

def parol(por:str):
    kata_harf = 0
    kichik_harif =0
    raqam = 0
    for a in por:
        if a.isupper():
            kata_harf = kata_harf +1
        if a.islower:
            kichik_harif = kichik_harif + 1
        if a.isdigit():
            raqam = raqam + 1
    if len(por) >= 8 and kata_harf >= 1 and kichik_harif >= 1 and raqam >= 1:
        print("parol to'g'ri")
    else:
        print("parol hato")
print(parol("salom"))



