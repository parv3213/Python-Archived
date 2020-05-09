def isi(l):
    for i in range (1,len(l)):
        a=l[i]
        j=i
        
        while l[j-1]>a and j>=1:
            l[j]=l[j-1]
            print l
            j-=1
        l[j]=a
        print l
l=[12,13,1,4,175,342,121]
print "Original list-",l
isi(l)
print "Sorted list-",l

