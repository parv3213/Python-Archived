class vehicle(object):
    def __init__(self,l=0,w=0):
        self.length=l
        self.width=w
        print "V"
    def define(self):
        print'Vehicle with length-',self.length,'In & width-',self.width,'in'
        
class car(vehicle):
    def __init__ (self,clr,seats,l,w):
        vehicle.__init__(self,l,w)
        self.colour=clr
        self.seatingcapacity=seats
        print "V"
    def changegears(self,gr):
        print 'Changed to gear',gr
        
    def turn(self,direction):
        print 'Turned to',direction,"direction"
        
class racingcar(car):
    def __init__(self,clr,seats,l,w,tr,spd):
        car.__init__(self,clr,seats,l,w)
        self.turnradius=tr
        self.speed=spd
        print'Racingcar insurance created'
        
    def start(self):
        self.define()
        self.changegears(2)
        print'Racing car starts-ready to vroom!'
#main
n=int(raw_input('Enter the no. of vehicles:-'))        
for i in range(n):
    print
    clr=raw_input('Enter the colour:-')
    seats=int(raw_input('Enter the no. of seats:-'))
    l=int(raw_input('Enter the length:-'))
    w=raw_input('Enter the width:-')
    spd=int(raw_input('Enter the speed:-'))
    tr=int(raw_input('Enter the turnradius:-'))
    direction=raw_input('Enter the direction:-')
    print
    rcar=racingcar(clr,seats,l,w,tr,spd)
    rcar.start()
    rcar.turn(direction)
