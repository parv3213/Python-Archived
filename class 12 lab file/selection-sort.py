def selection_sort(list1):
    for a in range(len(list1)):
        l=a
        print list1
        for r in range(a+1,len(list1)):
            if list1[r]<list1[l]:
                l=r
                
        #swap the two values
        t=list1[l]
        list1[l]=list1[a]
        list1[a]=t
#main..........
list1=[15,6,13,22,3,52,2]
print"Original liat is:",list1
selection_sort(list1)
print"list after sorting:",list1
