string=raw_input("Enter a string:")
def thanks():
    print "\n","\n","Made by Parv Garg, 11th-A","\n","Submitted to Sheela Kale Mam","\n","Thanks for using me","\n","#######################End#######################"
lenght =len(string)
print "Original string:",string
string2=""
for a in range(0,lenght,2):
    string2+=string[a]
    if a<(lenght-1):
        string2+=string[a+1].upper()
    print "Alternative capitalized string:",string2
thanks()
