import random
print "rock=1 paper=2 scissors=3"



for i in range (100):
    a= random.randint(1,3)
    b=int(raw_input("User choice:"))
    if a==b:
        print "Tie"
    elif (b==1 and a==3) or (b==2 and a==1) or (b==3 and a==2):
        print "USER WON"
    else:
        print "COMPUTER WON"
    
    

    
