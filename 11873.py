import sys
input = sys.stdin.readline

def maxSize(heights):
    max_size = 0
    stack = []
    n = len(heights)
    for i in range(n):
        left = i
        while stack and stack[-1][0] >= heights[i]:
            h, left = stack.pop()
            tmp_size = h * (i - left)
            max_size = max(max_size, tmp_size)
        stack.append([heights[i],left])
        
    for h, point in stack:
        max_size = max(max_size, (n-point)*h)

    return max_size
 
while True:
    N, M = map(int,input().split())
    if N == 0 and M == 0:
      break
    
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(1,N):
        for j in range(M):
            if arr[i][j] != 0:
                arr[i][j] = arr[i-1][j] + 1
    max_rect = 0
    for a in arr:
        temp = maxSize(a)
        if temp > max_rect:
            max_rect = temp
    print(max_rect)