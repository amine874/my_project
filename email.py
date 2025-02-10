import time
def validate_email(email):
    if "@" in email and "." in email :
        return True
    else :
        return False
def add_user (name,email):
    passed=validate_email(email)
    if passed :
        print(f"user {name} with email {email} was successfuly added")
    else:
        print(f"invalid email format for user {name}")

user_name=input("enter your user name ")
user_emal=input("enter ur emain adress ")
print("checking user name.......please wait")
time.sleep(3)
print("validating email adress......please wait")
time.sleep(4)
add_user(user_name,user_emal)