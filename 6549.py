import sys
input = sys.stdin.readline

def maxSize():
    max_size = 0
    stack = []

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
    n, *heights = map(int, input().split())
    if n == 0: 
        break
    print(maxSize())