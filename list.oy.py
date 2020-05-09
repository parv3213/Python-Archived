def search(a,b):
    i=0
    while i< len(a) and a[i]!=b:
        i+=1
    if i<len(a):
        return i
    else:
         return False


#-----main-----

n=int(raw_input("enter the desired linear size list..."))
print "enter elements for linear lists"
a=[0]*n
for i in range(n):
      a[i]=int(raw_input("elements"+str(i)+":"))

b=int(raw_input("enter elements to be serached for"))
d=search(a,b)
if d:
    print "element found",d,"positin",(d+1)
else:
    print "No element found"
