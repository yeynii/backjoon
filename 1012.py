# 유기농 배추
from collections import deque

def bfs(graph, x, y):
  if graph[y][x] == 0:
    return 0
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    graph[y][x] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= m or ny >= n:
        continue
      if graph[ny][nx] == 1:
        queue.append((nx, ny))
        graph[ny][nx] = 0
  return 1

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

for test in range(T):
  m, n, k = map(int, input().split())
  graph = [[0 for col in range(m)] for row in range(n)]
  
  for i in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1

  count = 0

  for i in range(n):
    for j in range(m):
      count += bfs(graph, j, i)
      
  result.append(count)

for r in result:
  print(r)