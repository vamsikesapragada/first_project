# Ex6
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5:
            print("*",end=" ")
        elif j ==1 or j==5:
            print ("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# Ex7
k=1
for i in range(4,0,-1):
    for j in range(i):
        print(" ",end="")
    for p in range(k):
        print("*",end=" " )
    k+=1
    print()
X=3
for i in range(2,5):
    for j in range(i):
        print(" ",end="")
    for p in range(X):
        print("*",end=" " )
    X-=1
    print()

# Ex8
for i in range(5,0,-1):
    k=5
    for j in range(i):
        print(f"{k}",end=" ")
        k-=1
    print()
for h in range(2,6):
    k=5
    for l in range(h):
        print(f"{k}", end=" ")
        k-=1
    print()
# Ec
k=1
for i in range(6,0,-1):
    for j in range(i):
        print(" ",end=" ")
    for p in range(k):
        print("*",end=" " )
    k+=1
    print()
