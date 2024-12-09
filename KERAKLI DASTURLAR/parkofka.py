parking = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

son = 1

while son != 0:
    print("\n1. Avtomobilni parkovkaga joylashtirish.")
    print("2. Avtomobilni o'chirib yuborish.")
    print("3. Bo'sh joylarni ko'rish.")
    print("0. Seansni tugatish.")
    son = int(input("\nMenyudan birini tanlang: "))
    
    if son == 1:
        row = int(input("Qatorni kiriting (1-10): "))
        col = int(input("Ustunni kiriting (1-10): "))
        if 1 <= row <= 10 and 1 <= col <= 10:
            if parking[row-1][col-1] == 0:
                nom = input("Avtomobil nomini kiriting: ")
                parking[row-1][col-1] = nom
                print("Avtomobil muvaffaqiyatli joylashtirildi.")
            else:
                print("Bu joy band. Eng yaqin bo'sh joylarni tavsiya qilamiz:")
                chap = col - 2 if col > 1 and parking[row-1][col-2] == 0 else None
                ong = col if col < 10 and parking[row-1][col] == 0 else None
                
                if chap:
                    print(f"Qator {row}, Ustun {chap + 1} (chap tomon).")
                if ong:
                    print(f"Qator {row}, Ustun {ong + 1} (o'ng tomon).")
                if not chap and not ong:
                    print("Yaqin atrofda bo'sh joy topilmadi.")
        else:
            print("Iltimos, to'g'ri qator va ustun raqamlarini kiriting (1-10).")
    
    elif son == 2:
        row = int(input("Qatorni kiriting (1-10): "))
        col = int(input("Ustunni kiriting (1-10): "))
        if 1 <= row <= 10 and 1 <= col <= 10:
            if parking[row-1][col-1] != 0:
                parking[row-1][col-1] = 0
                print("Avtomobil muvaffaqiyatli o'chirildi.")
            else:
                print("Bu joy allaqachon bo'sh.")
        else:
            print("Iltimos, to'g'ri qator va ustun raqamlarini kiriting (1-10).")
    
    elif son == 3:
        print("\nParkovka holati:")
        for i in range(10):
            for j in range(10):
                print(parking[i][j], end=' ')
            print()
    
    elif son == 0:
        print("Seans yakunlandi.")
    else:
        print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")
