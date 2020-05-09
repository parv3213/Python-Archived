def isi(l):
    for i in range (1,len(l)):
        a=l[i]
        j=i
        
        while l[j-1]>a and j>=1:
            l[j]=l[j-1]
            j-=1
        l[j]=a
        print l
l=[12,13,4]
print "Original list-",l
isi(l)
print "Sorted list-",l
