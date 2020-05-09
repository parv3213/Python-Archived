#buble sort
def bsort(a):
      i=0
      for i in range(len(a)):
            p=0
            temp=0
            for p in range(p+1,len(a)):
                  if a[p]<a[p-1] and p>=1:
                        temp=a[p-1]
                        a[p-1]=a[p]
                        a[p]=temp
a=[1,2,34,32,354,23,2,123,421,2.3,2.2,2.2223,2.2224]
print a
bsort(a)
print a 
                        
            
            
