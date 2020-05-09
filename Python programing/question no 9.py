def is_member(x,a):
    ln=len(a)
    for el in range(ln):
        if x==a[el]:
            return True
        return False 
x=eval(raw_input("Enter the string(single character):"))
a=eval(raw_input("Enetr the list:"))
print is_member(x,a)
def thanks():
    print "\n","\n","Made by Parv Garg, 11th-A","\n","Submitted to Sheela Kale Mam","\n","Thanks for using me","\n","#######################End#######################"
thanks()
