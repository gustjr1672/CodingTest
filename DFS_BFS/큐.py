from collections import deque

queue = deque()

queue.append(4)
queue.append(3)
queue.append(2)
queue.popleft()
queue.append(1)

#입력 순서대로 출력
print(list(queue))
print(queue)
#반대로 출력

print(list(queue)[::-1])
queue.reverse()
print(queue)