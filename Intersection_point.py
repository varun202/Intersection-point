def intersection_point(line1,line2):#Calculate the intersection point function
    x1=line1[0]#Take four coordinates
    y1=line1[1]
    x2=line1[2]
    y2=line1[3]
    x3=line2[0]
    y3=line2[1]
    x4=line2[2]
    y4=line2[3]
    #k ---> slope of the line
    #b ----> intercept of the line
    if (x2-x1)!=0 and (x4-x3)!=0:
        k1=(y2-y1)*1.0/(x2-x1)
        b1=y1*1.0-x1*k1*1.0
        k2=(y4-y2)*1.0/(x4-x3)
        b2=y3*1.0-x3*k2*1.0
        x=(b2-b1)*1.0/(k1-k2)
        y=(k1*b2-k2*b1)*1.0/(k1-k2)
    elif (x2-x1)==0 and (x4-x3)==0:
        return "lines are parallel"
    elif (x2-x1)==0:
        x=x1*1.0
        k2=(y4-y2)*1.0/(x4-x3)
        b2=y3*1.0-x3*k2*1.0
        y=k2*x+b2
    elif (x4-x3)==0:
        x=x3*1.0
        k1=(y2-y1)*1.0/(x2-x1)
        b1=y1*1.0-x1*k1*1.0
        y=k1*x+b1
    if (x>x1 or x>x3) or (x<x1 or x<x3):
        return "line segments doesnot intersect"
    return [x,y]
line1=list(map(int,input().split()))#taking co-ordinate points of the line1
line2=list(map(int,input().split()))#taking co-ordinate points of the line2
print(intersection_point(line1,line2))
