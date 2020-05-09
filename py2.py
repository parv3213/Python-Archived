class vehical(object):
    def __init__(self,l,w):
        self.lenght=l
        self.width=w

    def define(self):
        print "The lenght is:",self.lenght ," and width is:", self.width

class car(vehical):
    def __init__(self,clr,seats,l,w):
        vehical.__init__(self,l,w)
        self.seats=seats
        self.colour=clr

    def changedtogear(self,gr):
        print "changed to gears",gr
    def turn(self,direction):
        print "turned to direction",direction

class racingcar(car):
    def __init__(self,clr,seats,l,w,tlr,spd):
        car.__init__(self,clr,seats,l,w)
        self.turningradius=tlr
        self.speed=spd
        print "racing car insurance created"

    def start(self):
        self.define()
        self.changedtogear(2)
        print "car starts"


a=racingcar("blue",2,200,100,2000,20)
a.start()
a.turn("nirth")
