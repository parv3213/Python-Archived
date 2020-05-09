fil=open("marks.txt","r")
f=fil.readlines()
i=1
for p in f:
    onerec=p.split(',')
    print onerec
    r=int(onerec[0])
    name=onerec[1]
    marks=float(onerec[2])
    print "Record",i,"contains:",r,name,marks
    i+=1
fil.close()
    
