#!/usr/bin/python3
from array import array
import sys

rules={}

def okay(i, a):
    for j in a:
        print(f"Checking {j} against {i}")
        if j in i:
           #print(f"that's not okay")
           return False
    return True


def add_rule(s):
    print(f"s is {s}")
    x = s.split('|')
    rules.setdefault(int(x[1]), []).append(int(x[0]))
    
def check_update(s):
    print(f"S is {s}")
    x = array("i",list(map(int,s.split(','))))
    print(f"x is {x}")
    for idx,y in enumerate(x):
        print(f"Y is {idx}")
        if y in rules:
            r=rules.get(y)
            #print(f"{y} must come after: {r}")
            if not okay(x[idx:],r):
                return -1
    mid=int(len(x)/2)
    print(f"Mid is {mid}")
    return x[mid]
        
  

if len(sys.argv) > 1:  # Read JSON filename from CLI if provided
    input=sys.argv[1]
else:
    input="input.txt"

total=0
with open(input) as file:
    for line in file:
        if "|" in line:
            add_rule(line)
        elif "," in line:
            res=check_update(line)
            if res>0:
               print(f"{line.rstrip()} is okay. res = {res}")
               total = total + res
            else:
               print(f"{line.rstrip()} is not okay")


#print(f"Rules are {rules}")
print(f"Total is {total}")
