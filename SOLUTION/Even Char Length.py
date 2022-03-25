#To Enter 5 String in a List and check and Print String whose Length has Even Number of Character
l=[]
def createList():
    for i in range(1,6):
        x=input("Enter String:")
        l.append(x)
        
def len(l):
    x=[]
    c=0
    for i in l:
        for j in i:
            c=c+1

        if c%2==0:
            x.append(i)
        c=0
    return x

createList()
ans=len(l)
print(ans)
