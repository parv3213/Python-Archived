# QUIZ BY PARV GARG


aq=[0,"""Question 1
Who is the father of Geometry?
Your choices are-
1.Aristotle
2.Euclid
3.Pythagoras
4.Kepler""","""Question 2
Who was known as Iron man of India?
Your choices are-
1.Govind Ballabh Pant
2.Jawaharlal Nehru
3.Subhash Chandra Bose
4.Sardar Vallabhbhai Patel"""]

am=[0,"Euclid","Sardar Vallabhbhai Patel"]


def check(u,c,r,b,a,f,p):
    if b==f:
            u+=a    
            c+=1
            print "Correct answer is:",am[p]
            print "Your answer is correct, You have points,",u
            return u,c
    else:
            u-=a
            r+=1
            print "Correct answer is:",am[p]
            print "Your answer is wrong.You have points,",u
            return u,r
            if u==0:
                print "You are out of point"
                last()
    



def error(a):
    try:
        a=int(a)
        a=a+2
        return a
        
    except ValueError:
        exit()
    

def thanks(c,r):
    gap(2)
    print "Thanks for your time. Made by: Parv Garg and Ammar Alam"
    gap(3)
    gap(4)
    gap(2)
    report(c,r)
    print "Press any key to exit"
    a=raw_input()
    exit()
    
def gap(p):
    if p==0:
        print
    elif p==1:
        print
        print
    elif p==2:
        print
        print
        print
    elif p==3:
        print "*-*"*5
    elif p==4:
        print "___"*5
def last():
    print
    print "SORRY BUT YOU ARE UNBALE TO COPE UP WITH US,"
    print "This will end now, better luck next time :-)"
    thanks(c,r)
    

def switch(u):
    gap(2)
    gaap(3)
    print "Do you want to switch to the next quiz with points",u,"?"
    print"""If Yes-1
If No-2"""
    x=raw_input()
    if x=="1":
        starting()
    else:
        thanks(c,r)
def report(c,r):
    gap(2)
    gap(4)
    print "Your Report"
    print "+++++++++++++++No of right Answers=",c,"+++++++++++++++"
    print "+++++++++++++++No of Wrong Questions=",r,"++++++++++++++"
    print "+++++++++++++++Total no of Question=",c+r,"++++++++++++++"

# GENERAL QUIZ

def generalknowlegde(u,c,r):
    print
    print "Here we will test your general knowledge"
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=raw_input("Enter your bet")
    error(a)
    print a+a
    if 0<=a<=u:
        gap(2)
        print aq[1]
        gap(1)
        b=input("Enter your choice:-")
        f=2
        p=1
        check(u,c,r,b,a,f,p)
    else:
        print "j"
        last()
    gap(3)
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        gap(2)
        print aq[1]
        gap(1)
        b=input("Enter your choice:-")
        f=4
        p=2
        check(u,c,r,b,a,f,p)
    else:
        print "he"
        last()

    

            
def start():
    print "$$$$$$$ So here we are again to test your knowledge and skills $$$$$$$"
    print
    print """           <<<< Rules >>>>
|1.	You start from 100 points.|
|2.	You can decide how much you want to best for each question.|
|3.	You have to enter only specified commands or the application may collapse.|
|4.	You have to select from General and Science Quiz.|
|Best of Luck.... :):)|
"""
    print """Select your Quiz type:-
            (1) General Knowledge Quiz
            """
    print
    a=raw_input("Enter from the above choices:")
    if a== "1":
        gap(3)
        print
        gap(4)
        generalknowlegde(u,c,r)
    else:
        gap(2)
        last()
    
    


u=100
c=r=a=0
start()
