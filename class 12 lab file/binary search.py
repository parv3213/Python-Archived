def bsearch(ar,item):
    b=0
    l=len(ar)-1
    while (b<=l):
        m=(b+l)/2
        if item==ar[m]:
            return m
        elif item>ar[m]:
            b=m+1
        else:
            l=m-1
    else:
        return None
n= input ("Enter the size of list:-")
print "Enter elements for list"
ar=[0]*n
for i in range(n):
    ar[i]=input("Element"+str(i+1)+":")
item=input("Enter the element to be searched:-")
index=bsearch(ar,item)
if index<> None:
    print "Element found at index:",index,"position",(index+1)
else:
    print "Sorry Element not found"
