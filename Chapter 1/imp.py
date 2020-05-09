a=0
for a in range (100):
    x=float(raw_input("Enter the no.1:"))
    y=float(raw_input("Enter the no.2:"))
    z=float(raw_input("Enter the no.3:"))
    min=max=mid=0
    if x>y:
        if y>z:
           max,mid,min=x,y,z
        elif x>z:
            max,mid,min=x,z,y
        else:
            max,mid,min=z,x,y
    elif y>x:
        if x>z:
            max,mid,min=y,x,z
        elif y>z:
            max,mid,min= y,z,x
        else:
            max,mid,min=z,y,x
    print max,mid,min
