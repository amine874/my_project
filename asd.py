#class Task:
   # def __init__(self,title,description,due_date,status):
       # self.title=title
       # self.description=description
       # self.due_date=due_date
       # self.status=status
    #def display_task(self):
       # print(f"title {self.title}")
       # print(f"description {self.description}")
       # print(f" due date {self.due_date}")
       # print(f" status {self.status}")
    #def mark_as_complete(self):
        #self.status = "complete"

#task1=Task("hören","hören des textes","2025-02-20","icompéate")
#task1.display_task()
#task1.mark_as_complete()
#task1.display_task()


#class User:
    #def __init__(self,first_name,last_name,email,password,status="inactive"):
     #   self.first_name=first_name
      #  self.last_name=last_name
       # self.email=email
        #self.password=password
        #self.status=status

#def create_user():
    #first_name=input("enter the first_name")
   # last_name=input("enter the last_name")
    #email=input("enter the email")
    #password=input("enter the password")
    #return User(first_name,last_name,email,password)

#user1=create_user()

class User:
    def __init__(self, first_name, last_name, email, password, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def display_user(self):
        return f"الاسم: {self.first_name} {self.last_name}, البريد الإلكتروني: {self.email}, الحالة: {self.status}"


# قائمة لتخزين المستخدمين
users_list = []

while True:
    print("""
    1. إضافة مستخدم جديد
    2. عرض جميع المستخدمين
    3. خروج
    """)
    
    choice = input("أدخل خيارك: ")

    if choice == "1":
        # إنشاء مستخدم جديد
        first_name = input("أدخل الاسم الأول: ")
        last_name = input("أدخل الاسم الأخير: ")
        email = input("أدخل البريد الإلكتروني: ")
        password = input("أدخل كلمة المرور: ")

        new_user = User(first_name, last_name, email, password)
        users_list.append(new_user)
        print("\n✅ تم إضافة المستخدم بنجاح!\n")

    elif choice == "2":
        if users_list:
            print("\n📜 قائمة المستخدمين:\n")
            for user in users_list:
                print(user.display_user())
        else:
            print("\n⚠️ لا يوجد مستخدمون بعد.\n")

    elif choice == "3":
        print("\n👋 تم الخروج من البرنامج.\n")
        break

    else:
        print("\n❌ خيار غير صحيح، يرجى المحاولة مرة أخرى.\n")


