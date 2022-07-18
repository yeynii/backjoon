from math import ceil 

n, c, w = map(int, input().split())
trees = [int(input()) for _ in range(n)]
profits=[]
               
for L in range(1,max(trees)+1):
  profit = []
  for tree in trees:
    temp = (tree // L)*L*w - (ceil(tree / L)-1)*c
    if temp > 0:
      profit.append(temp)
  profits.append(sum(profit))

print(max(profits))