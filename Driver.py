import users
import owner
print("----Welcome To The App----")
print("1:Customer\n2:Owner")
ch=input("Enter Your Choice 1/2:")
if ch=='1':
    users.Login()
elif ch=='2':
    p=input("Enter Your password:")
    if p=="Owner@123":
        owner.work()
    else:
        print("invalid Password")
else:
    print("Invalid Input!!")

