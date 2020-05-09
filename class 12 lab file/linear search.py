def lsearch(ar,item):
    i=0
    if ar[0]==item:
          return 0
    while i<len(ar) and ar[i]<>item:
          i+=1
    if i<len(ar):
          return i
    else:
          return None

n = input("Enter the size of the list:-")
print "Enter elements for list"
ar=[0]*n
for i in range(n):
          ar[i]= input("Element"+str(i+1)+":")
item=input("Enter the element to be searched:-")
index= lsearch(ar,item)
if index<> None:
          print "Element fount at index:",index,"Position:",(index+1)
else:
          print "Sorry Element not found"

