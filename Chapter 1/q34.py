a=b=c=0
while True:
    a=raw_input("Enter:")
    if a=="done":
        print "done"
        print c
        break
    else:
        b=int(a)
        c+=b
