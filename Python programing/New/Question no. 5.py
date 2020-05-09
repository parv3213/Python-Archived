s=raw_input("Enter a String:-")

def thanks():
    print
    print
    print "Thanks for using me"
    print "Made by Parv Garg, 11th-A"
    print "Submitted to Sheela Kale Mam" 
    print "#######################End#######################"

lc=uc=d=al=0
for a in s:
    if a.islower():
        lc+=1
    elif a.isupper():
        uc+=1
    elif a.isdigit():
        d+=1
    if a.isalpha():
        al+=1

print "Number of uppercase letters:",uc
print "Number of lowercase letters:",lc
print "Number of alphabets:",al
print "Number of digits:",d
thanks()
