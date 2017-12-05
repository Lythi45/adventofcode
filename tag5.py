import time

f=open("tag5.txt",'r')
cells=[]
for jump in f:
    cells.append(int(jump))

len_c=len(cells)
num_jumps=0
pos=0
while not (pos<0 or pos>=len_c):
    cells[pos]+=1
    pos+=cells[pos]-1
    num_jumps+=1
print(num_jumps)

start=time.clock()
f=open("tag5.txt",'r')
cells=[]
for jump in f:
    cells.append(int(jump))

len_c=len(cells)
num_jumps=0
pos=0

while not (pos<0 or pos>=len_c):
    offset=cells[pos]
    if offset>=3:
        cells[pos]-=1
    else:
        cells[pos]+=1
    pos+=offset
    num_jumps+=1
elapsed=time.clock()-start
print(elapsed,num_jumps)
