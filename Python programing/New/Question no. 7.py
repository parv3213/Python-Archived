string=raw_input("Enter a string:")
def thanks():
    print "\n","\n","Made by Parv Garg, 11th-A","\n","Submitted to Sheela Kale Mam","\n","Thanks for using me","#######################End#######################"
lenght= len(string)
mid=lenght/2
rev=-1
for a in range(mid):
    if string[a]==string[rev]:
        a+=1
        rev-=1
    else:
        print string,"is not a palindrome"
        break
else:
    print string,"is a palindrome"
thanks()
