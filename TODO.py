

uzbek ={
    "say_hello":"Assalomu alaykum TODO dasturiga xush kelibsiz", 
    "add":"Task qo'shish"}

rus = {
    "say_hello":"Привет и добро пожаловать в TODO", 
    "add":"Добавить задачу"}

inglish = {
    "say_hello":"Hello and welcome to the TODO program.", 
    "add":"Add task"}

til = uzbek


tasklar = {}
history = []

def change_language():
    global til
    language = input("""
1 - O'zbek
2 - Russion
3 - English
""")
    if language == "1":
        til = uzbek
        print("Til Uzbektiliga o'gartirildi")
    elif language == "2":
        til = rus
        print("Til Rustiliga o'gartirildi")
    elif language == "3":
        til = inglish
        print("Til Inglistiliga o'gartirildi")
    else:
        print("Bunday til mavjud emas. Til o'zgarmadi")



def add_task():
    while True:
        result = input("""
1- Task qo'shish
2- Chiqish               
""")    
        if result == "1":
            tasklar[len(tasklar)+1] = [True,input(" Taskni kiriting = ")]
            print("Task muvofqiyatli qo'shildi")
        elif result == "2":
            break
        else:
            print("Bunda funksiya mavjud emas.Quyidagidan birini tanlang")
        

def show_tasks():
    for key,value in tasklar.items():
        if value[0]:
            print(f"taskID = {key},Task = {value[1]} ")


def todo_task():
    while True:
        result = input("""
1- Task bajarish
2- Chiqish               
""")      
        if result == "1":
            show_tasks()
            id = input("Bajarmoqchi bo'lgan task id sini kiriting = ")
            if id.isdigit():
                id = int(id)
                value = tasklar.get(id)
                value[0]= False
                history.append(value[1])
                print(f"Siz {value[1]} taskni muvofaqiyatli bajardingiz")
        elif result == "2":
            break
        else:
            print("Bunda funksiya mavjud emas.Quyidagidan birini tanlang")



def edit_task():
    while True:
        show_tasks()
        result = input("Edit qilmoqchi bo'lgan task ID sini kriting ID = ")
        if result.isdigit():
            result = int(result)
            task = tasklar.get(result, False)
            if task == False:
                print("Siz mavjud bo'lmagan  ID kritingiz")
            else:
                edit = input(f"Siz tahrirlamoqchi bo'lgan task {task[1]} o'zgartring: ")
                task[1] = edit 
                print("Muvafaqiyatli tahrirlandi")
        else:
            print("Siz nato'g'ri malumot kritingiz")





def show_history():
    print("Jami bajarilgan tasklar quyidagilar ")
    for i in history:
        print(i)



print(til.get("say_hello"))

while True:
    print(f"""
    1 - {til.get("add")}
    2 - Barcha taskni ko'rish
    3 - History
    4 - Tasklarni bajarish
    5 - Til
    6 - Taskni tahrirlash      
    7 - Dasturni to'xtatish

    """)
    result = input("Quyidagilarni birini tanlang = ")

    if result == "1":
        add_task()
    elif result == "2":
        show_tasks()
    elif result == "3":
        show_history()
    elif result == "4":
        todo_task()
    elif result == "5":
        change_language()
    elif result =="6":
        edit_task()
    elif result == "7":
        break
    else:
        print("Bunday funksiya mavjud emas")