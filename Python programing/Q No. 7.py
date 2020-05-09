import string
n=raw_input("Enter your sentence:-")
r=len(n)
print n[0].upper(),
for i in range(1,r):
    if n[i].isspace()==True:
        print n[i],
        print n[i+1].upper(),
    if n[i].isspace()==False:
        if n[i-1].isspace()==False:
           print n[i],
