import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-2):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
def bfs(start, visited):
  temp = [start]
  visited[start] = True
  queue = deque(graph[start])
  while queue:
    current = queue.popleft()
    temp.append(current)
    visited[current] = True
    for i in graph[current]:
      if not visited[i]:
        queue.append(i)
  return temp

map = []
for i in range(1, n+1):
  if not visited[i]:
    map.append(bfs(i,visited))

print(map[0][0],map[1][0])