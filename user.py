class User:
    def __init__(self,first_name,last_name,email,password,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status
def create_user():
    first_name=input("enter your first_name: ")
    last_name=input("enter the last_name: ")
    email=input("rnter the email: ")
    password=input("enter the password: ")
    return User(first_name,last_name,email,password)
user1=create_user()