import heapq
import sys
input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())
canSee = list(map(int, input().split()))
canSee[-1] = 0

graph = [[] for _ in range(n)]

for _ in range(m):
  a, b, t = map(int, input().split())
  graph[a].append((b, t))
  graph[b].append((a, t))

q = []
heapq.heappush(q, (0, 0))
distance = [inf] * n
distance[0] = 0
while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue
  for nxt, nxt_cost in graph[now]:
    cost = dist + nxt_cost
    if cost < distance[nxt] and canSee[nxt] == 0:
      distance[nxt] = cost
      heapq.heappush(q, (cost, nxt))

print(distance[-1] if distance[-1] < inf else -1)