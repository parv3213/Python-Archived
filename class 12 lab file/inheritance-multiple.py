class vehicle:
    def __init__(self,name,model):
        self.name=name
        self.model=model
        print
        print 'Initialized vehicle',self.name
    def details(self):
        print 'Name:',self.name
        print 'Model:',self.model
class car(vehicle):
    def __init__(self,name,model,price):
        vehicle.__init__(self,name,model)
        self.price=price
        vehicle.details(self)
        print "Price:",self.price
class truck(vehicle):
    def __init__(self,name,model,price):
        vehicle.__init__(self,name,model)
        self.price=price
        vehicle.details(self)
        print "Price:",self.price
#main
c=car('lamborghini',3277823,38888483)
T=truck("JEEP",2,324234)
vehicle=[c,T]
print
print "                --XX--                  "
for member in vehicle:
    print
    member.details()
