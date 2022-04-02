import time
n,m = map(int,input().split())
card = [list(map(int,(input().split()))) for _ in range(n)]


for i in range(n):
    card[i].sort()
answer = card[0][0]

for i in range(n):
    if answer < card[i][0]:
        answer = card[i][0]

print(answer)

