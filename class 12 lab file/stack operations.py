# Stack Operations
# """1.push, 2.pop 3.peek 4.display 5.exit"""
def isempty(a):
      if len(a)==0:
            return True
      else:
            return False 
      
def push1(a,b):
      a.append(b)
      
def pop1(a):
      if isempty(a):
            print "Stack is empty"
      else:
            item=a.pop()
            print "Poped item is:",item
def peek1(a):
      if isempty(a):
            print "Stack Empty"
      else:
            top=len(a)-1
            item=a[top]
            print item
def display(a):
      if isempty(a):
            print "StacK Empty"
      else:
            top=len(a)-1
            print a[top],"<--Top"
            i=0
            for i in range(top-1,-1,-1):
                  print a[i]
a=[]
while True:
      print """
Stack Operations:
      1.Push
      2.Pop
      3.Peek
      4.Display
      5.Exit
"""
      
      ch=int(raw_input("Enter your choice:"))
      if ch==1:
            b=int(raw_input("Enter the element to be pushed:"))
            push1(a,b)
      elif ch==2:
            pop1(a)
      elif ch==3:
            peek1(a)
      elif ch==4: 
            display(a)
      else:
            break
            


