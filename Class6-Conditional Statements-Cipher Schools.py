#Conditional Statements

a=True
if True:                         #Colon in python represents starting of a block
    print("the value is true")   #1 indent= 2 spaces, 4 spaces, 8 spaces
print("end")


a=False
if a:
    print("this value is true")
else:
    print("this value is false")
    
a=5
if a==4:
    print("this value is 4")
elif a==5:
    print("this value is 5")
else:
    print("this value is not 4 or 5")
