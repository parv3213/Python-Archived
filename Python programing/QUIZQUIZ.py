#Quiz
print "We welcome you to APS quiz and skills"
print
print


def pls():
    print "PLEASE TRY TO SELECT THE RIGHT CHOICE"
    starting()
        
def thanks():
    print "Thanks for your time. Made by: Parv Garg and Ammar Alam"

#Random
def luck():
    import random
    n=random.randint(10,20)
    a=0
    while a<5:
        guess=input("Guess no b/t 10-20-")
        if guess==n:
            print "You win :)"
            print "The number is=",n
            print "If you want to the start again press 1"
            a=input()
            if a==1:
                starting()
            else:
                pls()
            
        else:
            a+=1
    if not a>5:
        print "You lose, The number is=",n
        print "If you want to the start again press 1"
        a=input()
        if a==1:
            starting()
        else:
            pls()

#For General science Quiz
def science():
    u=100
    print "How much you want to bet for the 1st question?"
    print "Enter the points"
    print "You have points",u
    print "Enter the bet b/t",u,"-o, or statement will break and GAME OVER"
    a=input("Pls Enter your bet for this question")
    if a<=u:
        print "Question 1"
        print "Which of the following is a non metal that remains liquid at room temperature?"
        print "Your choices are-"
        print """1.Phosphorous
    2.Bromine
    3.Chlorine
    4.Helium"""
        b=input("Enter your choice")
        if b==2:
            u+=a
            print "Your points",u
            print "Your answer is correct you may continue to next question"
    else:
        print "Enter the bet b/t",u,"-o"
        exit()




        
    print
    print
    print
    a=input("Pls Enter your bet for this question")
    if a<+=u:
        print "Question 2"
        print "Brass gets discoloured in air because of the presence of which of the following gases in air?"
        print "Your choices are-"
        print """1.Oxygen
2.Hydrogen sulphide
3.Carbon dioxide
4.Nitrogen"""
        b=input("Enter your choice")
        if b==2:
            print "Your answer is correct you may continue to next question"
            u+=100
            print "Your points",u
        else:
            print "Your answer is wrong. You may quit."
            a=input("Press 1 to end or 2 to continue")
            if a==1:
                print
                print
                thanks()
                b=input("Press 1 to exit")
                exit()
             
            else:
                 generalknowlegde()
    else:
        print "Enter the bet b/t",u,"-o"
        exit()


    print
    print
    a=input("Pls Enter your bet for this question")
    if a<=u:
        print
        print "Question 3"
        print "Which of the following metals forms an amalgam with other metals?"
        print "Your choices are-"
        print """1.Tin
2.Mercury
3.Lead
4.Zinc"""
        b=input("Enter your choice")
        if b==2:
            print "Your answer is correct you may continue to next question"
        else:
            print "Your answer is wrong. You may quit."
            a=input("Press 1 to end or 2 to continue")
            if a==1:
                print
                print
                thanks()
                b=input("Press 1 to exit")
                exit()
             
            else:
             generalknowlegde()
    else:
        print "Enter the bet b/t",u,"-o"
        exit()

    print
    print
    a=input("Pls Enter your bet for this question")
    if a<=u:
        print
        print "Question 4"
       

        
        print " Which of the following is used in pencils?"
        print "Your choices are-"
        print """1.Graphite
2.Silicon
3.Charcoal
4.Phosphorous"""
        b=input("Enter your choice")
        if b==1:
            print "Your answer is correct you may continew to next question"
            u+=100
            print "Your points",u
        else:
            print "Your answer is wrong. You may quit."
            a=input("Press 1 to end or 2 to continue")
            if a==1:
                print
                print
                thanks()
                b=input("Press 1 to exit")
                exit()
             
            else:
                 generalknowlegde()
    else:
        print "Enter the bet b/t",u,"-o"
        exit()



#For General Knowledge Quiz
def generalknowlegde():
    print
    print
    print "Here we will test your general knowledge"
    print
    print
    print "Question 1"
    print "Who is the father of Geometry?"
    print "Your choices are-"
    print """1.Aristotle
2.Euclid
3.Pythagoras
4.Kepler"""
    b=input("Enter your choice")
    if b==2:
        print "Your answer is correct you may continue to next question"
    else:
        print "Your answer is wrong. You may quit."
        a=input("Press 1 to end or 2 to continue")
        if a==1:
            print
            print
            thanks()
            b=input("Press 1 to exit")
            exit()
             
        else:
             science()
    print
    print
    print
    print "Question 2"
    print "Who was known as Iron man of India?"
    print "Your choices are-"
    print """1.Govind Ballabh Pant
2.Jawaharlal Nehru
3.Subhash Chandra Bose
4.Sardar Vallabhbhai Patel"""
    b=input("Enter your choice")
    if b==4:
        print "Your answer is correct you may continue to next question"
    else:
        print "Your answer is wrong. You may quit."
        a=input("Press 1 to end or 2 to continue")
        if a==1:
            print
            print
            thanks()
            b=input("Press 1 to exit")
            exit()
             
        else:
             science()
    print
    print
    print
    print "Question 3"
    print "Who invented the BALLPOINT PEN?"
    print "Your choices are-"
    print """1.Biro Brothers
2.Waterman Brothers
3.Bicc Brothers
4.Write Brothers"""
    b=input("Enter your choice")
    if b==1:
        print "Your answer is correct you may continew to next question"
    else:
        print "Your answer is wrong. You may quit."
        a=input("Press 1 to end or 2 to continue")
        if a==1:
            print
            print
            thanks()
            b=input("Press 1 to exit")
            exit()
             
        else:
             science()
    print
    print
    print
    print "Question 4"
    print "Which scientist discovered the radioactive element radium?"
    print "Your choices are-"
    print """1.Isaac Newton
2.Albert Einstein
3.Benjamin Franklin
4.Marie Curie"""
    b=input("Enter your choice")
    if b==4:
        print "Your answer is correct you may continew to next question"
    else:
        print "Your answer is wrong. You may quit."
        a=input("Press 1 to end or 2 to continue")
        if a==1:
            print
            print
            thanks()
            b=input("Press 1 to exit")
            exit()
             
        else:
             science()

#Choice
def choice():
    print
    a=input("Please enter from the following choices:")
    if a==1:
        print
        print"Okk so you want to face General Quiz"
        print
        generalknowlegde()
    elif a==2:
        print
        print"Okk so you want to face General Quiz"
        print
        science()
    elif a==3:
        print
        print"Okk so you want to face General Quiz"
        print
        luck()
    else:
        pls()
        print
        print
        starting()

def starting():
    print """Please select which type of questions you want to face
            (1) To face general knowledge quiz
            (2) To face general science quiz
            (3) To try your luck"""
    choice()



starting()
        


    
