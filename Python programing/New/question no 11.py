n=int(raw_input("How many students?"))
def thanks():
    print "\n","\n","Made by Parv Garg, 11th-A","\n","Submitted to Sheela Kale Mam","\n","Thanks for using me","\n","#######################End#######################"
CompWinner={}
for a in range (n):
    key=raw_input("Name of the students:")
    value=int(raw_input("Number of competition won:"))
    CompWinner[key]=value

print "The dictionary now is:"
print CompWinner
thanks()
