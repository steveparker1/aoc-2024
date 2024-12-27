#!/usr/bin/python3
from array import array
import sys


def findroute(found,initial,x,y,came_from):
    # See if there's a next step from x,y containing initial+1
    #from_here=[]
    if x<0 or y<0 or x==width or y==height:
        return 0
    if grid[x][y]!=initial:
        return 0
    if initial==9:
        a=(x,y)
        print(f"Got to a 9 at {y+1},{x+1} from {came_from} (really {x},{y})")
        if (found.count(a)==0):
            print(f"Adding {x,y}")
            found.append((x,y))
            return 1
        else:
            print(f"Already have {x,y}")
    next_val=initial+1
    print(f"Found {initial} at {y+1},{x+1}. Looking for {next_val} from {y+1},{x+1} - came from {came_from}")
    a=0
    a=a+findroute(found,next_val,x-1,y,"below")
    #if a!=None and len(a)>0:
        #print(f"Appending: {a}")
        #found.append(a)
    a=a+findroute(found,next_val,x+1,y,"above")
    #if a!=None and len(a)>0:
        #print(f"Appending: {a}")
        #found.append(a)
    a=a+findroute(found,next_val,x,y-1,"right")
    #if a!=None and len(a)>0:
        #print(f"Appending: {a}")
        #found.append(a)
    a=a+findroute(found,next_val,x,y+1,"left")
    #if a!=None and len(a)>0:
        #print(f"Appending: {a}")
        #found.append(a)
    return a

if len(sys.argv) > 1:  # Read filename from CLI if provided
    input=sys.argv[1]
else:
    input="input.txt"

grid=[]
width=0
height=0
with open(input,'r') as f:
    for line in f.readlines():
        #print(f"Line = {line}")
        line=list(line.strip())
        #line = [int(item) for item in list(line.strip())]
        foo=[]
        for n in line:
            if n=='.':
                foo.append(-1)
            else:
                foo.append(int(n))
        grid.append(foo)
        width=len(line)
        height=height+1

print("=#=#=#=#=#=#=#=#= have read the data =#=#=#=#=#=#=#=#=#")
ans=[]
tot=0
for x in range(width):
    for y in range(height):
        if grid[x][y]==0:
            foo=findroute([],0,x,y,"start")
            tot=tot+foo
            #ans.append(foo)
            print(f"Ans is currently {foo} at {x},{y}")
print(f"Total= {tot}")
