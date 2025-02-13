def dispatch():
    print("-------Live Orders------\n")
    fp=open("orderlist.txt",'r')
    print(fp.read())
    fp.close()
    ordn=input("Enter Order Number To be Dispatched:")
    fp=open("orderlist.txt",'r')
    L=fp.readlines()
    fp.close()
    L1=[]
    c=0
    for i in L:
        if ordn==i.rstrip().split(",")[0]:
            c=1
            continue
        else:
            L1.append(i)
    if c==1:
        fp=open("orderList.txt",'w')
        fp.writelines(L1)
        fp.close()
        print("\n------Order Dispatched Successfully------")
    else:
        print("\nOrder Number Entered Not In Order List")
        
