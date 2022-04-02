n , m , k = map(int,input().split())

num = list(map(int,input().split()))
num.sort(reverse= True)

sum = 0
i = k

while(m!=0):
    if k !=0:
        sum += num[0]
        m-=1
        k-=1

    elif k==0:
        sum += num[1]
        m-=1
        k = i

print(sum)


