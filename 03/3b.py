#!/usr/bin/python3
# 110927584 is too low
# 175015740 is too high

def split(delimiters, string, maxsplit=0): # https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
    import re
    #regex_pattern = '|'.join(map(re.escape, delimiters))
    regex_pattern = '|'.join('(?<={})'.format(re.escape(delim)) for delim in delimiters)
    return re.split(regex_pattern, string, maxsplit)

def func(s):
    global ENABLED,F
    print(f"Parsing '{s}' with F={F} and ENABLED={ENABLED}")
    NEXTF=""
    if s.endswith("do()"):
        NEXTF="do"
    elif s.endswith("don\'t()"):
        NEXTF="dont"
    elif s.endswith("mul("):
        NEXTF="mul"
    if ENABLED=="y" and F=="mul":
        print("Calling mul")
        ans=mul(s)
    else:
        ans=0
    F=NEXTF
    if F=="do":
      ENABLED="y"
      print("Enabled")
    elif F=="dont":
      ENABLED="n"
      print("Disabled")
    return ans


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
                print(f"Returning {i} * {j} = {i*j}")
                return i * j
        else:
            return 0 # invalid
                
    print("Can't get here?")
    return 0



import sys

if len(sys.argv) > 1:  # Read JSON filename from CLI if provided
    input=sys.argv[1]
else:
    input="input.txt"
total=0
F=""
ENABLED="y"

with open(input, 'rb') as f:
    contents = f.read().decode()
    #for chunk in contents.split('mul('):
    for chunk in split(['do()','don\'t()','mul('], contents, 0):
        print (chunk)
        total = total + func(chunk)
print(f"Total is {total}")

