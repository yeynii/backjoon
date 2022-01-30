# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

dp = [0, 1, 2, 4]

T = int(input())

for i in range(T):
  n = int(input())
  if len(dp) <= n:
    for j in range(len(dp), n + 1):
      dp.append(dp[j-1] + dp[j-2] + dp[j-3])
  print(dp[n])