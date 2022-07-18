n = int(input())
array = []
dp = [0 for i in range(n)]
dp[0] = 1

for i in range(n):
  array.append(int(input()))
  
for i in range(1, n):
    temp = []
    for j in range(i):
        if array[i] > array[j]:
            temp.append(dp[j])
    if not temp:
        dp[i] = 1
    else:
        dp[i] = max(temp) + 1
print(dp)
print(n - max(dp))

      

# 3 7 5 2 6 1 4
