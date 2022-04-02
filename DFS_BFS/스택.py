#선입후출 , 후입선출
stack = []

stack.append(4)
stack.append(3)
stack.append(2)
stack.pop()
stack.append(1)

#입력 순서대로 출력
print(stack)

#반대로 출력
print(stack[::-1])
stack.reverse()
print(stack)

