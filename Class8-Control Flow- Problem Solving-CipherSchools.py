n=5
for i in range(n):
    for j in range(n):
        print(max([i+1,j+1,n-i,n-j]),end=" ")
    print()
print()
n=5
for i in range(n):
    for j in range(n):
        print((i,j),end=" ")
    print()
print()
n=5
for i in range(n):
    for j in range(n):
        print(max(i,j),end=" ")
    print()
print()
n=5
for i in range(n):
    for j in range(n):
        print(n-i-1,end=" ")
    print()
print()
n=5
for i in range(n):
    for j in range(n):
        print(n-j-1,end=" ")
    print()
print()
n=5
for i in range(n):
    for j in range(n):
        print(max(n-j-1,n-i-1),end=" ")
    print()
