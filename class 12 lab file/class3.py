class iteminfo():
    def __init__(self):
        self.ic=0
        self.itn=None
        self.p=0
        self.qu=0
        self.dis=0
        self.np=None
    def finddis(self):
        if self.qu<=10:
            self.dis=0
        if self.qu<20 and self.qu>=11:
            self.dis=float((15*self.p*self.qu)/100)
        if self.qu>=20:
            self.dis=float((20*self.p*self.qu)/100)
    def buy(self,ic,itn,p,qu):
        self.ic=ic
        self.itn=itn
        self.p=p
        self.qu=qu
        self.finddis()
        self.np=self.p*self.qu-self.dis
    def showall(self):
        print '\n',"Item code     :    ",self.ic,'\n',"Item name     :    ",self.itn,'\n',"Item price    : Rs ",self.p,'\n',"Item quantity :    ",self.qu,'\n',"Discount      : Rs ",self.dis, '\n',"Net price     : Rs ",self.np
        
            
#main             
n=int(raw_input('Enter the no. of customer'))        
for i in range(n):
    print
    ic=int(raw_input('Enter the item code'))
    itn=raw_input('Enter the itemname')
    p=int(raw_input('Enter the price'))
    qu=int(raw_input('Enter the quantity'))
    o=iteminfo()
    o.buy(ic,itn,p,qu)
    o.showall()     
