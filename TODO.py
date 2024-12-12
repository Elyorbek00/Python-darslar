print("Assalomu alaykum TODO dasturiga xush kelibsiz")

tasklar ={}
history = []



def add_task():
    tasklar[len(tasklar)+1] = [True, input("Taskni kriting = ")]
    print("Task muvofqiyatli qushildi")




def show_tasks():
    for key,value in tasklar.items():
        if value[0]:
            print(f"taskID = {key}, Task = {value[1]} ")




def todo_task():
    show_tasks()
    id = input("Bajarmoqchi bo'lgan task id sini kiriting = ")
    if id.isdigit():
        id = int(id)
        value = tasklar.get(id)
        value[0]= False
        history.append(value[1])




def show_history():
    print("Jami bajarilgan tasiklar quyidagilar ")
    for i in history:
        print(i)



while True:
    print("""
    1 - Task qo'shish
    2 - Barcha taskni ko'rish
    3 - History
    4 - Tasklarni bajarish
    5 - Til
    6 - Dasturni to'xtatish

    """)

    print("--------------------------------")
    result = input("Quyidagilarni brini tanlang ")

    if result =="1":
        add_task()
    elif result =="2":
        show_tasks()
    elif result =="3":
        show_history()
    elif result =="4":
        todo_task()
    elif result =="5":
        pass
    elif result =="6":
        pass
    else:
        print("Bunday funksiya mavjud emas")