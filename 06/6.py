#!/usr/bin/python3
# 4579 too low
# 4580 is right! Not even sure why! :-)
from array import array
import sys

grid=[]
x=-1
y=-1
direction="up"


def inside_grid():
    if x<0 or y<0:
        return False
    if x>width or y>height:
        return False
    return True

def rotate():
    global direction
    print(f"Rotating from {direction}...")
    if direction=="up":
        direction="right"
    elif direction=="down":
        direction="left"
    elif direction=="right":
        direction="down"
    elif direction=="left":
        direction="up"
    else:
        print("Where to?")
    print(f"New direction: {direction}")

def blocked(i,j):
    try:
        if grid[j][i]=='#':
            return True
    except:
        pass
    return False

def move():
    global x,y,direction
    print(f"Guard is at {x},{y}, going {direction}")
    if direction=="up":
        if y==0:
            return False
        else:
           if blocked(x,y-1):
               rotate()
           else:
               y=y-1
    elif direction=="down":
        if y==height:
            return False
        else:
            if blocked(x,y+1):
                rotate()
            else:
                y=y+1
    elif direction=="right":
        if x==width-1:
            return False
        else:
            if blocked(x+1,y):
                rotate()
            else:
                x=x+1
    else: # left
        if x==0:
            return False
        else:
            if blocked(x-1,y):
                rotate()
            else:
                x=x-1
    try:
        grid[y][x]='1'
    except:
        return False
    return True
        

if len(sys.argv) > 1:  # Read filename from CLI if provided
    input=sys.argv[1]
else:
    input="input.txt"

height=0
with open(input,'r') as f:
    for line in f.readlines():
        #grid.append(line)
        grid.append(list(line))
        if x<0:
            x=line.find('^')
            if x>0: # found it
                y=height
                width=len(line) # only grab this once
        height=height+1
if (y<0) or (x<0):
    print("Could not find the guard!")
    sys.exit(1)

print(f"Guard is at {x},{y}")
print(f"{grid[y][x]}")
while move():
    print("moving...")
    #move()
ans = sum(x.count('1') for x in grid)
#print(f"Moves: {grid.count('1')}")
print(f"Moves: {ans}")
#print(f"{grid}")
