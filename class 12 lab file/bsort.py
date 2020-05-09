def bsort(ar):
      for i in range(len(ar)-1):
            a=0
            for a in range(1,len(ar)):
                  if ar[a-1]>ar[a]:
                        t=ar[a-1]
                        ar[a-1]=ar[a]
                        ar[a]=t
a=[1,23,213,35,46,75,35,876]
print a
bsort(a)
print a

                  
                        
