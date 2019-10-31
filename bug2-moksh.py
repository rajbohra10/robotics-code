import math

start = [0,0]
end = [100,100]
d = 0.0
mem = start

obstacles = [[[15,5],[15,20],[30,20],[30,5]],[[40,40],[40,50],[50,50],[50,40]]]

def getEuclidean(p1,p2):
    return math.sqrt((p2[0] - p1[0])**2+(p2[1] - p1[1])**2)
    
def getLine(p1,p2):
    if p2[0]==p1[0]:
        return (-999,0)
    if p2[1]==p1[1]:
        return (0,p2[1])
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    c = p2[1] - m*p2[0]
    return (m,c)

def getY(x,m,c):
    return int((m*x + c))
    
def isBetween(a,b,c):
    return getEuclidean(a,c) + getEuclidean(c,b) == getEuclidean(a,b)

def getBoundary(square,qh):
    print("\nIntersection (Hit) point:",qh)
    minimum = displacement
    ql = []
    for p in range(0,3):
        s = square[p]
        e = square[(p+1)%4]
        m,c = getLine(s,e)
        if m == -999:
            x = s[0]
            for y in range(s[1],e[1]+1):
                if isBetween(start,end,[x,y]):
                    ql = [x,y]
        elif m == 0:
            y = s[1]
            for x in range(s[0],e[0]+1):
                if isBetween(start,end,[x,y]):
                    ql = [x,y]
        else:
            for x in range(s[0],e[0]+1):
                y = getY(x,m,c)
                if isBetween(start,end,[x,y]):
                    ql = [x,y]
                    
    print("Leave point:",ql,"\n")
    d = distance(square,qh,ql)
    
    return (d,ql)
    
def distance(square,qh,ql):
    d = 0.0
    for p in range(0,3):
        s = square[p]
        e = square[(p+1)%4]
        if isBetween(s,e,qh):
            if isBetween(s,e,ql):
                d += getEuclidean(ql,qh)
            else:
                d += getEuclidean(qh,e)
            qh = e
    return d

def checkIntersection(square1,total,x,y,m,c,last):
    if isBetween(square1[0],square1[1],[x,y]) or isBetween(square1[1],square1[2],[x,y]) or isBetween(square1[2],square1[3],[x,y]) or isBetween(square1[3],square1[0],[x,y]):
        total += getEuclidean(last,[x,y])
        min,ql = getBoundary(square1,[x,y])
        total += min
        x = ql[0]
        last = ql
        m,c = getLine(ql,end)
    return (total,x,y,m,c,last)

# Total displacement
displacement = getEuclidean(start,end)
print("Initial values: ","\nqstart:",start,"\nqgoal:",end,"\nDisplacement:",round(displacement,2),"\n")

# Main line equation
m,c = getLine(start,end)
total = 0.0 
x = start[0]
last = start

while x <= 100:
    
    y = getY(x,m,c)
    
    # Checks if coinciding with obstacle
    for i in obstacles:
        total,x,y,m,c,last = checkIntersection(i,total,x,y,m,c,last)
    
    x += 1
    
total += getEuclidean(last,[x,y])
print("Total distance = ",round(total,2))

