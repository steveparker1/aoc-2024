#!/usr/bin/python3
# 289 is too low
# Safe:
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

import sys

def safe(direction, i, j):
    diff = i-j
    if abs(diff)>3 or abs(diff)<1:
        print(f"{j} to {i} not safe")
        return False
    if diff > 0:
        if direction=="down":
            print(f"{j} to {i} not safe")
            return False
    else:
        if direction=="up":
            print(f"{j} to {i} not safe")
            return False
    return True

def get_direction(i,j):
      if i>j:
          return "down"
      return "up"

def part2(dampened,line):
    for i in range(len(line)):
        line[i]=int(line[i])
    direction=get_direction(line[0],line[1])
    if direction=="up":
        last=line[0]-1
    else:
        last=line[0]+1
    print(f"Direction: {direction}")
    for i in range(len(line)):
        if (not (safe(direction,line[i],last))):
            if not dampened:
                dampened=True
                newlist = line[:i-2] + line[i-1:]
                print(f"Testing first: {newlist}")
                if part2(True,newlist):
                    return True
                else:
                    newlist = line[:i-1] + line[i:]
                    print(f"Testing again: {newlist}")
                    if part2(True,newlist):
                        return True
                    else:
                        newlist=line[:i] + line[i+1:]
                        print(f"Final test: {newlist}")
                        return part2(True,newlist)
            else:
                return False
        last=line[i]
    return True

def part1(line):
    for i in range(len(line)):
        line[i]=int(line[i])
    if line[1] > line[0]:
        direction="up"
        last=line[0]-1
    else:
        direction="down"
        last=line[0]+1
    for i in range(len(line)):
        if (not (safe(direction,line[i],last))):
            return False
        last=line[i]
    return True
          
  
if len(sys.argv) > 1:  # Read JSON filename from CLI if provided
    input=sys.argv[1]
else:
    input="input.txt"
total=0

f=open(input,"r")
lines=f.readlines()
for i in lines:
    print(f"\nChecking {i.rstrip()}")
    if part2(False,i.split()):
        print(f"{i.rstrip()} is safe")
        total=total+1
    else:
        print(f"{i.rstrip()} is not safe")
f.close()
print(f"Total: {total}")

