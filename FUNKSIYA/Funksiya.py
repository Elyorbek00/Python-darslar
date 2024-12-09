def find_max(a,b):
    if a > b:
        print(f"{a} kotta {b} dan")
    else:
        print(f"{b} kotta {a} dan")



son1 = int(input("Son kriting"))
son2 = int(input("Son kriting"))

# if son1>son2:
#     print(f"{son1} katta {son2} dan")
# elif son1==son2:
#     print("Sonlar teng")
# else:
#     print(f"{son2} katta {son1} dan")


find_max(son1,son2)


# a = 30
# b = 90
# if a > b:
#     print(f"{a} kotta {b} dan")
# else:
#     print(f"{b} kotta {a} dan")


# def toq(a):
#     if 0<a:
#         print("Son musbat")
#     elif 0 > a:
#         print("Son Manfi")
#     elif 0==a:
#         print("Son teng")



# son = 0
# toq(son)



def toq(a,b,d):
    if a > b and a > d:
        print(f" {a} eng kottasi")
    elif b > a and b > d:
        print(f" {b} eng kottasi")
    elif d > a and d > b:
        print(f" {d} eng kottasi")


toq(80,40,70)


def text(a):
    print(f"Malumot uzunligi {len(a)} teng")
user = input("Malumot kriting ")
text(user)



def find_max2(son1:int,son2:int)->int:
    if son1>son2:
        return son1
    else:
        return son2
    
natija = find_max2(20,40)
print(natija)



def find_max3(son1:int,son2:int)->int:
    result = 0
    if son1>son2:
        result = son1
    else:
        result = son2
    return result

a = int(input("son1 = "))
b = int(input("son2 = "))

natija = find_max(a,b)
print(natija)








# bu funksiya ham positional ham named bo'la oladi
def yigindi(son1,son2):
    return son1+son2

a = yigindi(100,400)
print(a)


# positional argument berish
b = yigindi(1,40)
print(b)

# name argument berish
yigindi(son2 = 90,son1 = 8)

# positional parametr berish /-> named qilish bloclaydi
def ayirma(son1,son2,/):
    return son1-son2

print(ayirma(40,50))
# named argument berish -> * postional qiymat berishni bloc laydi
def kopaytma(*,a:int,b:int)->int:
    return a*b
print(kopaytma(b = 30,a = 50))

# birinchi positional keyin esa named parametrn berish kerak
# son1 va son2 positional son3,son4 esa nemad
def find_max(son1,son2,/,*,son3,son4):
    return  max(son1,son2,son3,son4)

a = find_max(200,4,son4=90,son3=100)
print(a)


raqamlar = [43,6,78,9,65]
a = sorted( raqamlar, reverse=True)
print(a)

# ikkita son uchun qo'shish ayrish ko'paytirish , bo'lish funksiyalarini yozamiz
# qo'shish da funksiya ham named ham positional bo'lsin
# ayirish faqat positional 
# ko'paytirishda faqat named
# bo'lishda birinchi parametr positional ikkinchisi named bo'lsin

def minus(a,b,/):
    return a-b

def multiplication(*,a,b):
    return a*b

def devison(a,/,*,b):
    return a/b

def calculator():
    a = int(input("a = "))
    b = int(input("b = "))
    amal = input("amalni kiriting (,+,-,*,/) amal = ")
    if amal == "+":
        natija  = plus(a,b)
        print(f"{a} + {b} = {natija}")
    elif amal == "-":  
        natija  = minus(a,b)
        print(f"{a} - {b} = {natija}")  
    elif amal == "*":  
        natija  = multiplication(a = a,b = b)
        print(f"{a} * {b} = {natija}")   
    elif amal == "/":  
        natija  = devison(a,b = b)
        print(f"{a} : {b} = {natija}") 
    else:
        print("Bunday amal mavjud emas")            
# calculatorni chaqirish
while True:
    if input("dasturni to'xtatish uchun stop ni yozing ") =="stop":
        break
    calculator()




def qushish(a:int,b:int)->int:
    return a + b

# lambda funksion -  > nomsiz funksiya
# bu funksiya nomsiz funksiya va unda bir qator code yozish mumkun
# gu funksiya qiymat qaytaradi
add = lambda a,b:a+b
print(type(add))



numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


studets = [("Ali", 90), ("Bek", 80), ("Vali", 85)]
sorted_students = sorted(studets, key=lambda x: x[1])
print(sorted_students)





#___________________________________MASALALAR___________________________________

#_______________1-masala________________________
#Ikkita sonni qo‘shish uchun lambda yozing.
qoshish = lambda x,y:x+y
print(qoshish(30,40))


#___________2-masala_________________
# 2. Ro‘yxatdan juft sonlarni ajratib olish uchun lambda ishlating.
listlar = [5,7,6,9,1,5,6,4,2,1]
juft = list(filter(lambda x: x % 2 == 0, listlar))
print(juft)


#________3-masala________________
# 3. Lug‘atlar ro‘yxatini ma’lum bir kalit bo‘yicha lambda yordamida saralang.


#________4-masala________________
# 4. Sonning kvadratini hisoblash uchun lambda funksiyasini tuzing.
kv = lambda x: x**2
print(kv(30))


#________5-masala________________
# 5. Ro‘yxatdan "A" harfi bilan boshlanadigan ismlarni ajratib oling.
mevalar = ['olma','yongoq', 'anor', 'anjir']
alar = list(filter(lambda x: x[0]=="a", mevalar))
print(alar)

#________6-masala________________
# 6. Narxga 10% soliq hisoblash uchun lambda yozing.
narx = lambda x:x*1.1
print(narx(50))


#________7-masala________________
# Ismlar ro‘yxatini bosh harflar bilan yozish uchun map() va lambda funksiyasini birga qo‘llang.
ismlar = ['akbar', 'vohid', 'hamid', 'muhlis']
ism = list(map(lambda x: str(x).title(), ismlar))
print(ism)



#________12-masala________________

selsiy = [2,3,410,45,100]
faranget = list(map(lambda x: x*1.8+32, selsiy))
print(faranget)


#________9-masala________________

yan_list = list(filter(lambda x: x % 2 == 1, selsiy))
print(yan_list)



#________13-masala________________

talabalar_ismi = ["Jamshit", "Otabek", "Elbek", "Zokir"]
print(max(talabalar_ismi, key=lambda x:len(x)))


#________14-masala________________

talabalar = list(filter(lambda x: len(x)<6,talabalar_ismi))
print(talabalar)

# filter   --  list, set, tupl ning ichidan biron qoida shatrt uchun kerak bo'ladi
# map -- biron qoida assosida yangi list yaratish