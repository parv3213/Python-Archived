import random
n=random.randint(10,50)
a=0
while a<5:
    guess=input("Guess no b/t 10-50-")
    if guess==n:
        print "You win :)"
        break
    else:
        a+=1
if not a<5:
    print "You lose, The number is=",n
