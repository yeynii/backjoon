import sys
from collections import deque
input = sys.stdin.readline

def grouping(i, j): # 섬마다 번호 붙이기
    q = deque([(i, j)])
    world[i][j] = gid
    while q:
        qi, qj = q.popleft()
        for t in range(4):
            nx, ny = qi + dx[t], qj + dy[t]
            if 0 <= nx < n and 0 <= ny < n:
                if world[nx][ny] == 1:
                    world[nx][ny] = gid
                    q.append((nx, ny))
                elif world[nx][ny] == 0 :
                    ocean.append((qi, qj))

def get_distance(): # 모든 섬에서 동시에 확장
    loop = 0
    ans = sys.maxsize
    while ocean:
        loop += 1
        length = len(ocean)
        for _ in range(length):
            oi, oj = ocean.popleft()
            for t in range(4):
                nx, ny = oi + dx[t], oj + dy[t]
                if 0 <= nx < n and 0 <= ny < n:
                    if world[nx][ny] == 0: 
                        world[nx][ny] = world[oi][oj]
                        ocean.append((nx, ny))
                    elif world[nx][ny] < world[oi][oj]:
                        ans = min(ans, (loop - 1) * 2)
                    elif world[nx][ny] > world[oi][oj]:
                        ans = min(ans, loop * 2 - 1)
    return ans

dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
n = int(input())
world = [list(map(int, input().split())) for _ in range(n)]
ocean = deque()
gid = -1

for i in range(n):
    for j in range(n):
        if world[i][j] == 1:
            grouping(i, j)
            gid -= 1

print(get_distance())