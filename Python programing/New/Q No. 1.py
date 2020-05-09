n=raw_input("Enter your name:-")
a=raw_input("Enter the string:-")
b=raw_input("Enter the string to be searched:-")
x=n.capitalize()
def string0():
 print"1. in range Operator"
 print"2. not in range function"
 print"3. Concatenation Operator"
 print"4. Replication Operator"
 print"5. Unicode Operator"
 ch=input("Enter your choice:-")
 if ch==1:
    print a in b
 if ch==2:
    print a not in b
 if ch==3:
    print a + b
 if ch==4:
    num=input("Enter the number:-")
    print"1. To get Replication of First String your choice is 1"
    print"2. To get Replication of Second String your choice is 2"
    c=input("Enter your choice:-")
    if c==1:
        print a*num
    else:
        print b*num
 if ch==5:
    print "To get unicode of First String------1"
    print "To get unicode of Second String------2"
    e=input("Enter your choice:-")
    if e==1:
     l=len(a)
     for i in range(0,l):
        print"The Unicode of",a[i],"is:-",ord(a[i])
    else:   
     r=len(b)
     for j in range(0,r):
        print"The Unicode of",b[j],"is:-",ord(b[j])
 
 print
 print n,"Do you want to continue??"
 print" To continue Program your choice is 1"
 print" To end the Program your choice is 2"
 h=input("Please enter your choice:-")
 if h==1:
    string0()
 else:
    exit()
string0()
def thanks():
    print "\n","\n","Made by Parv Garg, 11th-A","\n","Submitted to Sheela Kale Mam","\n","Thanks for using me","\n","#######################End#######################"
thanks()

