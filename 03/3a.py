#!/usr/bin/python3

def mul(s):
    state="i" # reading "i" then "," then "j" then ")"
    thisnum=""
    for c in s:
        print(f"c = {c}")
        if (c.isdigit()):
            thisnum = thisnum + c
        elif c==',':
            i=int(thisnum)
            if i>999:
                return 0
            thisnum=""
            state='j'
        elif c==')':
            if (state!="j"):
                return 0 # invalid state
            else:
                j=int(thisnum)
                if j>999:
                    return 0
                return i * j
                
    print("Can't get here?")
    return 0



import sys

if len(sys.argv) > 1:  # Read JSON filename from CLI if provided
    input=sys.argv[1]
else:
    input="input.txt"
total=0

with open(input, 'rb') as f:
    contents = f.read().decode()
    for chunk in contents.split('mul('):
        print (chunk[:8])
        total = total + mul(chunk[:8])
print(f"Total is {total}")

