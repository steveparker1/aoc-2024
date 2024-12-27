#!/usr/bin/python3
# 262 is too low
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

def part2(line):
    dampened=False
    for i in range(len(line)):
        line[i]=int(line[i])
    if line[1] > line[0]:
        direction="up"
        last=line[0]-1
    else:
        direction="down"
        last=line[0]+1
    print(f"Direction: {direction}")
    for i in range(len(line)):
        if (not (safe(direction,line[i],last))):
            if not dampened:
                dampened=True
                if i==len(line)-1:
                    return True
                if (not (safe(direction,line[i+1],last))):
                    return False
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
    if part2(i.split()):
        print(f"{i.rstrip()} is safe")
        total=total+1
    else:
        print(f"{i.rstrip()} is not safe")
f.close()
print(f"Total: {total}")

