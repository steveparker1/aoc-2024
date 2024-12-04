#!/usr/bin/python3
# XMAS: 2453 too high (2447)
# X-MAS: 5424 too high, 1416 too low
import sys

def find_x_mas(row,col):
    ans=0
    if chr(contents[row][col])=='A':
        try: # topleft
            tl=chr(contents[row-1][col-1])
        except:
            tl='-'
        try: # topright
            tr=chr(contents[row-1][col+1])
        except:
            tr='-'
        try: # bottomleft
            bl=chr(contents[row+1][col-1])
        except:
            bl='-'
        try: # bottomright
            br=chr(contents[row+1][col+1])
        except:
            br='-'
        if (tl=='M' and br=='S') and (tr=='M' and bl=='S'): ans = 1
        if (tl=='M' and br=='S') and (tr=='S' and bl=='M'): ans = 1
        if (tl=='S' and br=='M') and (tr=='M' and bl=='S'): ans = 1
        if (tl=='S' and br=='M') and (tr=='S' and bl=='M'): ans = 1
        if (ans>0):
            print(f"Found {ans} at ({row},{col})")
        #if (tl=='M' and br=='S'): ans = ans + 1
        #if (tl=='S' and br=='M'): ans = ans + 1
        #if (tr=='S' and bl=='M'): ans = ans + 1
        #if (tr=='M' and bl=='S'): ans = ans + 1
    return ans

def find_string(row,col,s):
    #print(f"Looking for {s} in {row},{col}")
    # up-down
    ans=0
    try:
        i=chr(contents[row][col]) + chr(contents[row+1][col]) + chr(contents[row+2][col]) + chr(contents[row+3][col])
        if (i==s): 
            #print(f"Found {s} at ({row},{col}) looking up-down")
            ans = ans + 1
    except:
        pass
    # left-to-right
    try:
        i=chr(contents[row][col]) + chr(contents[row][col+1]) + chr(contents[row][col+2]) + chr(contents[row][col+3])
        if (i==s): 
            ans = ans + 1
    except:
        pass
    # Diagonal down-right
    try:
        i=chr(contents[row][col]) + chr(contents[row+1][col+1]) + chr(contents[row+2][col+2]) + chr(contents[row+3][col+3])
        if (i==s): 
            ans = ans + 1
    except:
        pass
    # Diagonal up-right
    try:
        i=chr(contents[row][col]) + chr(contents[row+1][col-1]) + chr(contents[row+2][col-2]) + chr(contents[row+3][col-3])
        if (i==s): 
            ans = ans + 1
    except:
        pass
    return ans

      




if len(sys.argv) > 1:  # Read JSON filename from CLI if provided
    input=sys.argv[1]
else:
    input="input.txt"
xmas=0
x_mas=0

with open(input, 'rb') as f:
    contents = f.readlines()
    # index as contents[col][row]
    numrows = len(contents)
    numcols = len(contents[0])
    for row in range(numrows):
        for col in range(numcols):
            #print(chr(contents[row][col]))
            xmas = xmas + find_string(row,col,"XMAS")
            xmas = xmas + find_string(row,col,"SAMX")
            x_mas = x_mas + find_x_mas(row,col)

print(f"Total XMAS: {xmas}")
print(f"Total X-MAS: {x_mas}")
