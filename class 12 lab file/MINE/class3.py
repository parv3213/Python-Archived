class photo:
    def __init__(self):
        self.pno=0
        self.category=""
        self.exhibit=""
    def fixexhibit(self):
        if self.category=="x":
            self.exhibit=="y"
        elif self.category=="P":
            self.exhibit=="M"
        elif self.category=="o":
            self.exhibit=="p"

    def register(self,p,c):
        self.pno=p
        self.category=c
        self.fixexhibit()

    def view(self):
        print "photono",self.pno,"category",self.category,"exhibit",self.exhibit

a,b=[],[]
n=input("enter the no of photos")
for i in range (n):
    c=input("Enter the photo no")
    d=raw_input("Enter category")
    a.append(c)
    b.append(d)
for i in range (n):
    p=photo()
    p.register(a[i],b[i])
    p.view()
    
        
        
