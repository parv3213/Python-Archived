def overlapping(a,b):
    l1=len(a)
    l2=len(b)
    for i in range(l1):
        for j in range(l2):
            if a[i]==b[j]:
                return True
        else:
            return False

a=eval(raw_input("Enter the main list:"))
b=eval(raw_input("Enter a list which is to be checked in list 'a':"))
print "The result",overlapping(a,b)
def thanks():
    print "\n","\n","Made by Parv Garg, 11th-A","\n","Submitted to Sheela Kale Mam","\n","Thanks for using me","\n","#######################End#######################"
thanks()
