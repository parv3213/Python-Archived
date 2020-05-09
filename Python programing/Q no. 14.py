b=int(raw_input("Enter the number of products"))
def thanks():
    print "\n","\n","Made by Parv Garg, 11th-A","\n","Submitted to Sheela Kale Mam","\n","Thanks for using me","\n","#######################End#######################"
dict={}
for i in range(b):
    n=(raw_input("Enter the name of product"))
    value=int(raw_input("Enter the price of product"))
    dict[n]=value
print dict
thanks()
