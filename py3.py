class specialengine(object):
    def __init__(self,p):
        self.power=p
    def ignition(Self):
        print "Engine started"
class car(object):
    def __init__(self,clr,seats):
        self.colour=clr
        self.seats=seats
    def gears(self,gears):
        print "changed to gear:",gears

    def turn(self,direction):
        print "changed to direction",direction

class racingcar(specialengine,car):
    def __init__(self,clr,seats,p,tr,speed):
        specialengine.__init__(self,p)
        car.__init__(self,clr,seats)
        self.turnradius=tr
        self.speed=speed
        print "racing car instance created"

    def start(self):
        self.ignition()
        self.gears(2)
        print "ready"

rcar=racingcar("blue",2,750,6,200)
rcar.start()
rcar.turn("left")
