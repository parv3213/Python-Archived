import os
a=open("marks.txt","r")
b=open("t.txt","w")
na=raw_input("Enter name")
co=input("code")
ma=input("Enter marks")
st=na+str(co)+str(ma)
i=0
read=" "
while read:
      read=a.readline()
      i+=1
      if i==5:
            b.write(st+"\n")
      else:
            b.write(read)
a.close()
b.close()
os.remove("marks.txt")
os.rename("t.txt","marks.txt")

            
