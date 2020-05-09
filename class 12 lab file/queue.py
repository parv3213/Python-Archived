def cls():
    print"\n"*100

def isempty(qu):
    if qu==[]:
        return 1
    else:
        return 0
    
def Enquene(qu,item):
    qu.append(item)
    if len(qu)==1:
        front=rear=0
    else:
        rear=len(qu)-1

def dequeue(qu):
    if isempty(qu):
        return"Underflow"
    else:
        item=qu.pop(0)
    if len(qu)==0:
        front=rear=0
        
    return item

def peek(qu):
    if isempty(qu):
        return"Underflow"
    else:
        front=0
        return qu[front]
def display(qu):
    if isempty(qu):
        print"Queue empty"
    elif len(qu)==1:
        print qu[0],"front,rear"
    else:
        front=0
        rear=len(qu)-1
        print qu[front],"front"
        for a in range(1,rear):
            print qu[a]
        print qu[rear],"rear"

#main
queue=[]
front=0
while front==0:
    print"""Queue operations
            1.Enquene
            2.Dequeue
            3.Peek
            4.Display queue
            5.Exit"""
    ch=int(raw_input("Enter your choice(1-5):"))

    if ch==1:
        item=int(raw_input("Enter item:"))
        Enquene(queue,item)
        
    elif ch==2:
        item=dequeue(queue)
        if item=="Underflow":
               print"Underflow! queue is empty!"
        else:
               print"Dequeueped item is",item
        
    elif ch==3:
        item=peek(queue)
        if item=="Underflow":
            print"Underflow queue is empty"
        else:
            print"Frontmost item is ",item
        
    elif ch==4:
        display(queue)
        
    elif ch==5:
        break
    else:
        print"Invalid choice"
        
