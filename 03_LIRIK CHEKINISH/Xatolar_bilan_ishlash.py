#______________ SyntaxError - SINTEKS XATOLIK____________________
# print"Hello World!"               # Qavuslari qolib ketgan



#________EOL va EOF xatolik___________________
# print("Hello World!"              #Ohirgi qavus yo'q




# ______________IndentationError - JOY TASHLASHDA XATOLIK________________
#   print("Hello World!")           # boshida yoy tashlanib ketgan 


# print("O'ngacha sanaymiz")
# for n in range(10):
# print(n+1)                      # qatorda hato bor 


# print("O'ngacha sanaymiz")
# for n in range(10):
#   print(n)
#       print(n+1)                # ustunlar hato bor 



#_____________RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK____________________

# TypeError:
# son = input("Istalgan son kiritig: ")
# print(f"{son} ning kvadrati {son**2} ga teng")   # matindan int ga utqazib olish kerak chunki bu yerda steing berayabdi str{son**2} kupaytrib bulmaydi


# NameError:
# prit("Hello World")  # print xato yozilgan 

# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mvealar:                #  uzgaruvchi nomida hatolik bor 
#     print(meva)


# ValueError:
# son = int(input("Istalgan son kriting: "))    #  agar 20.5 kritsak hato beradi
# if son >=0:
#     print("Musbat son")
# else:
#     print("Manfiy son") 


# IndexError:
# mevalar = ["olma", "anor", "uzum"]
# print(mevalar[3])    # dasto'rlashda indeks 0 dan boshlanadi  bu yerda 3 index yo'q


# ZeroDivisionError:
# x, y = 50, 50    # bizda x va y birxil bo'lib olgan 0 ga bo'lib bo'lmaydi 
# z = 250/(x-y)
# print(z)


#___________MANTIQIY XATOLAR________________________
# radius = 5
# pi = 4.14        # bu joyda aslida   (3.14)  bo'lishi kerak
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi)


# son = float(input("Istalgan son kiriting: "))
# ildiz = son**1/2   # bu joyda xato masalani ohiridan boshlan hisoblayabdi biz  <<<son**(1/2)>>> deb yozishimiz kerak yoki <<<son**0.5>>>  deb yozishimiz kerak
# print(f"{son} ning ildizi {ildiz} ga teng")


# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi")   #   bu hyerda prin for ichiga krib qolgan va har bir mevaga datur tugadi deb chiqarayabdi 




#_________________AMALIYOT________________________________

"""
son = float(input("Juft son kiriting: ")   # OHIRIDA QAVUS QOLIB KETGAN
if son%2==0:
    print("Bu son juft emas.')   # OHIRGI QUSHTRNOQ XATO
else:
    print("Rahmat!"))      # QAVUS 2 TA BULIB QOLGAN
"""




"""
yosh = (input("Yoshingiz nechida?"))             # xati int() quyilmagan

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
    print(f"Chipta {narh} so'm")
"""


"""
x = float(input("Birinchi sonni kiriting: ")
y = float(input("Ikkinchi sonni kiriting: ")    # ohirida qavus qolib ketgan 
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f'{x}<{y}")  # qush trnoq xato berilgan
else
    print(f"{x}>{y}")
    """




"""
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
            'kartoshka', 'olma', 'banan', 'uzum', 'qovun']    #  ohirgi qavus qolib ketgan va qator nato'g'ri

for n in range(5):
    n.append() int(input(f"Savatga {n+1}-mahsulotni qo'shing: "))   # for dan kelayotgan uzgaruvchi hato

if n:
    for mahsulot in n:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")            
    """


mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

"""
savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo'shing: '))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahslot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
  print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    """

"""
users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang:' )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")
"""