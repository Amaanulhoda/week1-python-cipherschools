a=1
while a<10:
    print(a)
    a+=1
    
name="Amaan"
print(type(name))
for c in name:
    print(type(c))
print(name.__iter__)

for i in range(5):
    print(i)
    if i==3:
        break

if True:
    pass
print("rest of the code")

for i in range(4):
    print(i)
else:
    print("something")

for i in range(4):
    print(i)
    if i==2:
        break
else:
    print("abc")
