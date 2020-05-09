def bs(l):
    for m in range (len(l)-1):
        i=0
        while i<len(l)-1:
            if l[i]>l[i+1]:
                t=l[i]
                l[i]=l[i+1]
                l[i+1]=t
            i=i+1
    return l
l=[12,145,34,4234,34,1]
print "Original list is:-",l
print "Final list is:-",bs(l)
    
