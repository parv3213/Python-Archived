l=raw_input("Enter a line:-")
lcount=ucount=0
dcount=acount=0
for a in l:
    if a.islower():
        lcount +=1
    elif a.isupper():
        ucount +=1
    elif a.isdigit():
        dcount +=1
    if a.isalpha():
        acount +=1
print "Number of uppercase letters:",ucount
print "Number of lowercase letters:",lcount
print "Number of alphabets:",acount
print "Number of digits:",dcount
