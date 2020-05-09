class r(Exception):
    pass
e1=r("Hour not in range 00-23 Error")
e2=r("Minute not in range 00-59 Error")
try:
    class Time():
        def __init__(self,h,m):
            self.hpur=h
            self.min=m
        def check(self):
            if 24<self.hour or 0>self.hour:
                raise e1
            if 59<self.min or self.min<0:
                raise e2
        h=input("Enter the hour in 24hr:")
        m=input("Enter minute:")
        ob=Time(h,m)
        ob.check()
        print
        print "Time is",h,":",m
except r,e:
    print e.message
    print "Value entered are wrong"
