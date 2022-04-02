#들어온 문자를 분리
location = input()
y = location[0]
x = location[1]
count = 0

#문자를 연산하기 위해 잠시 숫자로 변경
engTonum = {'a':1, "b":2 ,"c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
numToeng =  {1: 'a', 2: "b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h"}

#문자를 숫자로 변경
y = engTonum[y]
x= int(x)


#이동경우의 수
one =[1,-1]
two = [2,-2]

#경우의 수 계산
for i in two:
    for j in one:
        if y+i>0 and x+j>0:
            count+=1
            # 확인용 출력
            print(numToeng[y+i],x+j)
        if y+j and x+i>0:
            count+=1
            #확인용 출력
            print(numToeng[y + j], x + i)

print(count)