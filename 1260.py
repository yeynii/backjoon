from collections import deque

def dfs(graph, start, visited):
  visited.append(start)
  print(start, end=' ')
  for node in graph[start]:
    if node not in visited:
      dfs(graph, node, visited)
      
def bfs(graph, start):
  queue = deque([start])
  visited = [start]
  while queue:
    currentNode = queue.popleft()
    print(currentNode, end=' ')
    for node in graph[currentNode]:
      if node not in visited:
        queue.append(node)
        visited.append(node)

n, m, v = map(int, input().split())
graph = list([] for _ in range(n+1))

for i in range(m):
  startNode, endNode = map(int, input().split())
  graph[startNode].append(endNode)
  graph[endNode].append(startNode)
  
for node in graph:
  node.sort()

dfs(graph, v, [])
print()
bfs(graph, v)