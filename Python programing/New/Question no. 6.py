l=raw_input("Enter a line:")
s=raw_input("Enter a sub-string:")
def thanks():
    print "\n","\n","Made by Parv Garg, 11th-A","\n","Submitted to Sheela Kale Mam","\n","Thanks for using me","#######################End#######################"
lenl=len(l)
lens=len(s)
start=0
end=lenl
count=0
while True:
    pos=l.find(s,start,end)
    if pos<>-1:
        count+=1
        start=pos+lens
    else:
        break
    if start>=lenl:
        break
print "No of occurance of",s,":",count
thanks()
        
