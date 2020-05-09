import os
o=open("marks.txt","r")
p=open("marks.txt","a")
r=input("Enter roll no")
n=raw_input("Enter name")
m=input("Enter marks")
to="\n"+str(r)+","+n+","+str(m)+"\n"
s=0
v=" "
while v:
    v=o.readline()
    s+=1
    if s==3:
        print "o"
        p.write(to)
    
p.close()
o.close()

