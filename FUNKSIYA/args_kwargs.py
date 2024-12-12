# def aylana(r:int):
#     p = 3.14
#     return 2*p*r


# def yuza(r):
#     p = 3.14
#     return p*r**2

def faktarial(n):
    if n >1:
        return n+faktarial(n-1)
    else:
        return 1

a = faktarial(10)
print(a)







# 4 ta sion yig'indisini chiqaradigan funksiya yarating
def yigindi4(g,w,o,h):
    return g+w+o+h

print(yigindi4(50,60,80,70))


def summa(*args):
    s = 0
    for a in args:
        s = s + a
    return s

print(summa(20,50,40,80,60))












# agar funksiyaga nechta named qilingan argumet berish namolum bo'lsa kwargs ishlatiladi va kelgan malumot turi dictionary bo'ladi
def talaba_info(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

talaba_info(talaba_ism = "Elyor", talaba_yosh = "20", talaba_jinsi = "Erkak")















# shunday funksiya yarating unga talaba barcha fanlardan bahosini kritsin umumiy o'rtacha bahosini va yaxshi o'zlashtirgan fanini ekranga chop etsin 

def talaba(**kwargs):
    a =0
    for k,v in kwargs.items():
        a=a+int(v)
    print(f"{a/len(kwargs)}")
    

print(talaba(programming = "1", english = "2", web = "3", its = "4"))



