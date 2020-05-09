n=input("range")
for i in range (1,n+1):
    for j in range (1,i+1):
        if i%j==0 and j<>1 and i<>j:
            print i,
            break
        
