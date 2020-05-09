class person:
    def __init__(self,first,last):
        self.firstname= first
        self.lastname = last
    def name(self):
        return self.firstname+" "+self.lastname

class employee(person):
    def __init__(self,first,last,idp):
        person.__init__(self,first,last)
        self.idp=idp

    def emo(self):
        return self.name()+" "+self.idp

x=person("parv","garg")
y=employee("rohit","lol","9")

print x.name()
print y.emo()
