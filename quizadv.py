#Quiz

print "$$$$$$$ So here we are again to test your knowledge and skills $$$$$$$"
print
print """           <<<< Rules >>>>
|1.	You start from 100 points.|
|2.	You can decide how much you want to bet for each question.|
|3.	You have to enter only specified commands or the application may collapse.|
|4.	You have to select from General and Science Quiz.|
|Best of Luck.... :):)|
"""
print
print

am=["Bromine","Nitrogen"]

def check(u,c,r,b,a,f,p):
    if b==f:
            u+=a    
            c+=1
            print "Correct answer is:",am[p]
            print "Your answer is correct, You have points,",u
            return u
    else:
            u-=a
            r+=1
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                last()
    return u
    

def science(u,c,r):
    print
    print "Here we will test your general knowledge"
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        print
        
        print """Question 1
Which of the following is a non metal that remains liquid at room temperature?
Your choices are-
1.Phosphorous
2.Bromine
3.Chlorine
4.Helium"""
        b=input("Enter your choice:-")
        f=2
        p=1
        check(u,c,r,b,a,f,p)
    
    else:
        last()
    cis()
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        print
        print """Question 2
Brass gets discoloured in air because of the presence of which of the following gases in air?
Your choices are-
1.Oxygen
2.Hydrogen sulphide
3.Carbon dioxide
4.Nitrogen"""
        b=input("Enter your choice:-")
        f=4
        p=2
    else:
        last()


    cis()
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        print
        print """Question 3
Which of the following metals forms an amalgam with other metals?
Your choices are-
1.Tin
2.Mercury
3.Lead
4.Zinc"""
        b=input("Enter your choice:-")
        if b==2:
            u+=a
            c+=1
            print "Your answer is correct, You have points,",u
        else:
            u-=a
            r+=1
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                last()
    else:
        last()




    cis()
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        print
        print """Question 4
Which of the following is used in pencils?
Your choices are-
1.Graphite
2.Silicon
3.Charcoal
4.Phosphorous"""
        b=input("Enter your choice:-")
        if b==1:
            u+=a
            c+=1
            print "Your answer is correct, You have points,",u
        else:
            u-=a
            r+=1
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                last()
    else:
        last()


    cis()
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        print
        print """Question 5
Which Gas is usually filled in electric bulb?
Your choices are-
1.Nitrogen
2.Hydrogen
3.Carbon Dioxide
4.Oxygen"""
        b=input("Enter your choice:-")
        if b==1:
            u+=a
            c+=1
            print "Your answer is correct, You have points,",u
        else:
            u-=a
            r+=1
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                last()
    else:
        last()


    cis()
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        
        print """Question 6
Washing Soda is the common name for?
Your choices are-
1.Sodium Bicarbonate 
2.Calcium Bicarbonate 
3.Sodium Carbonate 
4.Calcium Carbonate"""
        b=input("Enter your choice:-")
        if b==3:
            u+=a
            c+=1
            print "Your answer is correct, You have points,",u
        else:
            u-=a
            r+=1
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                last()
    else:
        last()
    cis()
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        print
        print """Question 7
Which of the Gas is not know as Green House Gas?
Your choices are-
1.Methane
2.Nitro Oxide 
3.Carbon Dioxide 
4.Hydrogen"""
        b=input("Enter your choice:-")
        if b==4:
            u+=a
            c+=1
            print "Your answer is correct, You have points,",u
        else:
            u-=a
            r+=1
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                last()
    else:
        last()
    cis()
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        print
        print """Question 8
Which of the Gas is not know as Green House Gas?
Your choices are-
1.Methane
2.Nitro Oxide 
3.Carbon Dioxide 
4.Hydrogen"""
        b=input("Enter your choice:-")
        if b==4:
            u+=a
            c+=1
            print "Your answer is correct, You have points,",u
        else:
            u-=a
            r+=1
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                last()
    else:
        last()
    report(c,r)
    print
    cis()
    switch(u)


