f=open(r"C:\Python27\ok.txt","r")
p=f.read()
size=len(p)
m=f.read()
bigsize=len(m.strip())
print size,bigsize
