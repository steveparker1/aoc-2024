#!/usr/bin/python3
import sys

if len(sys.argv) > 1:  # Read JSON filename from CLI if provided
    input=sys.argv[1]
else:
    input="input.txt"

f=open(input,"r")
lines=f.readlines()
list1=[]
list2=[]
for i in lines:
    list1.append(int(i.split()[0]))
    list2.append(int(i.split()[1]))
f.close()

list1.sort()
list2.sort()

a1=0
a2=0
for i in range(len(list1)):
  #print(f"{list1[i]} - {list2[i]} = {abs(list1[i] - list2[i])}")
  a1=a1 + abs(list1[i] - list2[i])
  a2 = a2 + (list2.count(list1[i]) * list1[i])

print(f"Answer 1 : {a1}")
print(f"Answer 2 : {a2}")


