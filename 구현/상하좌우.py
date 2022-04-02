n = int(input())
move= input().split()
x,y=1,1

#상황에 따른 이동
for i in move:
    if i == 'R' and y+1 < n:
        y+=1
    elif i == 'L' and y-1 >0:
        y-=1
    if i == 'D' and x+1 < n:
        x+=1
    if i == 'U' and x-1 >0:
        x-=1

print(x,y)

