class person:
    def __init__(self,first,last):
        self.firstname=first
        self.lastname=last
    def name(self):
        return self.firstname+' '+self.lastname
class employee(person):
    def __init__(self,first,last,staffnum):
        person.__init__(self,first,last)
        self.staffnumber=staffnum
    def getemployee(self):
        return self.name()+" "+self.staffnumber
#main
x=person('Parv','Garg')
y=employee('xyz','Dol','1001')

print x.name()
print y.getemployee()
