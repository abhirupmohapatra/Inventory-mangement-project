import random
def F1():
    ordn=random.randint(100,200)+random.randint(300,500)
    print("=="*25)
    print("\t-----Item List------")
    print("=="*25)
    print()
    fp=open('items.txt','r')
    print(fp.read())
    fp.close()
    fp=open('items.txt','r')
    L=fp.readlines()
    fp.close()
    d={}
    total=0
    while True:
        n=input("Choose Your Dish Number:")
        q=int(input("Enter Quantity:"))
        f=0
        for i in L:
            i=i.rstrip().split(',')
            if n==i[0]:
                f=1
                if i[1] not in d.keys():
                    d[i[1]]=q
                else:
                    d[i[1]]+=q
                total+=d[i[1]]*int(i[2])
        if f==0:
            print("invalid Dish Number:")
        ch=input("Hit 'y' to choose another Dish:")
        if ch=='y':
            continue
        else:
            break
    detail=','
    print("\n*****Your Order*****\n")
    print(f"Order Number:{ordn}\n")
    [print(key,":",value)for key,value in d.items()]
    print(f"\n-------Total Amount:Rs {total}------\n")
    for i in d:
        detail=detail+i+" "+str(d[i])+'\n'
    detail=str(ordn)+detail+'\n'   
    c2=input("Enter 'y' To confirm Your Order:")
    if c2=='y':
        fp=open("OrderList.txt",'a')
        fp.write(detail)
        fp.close()
        print("*"*10,end='')
        print("Congrats!Order Recieved!Visit Again",end='')
        print("*"*10)
    else:
        print("*"*10,end='')
        print("Thank You! ReLogin For a new Order",end='')
        print("*"*10)
    
def update():
    print("\n----What Do You Want To change in Item List----\n")
    print("1:Add an item to List\n2:Delete an Existing Item from List\n3:Update The price of an Item in the List\n")
    ch=input("Enter Your Choice:")
    c=0
    detail=''
    fp=open("items.txt",'r')
    L=fp.readlines()
    fp.close()
    if ch=='1':
        N=input("Enter Unique Item Number:")
        name=input("Enter Name Of Item To be Added:")
        p=input("Enter Price Of the The Item:")
        for i in L:
            i=i.rstrip().split(',')
            if N==i[0]:
                break
            else:
                c+=1
        if c==len(L):
            detail=N+','+name+','+p+'\n'
            print("\n--------Item Successfully Added--------")
        else:
            print(" Item Already Present In The Item List")
        
        fp=open("items.txt",'a')
        fp.write(detail)
        fp.close()
    elif ch=='2':
        fp=open("items.txt",'r')
        x=fp.readlines()
        fp.close()
        c=0
        L1=[]
        nm=input("Enter The Item Number To be Deleted:")
        for i in x:
            if nm==i.rstrip().split(',')[0]:
                c=1
                continue
            else:
                L1.append(i)
        if c==1:
            print("\n-------Item Deleted Successfully------")   
            fp=open("items.txt",'w')
            fp.writelines(L1)
            fp.close()
        else:
            print("\n------Item Not Present in The List------")
    elif ch=='3':
        num=input("Enter Item Number:")
        u=input("Enter Updated Price:")
        v=u.isdigit()
        if v==True:
            for i in range(len(L)):
                if num in L[i]:
                    s=L[i].rstrip().split(',')
                    L[i]=num+','+s[1]+','+u+'\n'
                    print("\n------Price Was Updated------")
                    break

            else:
                 print("\n------Item Not Present in The List------")
            fp=open("items.txt",'w')
            fp.writelines(L)
            fp.close()
        else:
            print("Invalid Type Of Price!!")
    else:
        print("Invalid Choice!!")