def generalknowlegde(u,c,r):
    print
    print "Here we will test your general knowledge"
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        print
        
        print """Question 1
Who is the father of Geometry?
Your choices are-
1.Aristotle
2.Euclid
3.Pythagoras
4.Kepler"""
        b=input("Enter your choice:-")
        if b==2:
            u+=a
            c+=1
            print "Your answer is correct, You have points,",u
        else:
            u-=a
            r+=1
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                last()
    else:
        last()
    cis()
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        print    
        print """Question 2
Who was known as Iron man of India?
Your choices are-
1.Govind Ballabh Pant
2.Jawaharlal Nehru
3.Subhash Chandra Bose
4.Sardar Vallabhbhai Patel"""
        b=input("Enter your choice:-")
        if b==4:
            u+=a
            c+=1
            print "Your answer is correct, You have points,",u
        else:
            u-=a
            r+=1
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                last()
    else:
        last()
    cis()
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        print
        print """Question 3
Who invented the BALLPOINT PEN?
Your choices are-
1.Biro Brothers
2.Waterman Brothers
3.Bicc Brothers
4.Write Brothers"""
        b=input("Enter your choice:-")
        if b==1:
            u+=a
            c+=1
            print "Your answer is correct, You have points,",u
        else:
            u-=a
            r+=1
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                last()
    else:
        last()



    cis()
    print
    print "You have points:-",u
    print "Enter your bet, though it must fit between 0 to",u
    a=input("::::-")
    if 0<=a<=u:
        print
        print """Question 4
Which scientist discovered the radioactive element radium?
Your choices are-
1.Isaac Newton
2.Albert Einstein
3.Benjamin Franklin
4.Marie Curie"""
        b=input("Enter your choice:-")
        if b==4:
            u+=a
            c+=1
            print "Your answer is correct, You have points,",u
            thanks(c,r)
        else:
            u-=a
            r+=1
            print "Your answer is wrong.You have points,",u
            if u==0:
                print "You are out of point"
                last()
    else:
        last()
    report(c,r)
    print
    cis()
    switch(u)




def choice():
    print
    a=raw_input("Enter from the above choices:")
    if a== "1":
        vis()
        print
        print"Here you go for General Knowledge Quiz. Best of luck in Advance :-)"
        print
        vis()
        generalknowlegde(u,c,r)
    elif a=="2":
        vis()
        print
        print"Here you go for Science Quiz. Best of luck in Advance :-)"
        print
        vis()
        science(u,c,r)
    else:
        print
        print
        pls()
        
   
def pls():
    print "PLEASE TRY TO SELECT THE RIGHT CHOICE OR YOU WILL END UP"
    print
    a=raw_input("""Enter from the following choices:
(1) General Knowledge Quiz
(2) Science quiz
Enter from following choices:""")
    if a== "1":
        print
        print"Here you go for General Knowledge Quiz. Best of luck in Advance :-)"
        print
        generalknowlegde(u,c,r)
        
    elif a=="2":
        print
        print"Here you go for Science Quiz. Best of luck in Advance :-)"
        print
        science(u,c,r)
    else:
        last()

def thanks(c,r):
    print
    print
    print "Thanks for your time. Made by: Parv Garg and Ammar Alam"
    cis()
    vis()
    cis()
    vis()
    print
    report(c,r)
    print "Press any key to exit"
    a=raw_input()
    exit()

def last():
    print
    print "SORRY BUT YOU ARE UNBALE TO COPE UP WITH US,"
    print "This will end now, better luck next time :-)"
    thanks(c,r)
    
def starting():
    print """Select your Quiz type:-
            (1) General Knowledge Quiz
            (2) Science quiz"""
    choice()
def vis():
    print"_________________________________________________________________________________________________________________"
def cis():
    print"#################################################################################################################"
def switch(u):
    vis()
    cis()
    print "Do you want to switch to the next quiz with points",u,"?"
    print"""If Yes-1
If No-2"""
    x=raw_input()
    if x=="1":
        starting()
    else:
        thanks(c,r)

def report(c,r):
    print
    cis()
    vis()
    print "Your Report"
    print "+++++++++++++++No of right Answers=",c,"+++++++++++++++"
    print "+++++++++++++++No of Wrong Questions=",r,"++++++++++++++"
    print "+++++++++++++++Total no of Question=",c+r,"++++++++++++++"

u=100
c=0
r=0
starting()

