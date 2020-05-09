import os
infile=open("marks.txt","r")
outfile=open("temp.txt","w")
nrollno=int(raw_input("Enter roll no:"))
nname=raw_input("Enter name:")
nmarks=float(raw_input("Enter marks:"))
nrec=str(nrollno)+","+nname+","+str(nmarks)+'\n'
count=0
rec=" "
while rec:
    rec=infile.readline()
    count=count+1
    if count==5:
        outfile.write(nrec)
        outfile.write(rec)
    else:
        outfile.write(rec)

infile.close()
outfile.close()
os.remove("marks.txt")
os.rename("temp.txt","marks.txt")
print"New record succefully added"
