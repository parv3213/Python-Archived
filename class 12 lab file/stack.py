def isempty(stk):
    if stk==[]:
        return 1
    else:
        return 0
    
def push(stk,item):
    stk.append(item)
    top=len(stk)-1

def pop(stk):
    if isempty(stk):
        return"Underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=0
        else:
            top=len(stk)-1
        return item

def peek(stk):
    if isempty(stk):
        return"Underflow"
    else:
        top=len(stk)-1
        return stk[top]
def display(stk):
    if isempty(stk):
        print"Stack empty"
    else:
        top=len(stk)-1
        print stk[top],",-top"
        for i in range(top-1,-1,-1):
            print stk[a]

#main
stack=[]
top=0
while top==0:
    print"""Stack operations
            1.Push
            2.Pop
            3.Peek
            4.Display stack
            5.Exit"""
    ch=int(raw_input("Enter your choice(1-5):"))

    if ch==1:
        item=int(raw_input("Enter item:"))
        push(stack,item)
    elif ch==2:
        item=pop(stack)
        if item=="Underflow":
               print"Underflow! Stack is empty!"
        else:
               print"Popped item is",item
    elif ch==3:
        item=peek(stack)
        if item=="Underflow":
            print"Underflow stack is empty"
        else:
            print"Topmost item is "<item
    elif ch==4:
        display(stack)
    elif ch==5:
        break
    else:
        print"Invalid Choice"
   
