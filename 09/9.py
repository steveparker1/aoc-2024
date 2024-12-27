#!/usr/bin/python3
from array import array
import sys

def getNextEmpty(i):
    while blocks[i]>=0:
        i=i+1
    return i

if len(sys.argv) > 1:  # Read filename from CLI if provided
    input=sys.argv[1]
else:
    input="input.txt"

i = list(open(input).read().strip())
#print(f"0 is {i[0]}, and 1 is {i[1]}")
i = [int(item) for item in i]

isFile=True
fileId=0
blocks=[]
n=0

for b in i:
    #print(f"Processing {b}")
    if isFile:
        #blocks[n]=fileId
        for x in range(b):
            blocks.append(fileId)
        fileId=fileId+1
    else:
        #blocks[n]=-1 # unused
        for x in range(b):
            blocks.append(-1)
    isFile=not isFile
    n=n+1

for b in blocks:
    if b==-1:
        print(".",end='')
    else:
        print(b,end='')
print("\n")

nextEmpty=getNextEmpty(0) # index of next empty block of disk space
b=len(blocks)-1
while b>nextEmpty:
    if blocks[b]>=0:
        blocks[nextEmpty]=blocks[b]
        blocks[b]=-1
        nextEmpty=getNextEmpty(nextEmpty)
    b=b-1
        
    #print(f"{blocks[b]}",end='')
print("Done")
total=0
for b in range(len(blocks)):
    if blocks[b]>=0:
        total = total + (b*blocks[b])
print("\n")
print(f"Checksum = {total}")

