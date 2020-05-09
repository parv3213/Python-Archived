j=i=0
n=int(raw_input("Enter the range:"))
print "Comporite number from 2 to",n,":-"
for i in range (1,n):
    for j in range (1,j):
        if i%j==0 and i!=j and j!=1:
            print i,
            break
            

