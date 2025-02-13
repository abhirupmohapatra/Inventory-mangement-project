import items
import orders
def work():
    while True:
        print("--"*10,end='')
        print("What do you want to do?",end='')
        print("--"*10)
        print("\t1:Update Item List\n\t2:Dispatch Order\n\t3:View the item List\n\t4:close")
        ch=input("Enter:")
        if ch=='1':
            items.update()
        elif ch=='2':
            orders.dispatch()
        elif ch=='3':
            fp=open("items.txt",'r')
            print(fp.read())
            fp.close()
        elif ch=='4':
            print("Thank You! Login Again To Have Access")
            break
