import bisect

list1=[10,20,30,40]
print "list is:",list1
item=int(raw_input("Enter element to be inserted:"))
ind=bisect.bisect(list1,item)
bisect.insort(list1,item)
print "position:",ind+1
print "list after insertion:",list1
