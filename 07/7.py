#!/usr/bin/python3
from array import array
import sys

def calc(operator,ans,target,x):
    if len(x)>0:
        #print(f"Calc ({operator},{ans},{target},{x}")
        #print(f"{len(x)}: ",end='')
        if operator=='+':
            ans = ans + x[0]
            #print(f"Adding got {ans}")
        elif operator=='*':
            ans = ans * x[0]
            #print(f"Multiplying got {ans}")
        elif operator=='|':
            ans = int(str(ans) + str(x[0]))
            #print(f"Concat got {ans}")
    else:
        return ans
    a1 = calc("+",ans,target,x[1:])
    a2 = calc("*",ans,target,x[1:])
    a3 = calc("|",ans,target,x[1:])
    if (a1==target):
        return a1
    elif (a2==target):
        return a2
    elif (a3==target):
        return a3
    return -1

if len(sys.argv) > 1:  # Read filename from CLI if provided
    input=sys.argv[1]
else:
    input="input.txt"

height=0
total=0
with open(input,'r') as f:
    for line in f.readlines():
        items=line.split(' ')
        items[0]=items[0].replace(':','')
        items = [int(item) for item in items]
        a1=calc("+",items[1],items[0],items[2:])
        a2=calc("*",items[1],items[0],items[2:])
        a3=calc("|",items[1],items[0],items[2:])
        #print(f"a1 = {a1}")
        #print(f"a2 = {a2}")
        #print(f"a3 = {a3}")
        if (a1 == items[0]):
            total=total+a1
        elif (a2 == items[0]):
            total=total+a2
        elif (a3 == items[0]):
            total=total+a3

print(f"Total = {total}")
