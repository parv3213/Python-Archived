class society:
    def __init__(self):
        self.sname='minal residency'
        self.flat='A type'
        self.hno=20
        self.nom=3
        self.inc=100000
    def allocate(self):
        if self.inc>=100000:
            self.flat='A type'
        elif self.inc>=25000 and self.inc<=75000:
            self.flat='B type'
        elif self.inc<=25000:
            self.flat='C type'
    def input(self,sname,hno,nom,inc):
        self.inc=inc
        self.sname=sname
        self.hno=hno
        self.nom=nom
        self.allocate()
    def showdata(self):
        print
        print 'Society name   ---> ',(self.sname)
        print 'House number   ---> ',(self.hno)
        print "Flat no is     ---> ",(self.flat)
        print "No. of members ---> ",(self.nom)
        print "Income is      ---> ",(self.inc)
#main...
n = int(raw_input("Enter no. of house:-"))
for i in range(n):
    print
    A = str(raw_input("Enter society name:-"))
    B = int(raw_input("Enter ur house number:-"))
    D = int(raw_input("Enter ur income:-"))
    C = int(raw_input("Enter no. of members:-"))
    obj = society()
    obj.input(A,B,C,D)
    obj.showdata()
