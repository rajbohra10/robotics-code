def eucd(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**(0.5)

def lin(x,y):
    if(x==y):
        return True
    return False
    
def obs(x,y,xd,yd):
    l=[x,y]
    dist=list()
    i=j=0
    ld=[[x,y+1],[x,y+2],[x,y+3],[x+1,y+3],[x+2,y+3],[x+2,y+2],[x+2,y+1],[x+2,y+1]] #Obstacle boundary coordinates
    t=0
    dist=list()
    for i in range(len(ld)):
        print("(",ld[t][0],",",ld[t][1],")")
        dist.append(eucd(ld[t][0],ld[t][1],xd,yd))
        if(lin(ld[t][0],ld[t][1])):
            print("Leave boundary at coordinate : ","(",ld[t][0],",",ld[t][1],")")
            break
        t+=1
    return min(dist)
    
print("Enter initial state coordinates")
x1=int(input("Enter x : "))
y1=int(input("Enter y : "))

init=[x1,y1]

print("Enter goal state coordinates")
x2=int(input("Enter x : "))
y2=int(input("Enter y : "))

goal=[x2,y2]

d=eucd(x1,y1,x2,y2)

l=list()
n=int(input("Enter the no. of obstacles : "))
print("Enter the coordinates of the ",n," obstacles")
for i in range(n):
    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    l.append(x)
    l.append(y)
    
f=list()
for i in range(20):
    f.append(0)

for i in range(x1,x2+1):
    if(i==x1 or i==x2):
        f.insert(i,2)
    elif(i==x):
        f.insert(i,1)
    else:
        f.insert(i,0)

print(f)
print("\n\n")    
store=0 #disance
dd=1    #increment
temp=0
xx=x1
yy=y1
print("(",xx,",",yy,")")
print("|")
print("|")
for i in range(0,x2+1):
    xx+=dd
    yy+=dd
    print("(",xx,",",yy,")")
    if(f[xx]==2):  #if goal state is met
        break
    elif(f[xx]==0): #if blank coordinate in space
        store=store+eucd(x1,y1,x1+1,y1+1)
    elif(f[xx]==1): #obstacle
        xx-=1
        yy-=1
        p=obs(xx,yy,x2,y2)
        store+=(d-p+1)
        xx+=1
        yy+=1
    print("|")
    print("|")

print("\n\nDISTANCE BETWEEN 'init' and 'goal'  : ",store)
