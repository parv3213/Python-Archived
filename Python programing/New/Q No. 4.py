ch=0
list=[]
while True:
    print"List Manipulation Menu"
    print"1. Add Element(s)"
    print"2. Modify Element"
    print"3. Delete Element"
    print"4. Sort List"
    print"5. Display List"
    print"6. Exit"
    c=int(raw_input("Enter your choice:-"))
    if c==1:
        print"1. Add Element"
        print"2. Add List"
        r=raw_input("Enter your choice 1 or 2:-")
        if r==1:
            i=raw_input("Enter the Element to be added:-")
            p=raw_input("Enter the position:-")
            list.insert(p,i)
        else:
            h=raw_input("Enter the list to be added:-")
            list.extend(h)
        print"Successfully Added"
    if c==2:
        p=raw_input("Enter position where to be added:-")
        i=raw_input("Enter new value for element:-")
        o=list[p]
        list[p]=i
        print o,"modified with value",i
    if c==3:
        print"1. Delete element by position"
        print"2. Delete element by value"
        r=raw_input("Enter your choice 1 or 2:-")
        if r==1:
            p=raw_input("Enter position where to delete:-")
            i=list.pop(p)
            print i,"deleted"
        else:
            i=raw_input("Enter element to be deleted:-")
            p=list.remove(i)
            print "Successfully Deleted"
    if c==4:
        print"1. Ascending"
        print"2. Descending"
        r=raw_input("Enter your choice 1 or 2:-")
        if r==1:
            list.sort()
        else:
            list.sort(reverse=True)
    if c==5:
        print list
    if c==6:
        break
    else:
        print "Valid choices are 1 to 6.."
        
def thanks():
    print "\n","\n","Made by Parv Garg, 11th-A","\n","Submitted to Sheela Kale Mam","\n","Thanks for using me","\n","#######################End#######################"
thanks()
