import math

A, B, V = map(int, input().split())
day = 0
distance = V - A 
day += 1
if distance > 0:
  day += math.ceil(distance / (A-B))
print(day)