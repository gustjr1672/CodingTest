from collections import deque

def bfs(graph, start, visted):
    queue = deque([start])
    visted[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visted[i]:
                queue.append(i)
                visted[i] = True


visted =[False] *9

graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

bfs(graph,1,visted)