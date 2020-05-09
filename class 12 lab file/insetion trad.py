def findpos(ar,item):
      size=len(ar)
      if item<=ar[0]:
            #item is less than or equal to the first element
            return 0
      else:
            pos=-1
            for i in range(size-1):
                  if (item>=ar[i]) and (item<ar[i+1]):
                        pos=i+1
                        break
            if (pos==-1)and i<=size-1:
                  print "i=",i
                  pos=size
            return pos
def shift(ar,pos,item):
      ar.append(None)
      size=len(ar)
      i=size-1
      while i>pos:
            ar[i]=ar[i-1]
            i-=1
            print ar
      ar[pos]=item
      return ar
            
            
ar=[1,2,8,10,12,16]
print "LIST:",ar
item=float(raw_input("Enter element to be inserted:"))
pos=findpos(ar,item)
aar=shift(ar,pos,item)
print pos
print "Inserted List:",aar


