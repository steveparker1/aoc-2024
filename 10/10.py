#!/usr/bin/python3
from array import array
import sys


def findroute(found,initial,x,y,came_from):
    # See if there's a next step from x,y containing initial+1
    #from_here=[]
    if x<0 or y<0 or x==width or y==height:
        return None
    if grid[x][y]!=initial:
        return None
    if initial==9:
        a=(x,y)
        print(f"Got to a 9 at {y+1},{x+1} from {came_from} (really {x},{y})")
        #if (found.count(a)==0):
        print(f"Adding {x,y}")
        found.append((x,y))
    next_val=initial+1
    print(f"Found {initial} at {y+1},{x+1}. Looking for {next_val} from {y+1},{x+1} - came from {came_from}")
    a=findroute(found,next_val,x-1,y,"below")
    #if a!=None and len(a)>0:
        #print(f"Appending: {a}")
        #found.append(a)
    a=findroute(found,next_val,x+1,y,"above")
    #if a!=None and len(a)>0:
        #print(f"Appending: {a}")
        #found.append(a)
    a=findroute(found,next_val,x,y-1,"right")
    #if a!=None and len(a)>0:
        #print(f"Appending: {a}")
        #found.append(a)
    a=findroute(found,next_val,x,y+1,"left")
    #if a!=None and len(a)>0:
        #print(f"Appending: {a}")
        #found.append(a)
    return found

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
for x in range(width):
    for y in range(height):
        if grid[x][y]==0:
            foo=findroute([],0,x,y,"start")
            print(f"Foo is {foo}")
            print(f"Len is {len(foo)} from {x},{y}")
            ans.append(foo)
            print(f"Ans is currently {ans} at {x},{y}")

print(f"Final Ans = {ans}")
tot=0
print("-------------------------------")
for x in ans:
    for y in x:
        print(f"y={y} and len={len(y)}")
        if len(y)==2:
            tot=tot+1
print(f"Tot= {tot}")
#print(f"Ans = {set(ans)}")
