import sys
input = sys.stdin.readline

n = int(input())
coins = []
for _ in range(n):
  coin, count = map(int, input().split())
  coins.append([coin]*count)

coins = sum(coins,[])
coins.sort()

sum = 0
aim = coins / 2

while coins:
  temp = coins.pop()
  print(temp)
  
print(coins)
  