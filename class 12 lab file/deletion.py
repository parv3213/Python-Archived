def bsearch(ar,item):
      beg=0
      last=len(ar)-1
      while beg<=last:
            mid=(beg+last)/2
            if item==ar[mid]:
                  return mid
            elif item>ar[mid]:
                  beg+=1
            else:
                  beg-=1
ar=[1,2,3,4,5,6,7,8]
print "List is:",ar
item=int(raw_input("Enter element to be deleted:"))
pos=bsearch(ar,item)
if pos:
      del ar[pos]
      print ar
else:
      print "Not found"

      
