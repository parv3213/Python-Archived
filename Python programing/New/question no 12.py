my_points={"a":(4,3),"b":(1,2),"c":(5,1)}
def thanks():
    print "\n","\n","Made by Parv Garg, 11th-A","\n","Submitted to Sheela Kale Mam","\n","Thanks for using me","\n","#######################End#######################"
highest=[0,0]
init=0
for a in range(2):
    init=0
    for b in my_points.keys():
        val=my_points[b][a]
        if init ==0:
            highest[a]=val
        init +=1
        if val>highest[a]:
            highest[a]=val
        print "Maximun Value at index(my_points,",a,")=",highest[a]
        
thanks()
