lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,30]
def thanks():
    print "\n","\n","Made by Parv Garg, 11th-A","\n","Submitted to Sheela Kale Mam","\n","Thanks for using me","\n","#######################End#######################"
slc1=lst[5:15:2]
slc2=lst[::4]
sum=0
avg=0
print "Slice 1"
for a in slc1:
    sum+=a
    print a,
print
print "Sum of elements of slice 1:",sum
sum=0
for a in slc2:
    sum+=a
    print a,
print
avg=sum/len(slc2)
print "Average a elements of slice 2:",avg
thanks()
