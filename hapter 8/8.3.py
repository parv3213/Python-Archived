c=int(raw_input("Enter the no of students:"))
fil=open("marks.txt","w")
for i in range (c):
    print "Enter the details", (i+1),"Below:"
    r=input("Enter the rollno:")
    name=raw_input("Enter name:")
    marks=float(raw_input("Enter the marks:"))
    al=str(r)+","+name+","+ str(marks) + "\n"
    fil.write(al)
fil.close()
