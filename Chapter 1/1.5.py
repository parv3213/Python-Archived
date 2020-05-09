a=int(raw_input("Enter the salary of the person:"))
if a>=40000:
    print "Tax % is:12%"
    b=a*(0.12)
elif a>=20000:
    print "Tax % is:10%"
    b=a*(0.10)
elif a>=10000:
    print "Tax % is:5%"
    b=a*(0.5)
elif a<1000:
    print "Tax is 0%"
    b=0
print b
print "thank You!"
