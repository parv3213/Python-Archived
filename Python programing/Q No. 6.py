l=raw_input("Enter a line:-")
sub=raw_input("Enter the Substring:-")
r=len(l)
s=len(sub)
start=count=0
end=r
while True:
    pos=l.find(sub,start,end)
    if pos != -1:
        count+=1
        start=pos + s
    else:
        break
    if start>=r:
        break
print "NO. of occurences of",sub,":",count    
