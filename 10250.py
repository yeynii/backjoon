import math

T = int(input())
result = []

for i in range(T):
  H, W, N = map(int, input().split())

  leftNum = N % H
  if leftNum == 0:
    leftNum = H
  rightNum = math.ceil(N / H)

  leftstr = str(leftNum)
  rightstr = '0' + str(rightNum)
  rightstr = rightstr[-2:]
  print(leftstr + rightstr)