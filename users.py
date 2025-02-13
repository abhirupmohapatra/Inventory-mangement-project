import items
def validate(password):
    d=0
    u=0
    l=0
    s=0
    if len(password)>=6:
        for i in password:
            if i.isdigit():
                d+=1
            elif i.islower():
                l+=1
            elif i.isupper():
                u+=1
            elif i=='@'or i=='#'or i=='$'or i=='&':
                s+=1
        if d>=1 and l>=1 and u>=1 and s>=1:
            return 'valid'
        else:
            if d==0:
                print("Password should have a Digit")
            if l==0:
                print("Password should have a lower case")
            if u==0:
                print("Password should have a upper case")
            if s==0:
                print("Password should have a special character")
            return 'invalid'
    else:
        print("Length must be equal or more than six")
        return 'invalid'
                
def Login():
    print("-------Customer Page-------")
    print("1:New User \n 2:Existing User")
    ch=input("Enter 1 OR 2:")
    if ch=='1':
        name=input("Enter Your Name:")
        p=input("Enter Password:")
        c=validate(p)
        while c!='valid':
            p=input("Enter Password:")
            c=validate(p)
        detail=name+","+p+"\n"
        print("Account Created Successfully")
        fp=open("customer.txt",'a')
        fp.write(detail)
        fp.close()
        items.F1()
    elif ch=='2':
        name=input("Enter name:")
        p=input("password:")
        fp=open("customer.txt",'r')
        c1=0
        L=fp.readlines()
        fp.close()
        for i in L:
            i=i.rstrip().split(",")
            if name in i[0] and p in i[1]:
                print("Login successful")
                items.F1()
                break
            elif name in i[0] and p not in i[1]:
                print("Invalid Password!")
            elif name not in i[0] and p in i[1]:
                print("Invalid User name!")
        else:
            print("User Doesn't Exist")
